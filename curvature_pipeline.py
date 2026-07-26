from __future__ import annotations

import os
import sys
import json
import math
from pathlib import Path
from itertools import combinations
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from sklearn.metrics import roc_auc_score, average_precision_score, roc_curve
import random

# Global Seeding for Strict Reproducibility
DEFAULT_SEED = 42
np.random.seed(DEFAULT_SEED)
random.seed(DEFAULT_SEED)

# Import from our consolidated library
from curvature_lib import (
    load_config, load_models, load_crispr, load_mutation_subset,
    mutation_binary, build_gene_dictionary, compute_essentiality_baseline,
    classify_pan_essential, build_analysis_cohort, split_cohorts_by_lineage,
    save_parquet, write_markdown, load_corum, build_corum_hyperedges,
    compute_hfrc, compute_hlrc, project_to_graph, build_hypergraph_stats,
    compute_mutation_specific_dependencies, build_standard_topologies,
    bh_qvalues, holm_adjusted_pvalues, parse_gene_column, mutation_gene_columns,
    bipartite_degree_preserving_shuffle, matched_null_samples, summarize_nulls,
    welch_delta_p, run_survival_bridge, strip_gene, save_csv, assert_schema, run_smoke_test,
    build_maximal_clique_hyperedges, setup_logging,
    load_project_score_matrix, build_matched_sanger_mutation_lookup,
    validate_family_set
)


ROOT = Path(__file__).resolve().parent
logger = setup_logging("curvature_pipeline", ROOT / "logs")

def phase_0_preflight(config, root):
    logger.info("--- Phase 0: Preflight Checks ---")
    required_paths = [
        config["depmap_model_path"],
        config["depmap_crispr_path"],
        config["depmap_mutation_damaging_path"],
        config["depmap_mutation_hotspot_path"],
        config["corum_path"],
        config["trrust_path"],
        config["string_alias_path"],
        config["string_links_path"]
    ]
    missing = [p for p in required_paths if not (root / p).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required data files: {missing}")
    
    # Ensure directories exist
    for d in ["data_processed", "results/tables", "results/reports", "results/figures"]:
        os.makedirs(root / d, exist_ok=True)
    
    logger.info("Preflight complete. All required files found.")

def phase_1_first_pass(config, root):
    logger.info("--- Phase 1: First Pass & Data Audit ---")
    models = load_models(root / config["depmap_model_path"])
    crispr = load_crispr(root / config["depmap_crispr_path"])
    crispr_cols = [col for col in crispr.columns if col != "ModelID"]

    corum = load_corum(root / config["corum_path"])
    edges, incidence, corum_summary = build_corum_hyperedges(
        corum=corum,
        allowed_genes=[c.split(" (")[0] if " (" in c else c for c in crispr_cols],
        min_size=config["corum_min_size"],
        max_size=config["corum_max_size"],
    )
    hypergraph_genes = sorted(incidence["gene_symbol"].unique().tolist()) if not incidence.empty else []

    damaging = load_mutation_subset(root / config["depmap_mutation_damaging_path"], selected_genes=hypergraph_genes)
    hotspot = load_mutation_subset(root / config["depmap_mutation_hotspot_path"], selected_genes=hypergraph_genes)
    damaging_binary = mutation_binary(damaging)
    hotspot_binary = mutation_binary(hotspot)

    mutation_cols = sorted(set(mutation_gene_columns(damaging)) | set(mutation_gene_columns(hotspot)))
    gene_dict = build_gene_dictionary(crispr_cols, mutation_cols)
    save_parquet(gene_dict, root / "data_processed/gene_dictionary.parquet")

    baseline = compute_essentiality_baseline(crispr, config["essentiality_threshold"])
    pan_essential = classify_pan_essential(baseline, config, random_state=config["random_seed"])
    
    cohort = build_analysis_cohort(models, crispr, damaging, hotspot)
    discovery, validation, lineages = split_cohorts_by_lineage(cohort, config["discovery_lineage_min_models"])

    save_parquet(models, root / "data_processed/models.parquet")
    save_parquet(crispr, root / "data_processed/crispr_gene_effect.parquet")
    save_parquet(damaging_binary, root / "data_processed/mutations_damaging_binary.parquet")
    save_parquet(hotspot_binary, root / "data_processed/mutations_hotspot_binary.parquet")
    save_parquet(discovery, root / "data_processed/discovery_models.parquet")
    save_parquet(validation, root / "data_processed/validation_models.parquet")
    save_parquet(edges, root / "data_processed/hypergraph_corum_edges.parquet")
    save_parquet(incidence, root / "data_processed/hypergraph_corum_incidence.parquet")
    save_parquet(baseline, root / "data_processed/gene_essentiality_baseline.parquet")
    save_parquet(pan_essential, root / "data_processed/pan_essential_genes.parquet")

    # Curvature for CORUM
    stats_obj = build_hypergraph_stats(incidence, include_neighbors=True)
    hfrc = compute_hfrc(edges, incidence, stats=stats_obj)
    hlrc = compute_hlrc(edges, incidence, stats=stats_obj)
    curvature = hfrc.merge(hlrc, on="hyperedge_id", how="left")
    curvature = curvature.merge(edges[["hyperedge_id", "complex_id", "complex_name", "size"]], on="hyperedge_id", how="left")
    assert_schema(curvature, ["hyperedge_id", "hfrc", "hlrc", "size"], "CORUM curvature")
    save_parquet(curvature, root / "data_processed/hyperedge_curvature_corum.parquet")
    logger.info("Phase 1 complete.")

def phase_2_topology_build(config, root):
    logger.info("--- Phase 2: Building External Topologies ---")
    gene_dict = pd.read_parquet(root / "data_processed/gene_dictionary.parquet")
    allowed_genes = set(gene_dict["gene_symbol"].unique())
    topos = build_standard_topologies(config, root, allowed_genes)
    for name, data in topos.items():
        if name == "string":
            e, i, c, g = data
            save_parquet(e, root / f"data_processed/hypergraph_{name}_clique_edges.parquet")
            save_parquet(i, root / f"data_processed/hypergraph_{name}_clique_incidence.parquet")
            save_parquet(c, root / f"data_processed/hyperedge_curvature_{name}.parquet")
            save_parquet(g, root / f"data_processed/string_gene_graph.parquet")
        else:
            e, i, c = data
            save_parquet(e, root / f"data_processed/hypergraph_{name}_regulon_edges.parquet")
            save_parquet(i, root / f"data_processed/hypergraph_{name}_regulon_incidence.parquet")
            save_parquet(c, root / f"data_processed/hyperedge_curvature_{name}.parquet")
            
    # Topology Size Distribution Logging
    import json
    dist_output = {}
    corum_edges_path = root / "data_processed/hypergraph_corum_edges.parquet"
    corum_edges = pd.read_parquet(corum_edges_path) if corum_edges_path.exists() else None
    
    topo_dfs = {"corum": corum_edges}
    if "string" in topos: topo_dfs["string"] = topos["string"][0]
    if "trrust" in topos: topo_dfs["trrust"] = topos["trrust"][0]
    
    for t_name, df_edges in topo_dfs.items():
        if df_edges is not None and not df_edges.empty and "size" in df_edges.columns:
            sizes = df_edges["size"].dropna().values
            if len(sizes) > 0:
                dist_output[t_name] = {
                    "mean": float(np.mean(sizes)),
                    "median": float(np.median(sizes)),
                    "max": int(np.max(sizes)),
                    "min": int(np.min(sizes)),
                    "skew": float(pd.Series(sizes).skew()),
                    "raw_sizes": [int(x) for x in sizes]
                }
    
    out_path = root / "results/tables/hyperedge_size_distributions.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(dist_output, f)
        
    logger.info("Phase 2 complete.")

def phase_3_systematic_discovery(config, root):
    logger.info("--- Phase 3: Systematic Discovery ---")
    discovery_models = pd.read_parquet(root / "data_processed/discovery_models.parquet")
    validation_models = pd.read_parquet(root / "data_processed/validation_models.parquet")
    crispr = pd.read_parquet(root / "data_processed/crispr_gene_effect.parquet")
    damaging = pd.read_parquet(root / "data_processed/mutations_damaging_binary.parquet")
    hotspot = pd.read_parquet(root / "data_processed/mutations_hotspot_binary.parquet")
    
    # Load pan-essential genes to exclude
    pan_ess = pd.read_parquet(root / "data_processed/pan_essential_genes.parquet")
    pan_essential_set = set(pan_ess[pan_ess["is_pan_essential"] == True]["gene_symbol"])
    logger.info(f"  - Filtering {len(pan_essential_set)} pan-essential genes from partners.")

    # Discovery loop
    topologies = ["corum", "string", "trrust"]
    all_discovery = []
    all_validation = []
    
    for topo in topologies:
        inc_path = root / f"data_processed/hypergraph_{topo if topo == 'corum' else topo + ('_clique' if topo == 'string' else '_regulon')}_incidence.parquet"
        if not inc_path.exists(): continue
        inc = pd.read_parquet(inc_path)
        hypergraph_genes = sorted(inc["gene_symbol"].unique())
        
        # Efficient partner lookup
        edge_to_genes = inc.groupby("hyperedge_id")["gene_symbol"].apply(set).to_dict()
        gene_partners = defaultdict(set)
        for gene, edges in inc.groupby("gene_symbol")["hyperedge_id"]:
            for edge in edges:
                gene_partners[gene].update(edge_to_genes[edge])
            gene_partners[gene].discard(gene)
            # Pan-essential filter
            gene_partners[gene] = gene_partners[gene] - pan_essential_set
        
        # Discovery cohort
        _, dep = compute_mutation_specific_dependencies(hypergraph_genes, gene_partners, crispr, hotspot, damaging, discovery_models, config)
        if not dep.empty:
            dep["topology"] = topo
            all_discovery.append(dep)
            
        # Validation cohort (held out)
        _, v_dep = compute_mutation_specific_dependencies(hypergraph_genes, gene_partners, crispr, hotspot, damaging, validation_models, config)
        if not v_dep.empty:
            v_dep["topology"] = topo
            all_validation.append(v_dep)
            
    if all_discovery:
        disc_df = pd.concat(all_discovery, ignore_index=True)
        disc_df["undirected_key"] = disc_df.apply(lambda x: ":".join(sorted([x["mutation_gene"], x["partner_gene"]])), axis=1)
        save_parquet(disc_df, root / "results/tables/all_systematic_discovery_pairs.parquet")
        
    if all_validation:
        val_df = pd.concat(all_validation, ignore_index=True)
        val_df["undirected_key"] = val_df.apply(lambda x: ":".join(sorted([x["mutation_gene"], x["partner_gene"]])), axis=1)
        # Mark nominal validation
        # We explicitly use nominal p < 0.05 without multiplicity correction here because 
        # this is a directional confirmation of pre-specified pairs discovered in the 
        # previous cohort (not de novo systematic discovery).
        val_df["passes_validation_nominal"] = (val_df["p_value"] < 0.05) & (val_df["delta_dependency"] < 0)
        save_parquet(val_df, root / "results/tables/all_discovery_validation_heldout.parquet")
        
    logger.info("Phase 3 complete.")

def phase_4_topology_replication(config, root):
    logger.info("--- Phase 4: Topology Replication Evaluation ---")
    discovery = pd.read_parquet(root / "results/tables/all_systematic_discovery_pairs.parquet")
    candidates = discovery[discovery["passes_main_thresholds"]].copy()
    save_parquet(candidates, root / "results/tables/candidate_dependency_pairs.parquet")
    
    val_path = root / "results/tables/all_discovery_validation_heldout.parquet"
    validated_keys = set()
    if val_path.exists():
        v = pd.read_parquet(val_path)
        v = v[v["passes_validation_nominal"]]
        validated_keys = set(v["undirected_key"])
    
    essentiality = pd.read_parquet(root / "data_processed/gene_essentiality_baseline.parquet").set_index("gene_symbol")["mean_gene_effect"].to_dict()

    topologies = ["corum", "string", "trrust"]
    for topo in topologies:
        inc_path = root / f"data_processed/hypergraph_{topo if topo == 'corum' else topo + ('_clique' if topo == 'string' else '_regulon')}_incidence.parquet"
        curv_path = root / f"data_processed/hyperedge_curvature_{topo}.parquet"
        if not inc_path.exists() or not curv_path.exists(): continue
        
        inc, curv = pd.read_parquet(inc_path), pd.read_parquet(curv_path)
        if not curv.empty:
            curv = curv.drop_duplicates(subset=["hyperedge_id"])
        curv_lookup = curv.set_index("hyperedge_id").to_dict("index")
        node_degree = inc.groupby("gene_symbol")["hyperedge_id"].nunique().to_dict()
        
        pair_rows = []
        for eid, group in inc.groupby("hyperedge_id"):
            genes = sorted(group["gene_symbol"].unique())
            if len(genes) < 2 or eid not in curv_lookup: continue
            m = curv_lookup[eid]
            for a, b in combinations(genes, 2):
                pair_rows.append({
                    "pair_key": ":".join(sorted([a, b])), "hfrc": m.get("hfrc", np.nan), "hlrc": m.get("hlrc", np.nan),
                    "size": m.get("size", len(genes)), "mean_nd": m.get("mean_node_degree", np.nan),
                    "ess": np.mean([essentiality.get(a, np.nan), essentiality.get(b, np.nan)]),
                    "max_nd": max(node_degree.get(a, 0), node_degree.get(b, 0))
                })
        
        if not pair_rows: continue
        pair_df = pd.DataFrame(pair_rows).sort_values(["pair_key", "hlrc"])
        pdf = pair_df.groupby("pair_key").agg({
            "hfrc": ["min", "median", "mean"], "hlrc": ["min", "median", "mean"],
            "size": ["mean", "first"], "mean_nd": "mean", "ess": "mean", "max_nd": "max",
            "pair_key": "size"
        })
        pdf.columns = [c[0] if c[1] == "" else "_".join(c) for c in pdf.columns]
        pdf = pdf.reset_index().rename(columns={"hfrc_min": "min_hfrc", "hfrc_median": "median_hfrc", "hfrc_mean": "mean_hfrc", "hlrc_min": "min_hlrc", "hlrc_median": "median_hlrc", "hlrc_mean": "mean_hlrc", "size_mean": "mean_hyperedge_size", "size_first": "min_hlrc_hyperedge_size", "mean_nd_mean": "mean_edge_node_degree", "ess_mean": "mean_pair_essentiality", "max_nd_max": "pair_max_node_degree", "pair_key_size": "pair_hyperedge_count"})
        
        pdf["is_systematic_candidate"] = pdf["pair_key"].isin(set(candidates["undirected_key"])).astype(int)
        pdf["is_validated_candidate"] = pdf["pair_key"].isin(validated_keys).astype(int)
        pdf["log_pair_hyperedge_count"] = np.log1p(pdf["pair_hyperedge_count"])
        pdf["log_pair_max_node_degree"] = np.log1p(pdf["pair_max_node_degree"])
        pdf["log_mean_edge_node_degree"] = np.log1p(pdf["mean_edge_node_degree"])
        pdf["log_mean_hyperedge_size"] = np.log1p(pdf["mean_hyperedge_size"])
        
        assert_schema(pdf, ["pair_key", "min_hlrc", "log_pair_hyperedge_count", "log_pair_max_node_degree", "log_mean_edge_node_degree", "mean_pair_essentiality", "log_mean_hyperedge_size"], f"{topo} pair summary")
        save_parquet(pdf, root / f"results/tables/{topo}_family_pair_summary.parquet")

    logger.info("Phase 4 complete.")

def phase_5_cross_topology_audit(config, root):
    logger.info("--- Phase 5: Phase 13 Cross-Topology Audit ---")
    discovery_path = root / "results/tables/all_systematic_discovery_pairs.parquet"
    if not discovery_path.exists():
        logger.info("  - Error: Systematic discovery results missing. Skipping audit.")
        return

    discovery = pd.read_parquet(discovery_path)
    fdr = discovery[(discovery["fdr"] <= config["dependency_fdr_threshold"]) & (discovery["delta_dependency"] <= config["dependency_effect_threshold"])].copy()
    
    # Rigorous check for discovery results
    run_smoke_test(fdr, "Threshold-passing discovery pairs", min_rows=1)

    cor = set(fdr.loc[fdr["topology"] == "corum", "undirected_key"])
    string = set(fdr.loc[fdr["topology"] == "string", "undirected_key"])
    overlap_keys = sorted(cor & string)
    
    corum_sum_path = root / "results/tables/corum_family_pair_summary.parquet"
    string_sum_path = root / "results/tables/string_family_pair_summary.parquet"
    
    if not corum_sum_path.exists() or not string_sum_path.exists():
        raise FileNotFoundError(f"CRITICAL ERROR: Summary tables missing ({'corum' if not corum_sum_path.exists() else ''} {'string' if not string_sum_path.exists() else ''}).")

    corum_summary = pd.read_parquet(corum_sum_path)
    string_summary = pd.read_parquet(string_sum_path)
    
    overlap_rows = []
    for key in overlap_keys:
        ga, gb = key.split(":")
        c_subset = fdr[(fdr["topology"] == "corum") & (fdr["undirected_key"] == key)].sort_values("p_value")
        s_subset = fdr[(fdr["topology"] == "string") & (fdr["undirected_key"] == key)].sort_values("p_value")
        c_curv_sub = corum_summary[corum_summary["pair_key"] == key]
        s_curv_sub = string_summary[string_summary["pair_key"] == key]
        
        if c_subset.empty or s_subset.empty or c_curv_sub.empty or s_curv_sub.empty:
            continue
            
        c_row, s_row = c_subset.iloc[0], s_subset.iloc[0]
        c_curv, s_curv = c_curv_sub.iloc[0], s_curv_sub.iloc[0]
        
        overlap_rows.append({
            "undirected_key": key, "gene_a": ga, "gene_b": gb,
            "mutation_gene": c_row["mutation_gene"], "partner_gene": c_row["partner_gene"],
            "corum_mutation_type": c_row["mutation_type"], "string_mutation_type": s_row["mutation_type"],
            "corum_delta_dependency": c_row["delta_dependency"], "string_delta_dependency": s_row["delta_dependency"],
            "corum_min_hlrc": c_curv["min_hlrc"], "string_min_hlrc": s_curv["min_hlrc"]
        })
    
    overlap_df = pd.DataFrame(overlap_rows)
    # Ensure results are valid before saving
    run_smoke_test(overlap_df, "Overlap families", min_rows=1)
    
    save_parquet(overlap_df, root / "results/tables/phase13_cross_topology_families.parquet")
    logger.info(f"Phase 5 complete. Found {len(overlap_df)} cross-topology overlap families.")

def phase_6_tight_null_framework(config, root):
    logger.info("--- Phase 6: Tight Null Framework & Defensive Ablations ---")
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(config["random_seed"])
    
    overlap_path = root / "results/tables/phase13_cross_topology_families.parquet"
    if not overlap_path.exists():
        logger.info("  - Error: Overlap families missing. Skipping null framework.")
        return
        
    overlap_df = pd.read_parquet(overlap_path)
    if overlap_df.empty:
        logger.info("  - Warning: No overlap families to test. Skipping.")
        return

    string_summary = pd.read_parquet(root / "results/tables/string_family_pair_summary.parquet")
    string_summary["is_overlap_family"] = string_summary["pair_key"].isin(set(overlap_df["undirected_key"])).astype(int)
    
    obs_val = overlap_df["string_min_hlrc"].mean()
    obs_count = len(overlap_df)
    null_results = []
    
    # Feature-Matched KDTree (Primary + Multiple Testing + Jackknife)
    features = ["log_pair_hyperedge_count", "log_pair_max_node_degree", "log_mean_edge_node_degree", "mean_pair_essentiality", "log_mean_hyperedge_size"]
    logger.info(f"  - Null 1: Feature-Matched KDTree Multiple Testing (N=1000 base, adaptive up to 10000)...")
    
    # Multiple Testing across all 6 geometric metrics
    geometric_metrics = ["min_hlrc", "median_hlrc", "mean_hlrc", "min_hfrc", "median_hfrc", "mean_hfrc"]
    p_values_for_correction = []
    
    # fix: Initialize primary-metric placeholders to prevent NameError
    nulls_dm = pd.DataFrame()
    summ_dm = pd.DataFrame()
    
    for metric in geometric_metrics:
        logger.info(f"    - Testing metric: {metric}...")
        nulls_m = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=1000, max_iterations=10000, metric=metric, features=features)
        
        if not nulls_m.empty:
            summ_m = summarize_nulls(nulls_m)
            is_primary = (metric == "min_hlrc")
            
            # fix: Capture data if this is the primary metric (min_hlrc)
            if is_primary:
                nulls_dm = nulls_m
                summ_dm = summ_m
                
            res_dict = {
                **summ_m.iloc[0].to_dict(), 
                "null_type": "feature_matched", 
                "description": f"Matched on {', '.join(features)}", 
                "frozen_primary": is_primary
            }
            null_results.append(res_dict)
            p_values_for_correction.append(res_dict["empirical_p_less"])

    # Apply Hierarchical Testing Procedure
    primary_pval = None
    secondary_pvals = []
    secondary_indices = []
    
    for idx, (m, p_val) in enumerate(zip(geometric_metrics, p_values_for_correction)):
        null_results[idx]["testing_tier"] = "primary" if m == "min_hlrc" else "secondary"
        if m == "min_hlrc":
            primary_pval = p_val
            null_results[idx]["holm_adjusted_p"] = p_val # Unpenalized
            null_results[idx]["hierarchical_reject"] = bool(p_val < 0.05)
        else:
            secondary_pvals.append(p_val)
            secondary_indices.append(idx)
            
    primary_rejected = bool(primary_pval is not None and primary_pval < 0.05)
    
    if primary_rejected and secondary_pvals:
        adj_pvals = holm_adjusted_pvalues(secondary_pvals)
        for idx, adj_p in zip(secondary_indices, adj_pvals):
            null_results[idx]["holm_adjusted_p"] = float(adj_p)
            null_results[idx]["hierarchical_reject"] = bool(adj_p < 0.05)
    else:
        for idx in secondary_indices:
            null_results[idx]["holm_adjusted_p"] = np.nan
            null_results[idx]["hierarchical_reject"] = False

    logger.info(f"    - Primary Endpoint (min_hlrc) P-value: {primary_pval}")
    if primary_rejected:
        secondary_metrics_str = {geometric_metrics[i]: null_results[i]["holm_adjusted_p"] for i in secondary_indices}
        logger.info(f"    - Secondary Exploratory Metrics (Holm-Adjusted P-values): {secondary_metrics_str}")
    else:
        logger.info(f"    - Primary endpoint did not reject. Secondary metrics skipped in hierarchy.")

    # Jackknife / Leave-One-Family-Out (LOFO) Analysis for min_hlrc
    logger.info("  - Null 1b: Running Jackknife / LOFO analysis on min_hlrc to assess fragility...")
    overlap_keys = overlap_df["undirected_key"].tolist()
    lofo_results = []
    
    for loo_key in overlap_keys:
        logger.info(f"    - LOFO: Dropping {loo_key}...")
        loo_keys = [k for k in overlap_keys if k != loo_key]
        
        # Explicitly remove the dropped family from the frame entirely to prevent any null pool leakage
        loo_frame = string_summary[string_summary["pair_key"] != loo_key].copy()
        loo_frame["is_overlap_family_loo"] = loo_frame["pair_key"].isin(loo_keys).astype(int)
        
        nulls_loo = matched_null_samples(loo_frame, "is_overlap_family_loo", rng, iterations=1000, max_iterations=10000, metric="min_hlrc", features=features)
        
        if not nulls_loo.empty:
            summ_loo = summarize_nulls(nulls_loo)
            lofo_results.append({
                "omitted_family": loo_key,
                "n_remaining": len(loo_keys),
                "empirical_p_less": summ_loo.iloc[0]["empirical_p_less"],
                "observed_value": summ_loo.iloc[0]["observed_value"]
            })
            
    lofo_df = pd.DataFrame(lofo_results)
    save_parquet(lofo_df, root / "results/tables/tight_null_lofo_fragility.parquet")
    
    if not lofo_df.empty:
        max_p = lofo_df["empirical_p_less"].max()
        min_p = lofo_df["empirical_p_less"].min()
        logger.info(f"    - LOFO P-value range: {min_p:.4f} to {max_p:.4f}")

    # Simple Random Matching (Baseline)
    logger.info("  - Null 2: Simple Random Matching (No features)...")
    random_samples = [string_summary[string_summary["is_overlap_family"] == 0].sample(obs_count, replace=True, random_state=rng.integers(0, 1e9))["min_hlrc"].mean() for _ in range(1000)]
    p_rand = (sum(np.array(random_samples) <= obs_val) + 1) / (1000 + 1)
    null_results.append({
        "metric": "min_hlrc", "observed_count": obs_count, "observed_value": obs_val, 
        "null_mean": np.mean(random_samples), 
        "iter_null_std": np.std(random_samples),
        "iter_null_min": np.min(random_samples),
        "iter_null_max": np.max(random_samples),
        "empirical_p_less": p_rand, "n_permutations": 1000,
        "null_type": "random_matching", "description": "Uniform random sampling from background"
    })

    # Ablation: vs. Hyperedge Size Alone
    logger.info("  - Null 3: Ablation vs. Hyperedge Size...")
    nulls_size = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=500, metric="mean_hyperedge_size", features=features)
    if not nulls_size.empty:
        summ_size = summarize_nulls(nulls_size)
        null_results.append({**summ_size.iloc[0].to_dict(), "null_type": "ablation_size", "description": "Testing if size alone explains overlap", "frozen_primary": False})

    # Ablation: vs. Node Degree Alone
    logger.info("  - Null 4: Ablation vs. Max Node Degree...")
    nulls_deg = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=500, metric="pair_max_node_degree", features=features)
    if not nulls_deg.empty:
        summ_deg = summarize_nulls(nulls_deg)
        null_results.append({**summ_deg.iloc[0].to_dict(), "null_type": "ablation_degree", "description": "Testing if degree alone explains overlap", "frozen_primary": False})

    # Feature Ablations (dropping one feature at a time)
    logger.info("  - Null 5: Feature Ablations...")
    for feat in features:
        logger.info(f"    - Dropping {feat}...")
        nulls_ab = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=500, metric="min_hlrc", features=[f for f in features if f != feat])
        if not nulls_ab.empty:
            summ_ab = summarize_nulls(nulls_ab)
            null_results.append({**summ_ab.iloc[0].to_dict(), "null_type": f"ablation_drop_{feat}", "description": f"Dropped {feat} from matching", "frozen_primary": False})

    # Bipartite Topology Control (Shuffle)
    logger.info("  - Null 6: Bipartite Topology Control (Shuffle)...")
    inc_string_path = root / "data_processed/hypergraph_string_clique_incidence.parquet"
    edges_string_path = root / "data_processed/hypergraph_string_clique_edges.parquet"
    if inc_string_path.exists() and edges_string_path.exists():
        inc_real = pd.read_parquet(inc_string_path)
        edges_real = pd.read_parquet(edges_string_path)
        
        # Perform Bipartite Shuffle
        inc_shuffled = bipartite_degree_preserving_shuffle(inc_real, rng, swaps_multiplier=10)
        shuff_stats = build_hypergraph_stats(inc_shuffled, include_neighbors=True)
        shuff_curv = compute_hlrc(edges_real, inc_shuffled, stats=shuff_stats)
        
        # Map shuffled curvature back to pairs
        shuff_pair_rows = []
        edge_to_nodes_shuff = inc_shuffled.groupby("hyperedge_id")["gene_symbol"].apply(list).to_dict()
        curv_lookup_shuff = shuff_curv.set_index("hyperedge_id")["hlrc"].to_dict()
        for eid, nodes in edge_to_nodes_shuff.items():
            if eid not in curv_lookup_shuff: continue
            val = curv_lookup_shuff[eid]
            for a, b in combinations(sorted(nodes), 2):
                shuff_pair_rows.append({"pair_key": ":".join([a, b]), "hlrc": val})
        
        shuff_pdf = pd.DataFrame(shuff_pair_rows).groupby("pair_key")["hlrc"].min().reset_index(name="min_hlrc_shuffled")
        overlap_keys = set(overlap_df["undirected_key"])
        surviving_shuff = shuff_pdf[shuff_pdf["pair_key"].isin(overlap_keys)]
        
        num_overlap = len(overlap_keys)
        num_surviving = len(surviving_shuff)
        num_missing = num_overlap - num_surviving
        
        shuff_sum = surviving_shuff["min_hlrc_shuffled"].sum() if num_surviving > 0 else 0.0
        shuff_val = (shuff_sum + (num_missing * 1.0)) / num_overlap if num_overlap > 0 else np.nan
        
        null_results.append({
            "metric": "min_hlrc", "observed_count": obs_count, "observed_value": obs_val,
            "null_mean": shuff_val, 
            "iter_null_std": 0.0,
            "iter_null_min": shuff_val,
            "iter_null_max": shuff_val,
            "empirical_p_less": np.nan, "n_permutations": 1,
            "null_type": "bipartite_shuffle", "description": "Single-instance bipartite degree-preserving shuffle", "frozen_primary": False
        })

    summary_df = pd.DataFrame(null_results)
    save_parquet(summary_df, root / "results/tables/tight_null_framework_summary.parquet")
    
    # Calibration Plot
    if not nulls_dm.empty:
        logger.info("  - Generating Null Calibration Plot...")
        plt.figure(figsize=(8, 6))
        plt.hist(nulls_dm["iter_null_value"], bins=30, alpha=0.5, label="Feature-Matched Nulls", color="gray")
        plt.axvline(obs_val, color="red", linestyle="--", label=f"Observed Overlap (p={summ_dm['empirical_p_less'].iloc[0]:.4f})")
        plt.xlabel("Mean min_HLRC")
        plt.ylabel("Frequency")
        plt.title("Null Calibration: Overlap vs. Feature-Matched Background")
        plt.legend()
        plt.tight_layout()
        plt.savefig(root / "results/figures/null_calibration_hlrc.png")
        plt.close()

    if not summary_df.empty and "frozen_primary" in summary_df.columns:
        primary = summary_df[summary_df["frozen_primary"] == True]
        if not primary.empty:
            logger.info(f"Phase 6 complete. Primary Endpoint (FM) P = {primary['empirical_p_less'].iloc[0]:.5f}")
            
def phase_7_sensitivity_backbone(config, root):
    logger.info("--- Phase 7: Sensitivity Analysis (Backbone On) ---")
    overlap_df = pd.read_parquet(root / "results/tables/phase13_cross_topology_families.parquet")
    overlap_keys = set(overlap_df["undirected_key"])
    
    # STRING backbone sensitivity
    string_graph_path = root / "data_processed/string_gene_graph.parquet"
    if not string_graph_path.exists():
        logger.info("  - Warning: string_gene_graph.parquet missing.")
        return
        
    s_graph = pd.read_parquet(string_graph_path)
    # Build hypergraph WITH backbone
    e, i, _, _ = build_maximal_clique_hyperedges(s_graph, include_backbone=True, prefix="STRING_SENS")
    stats = build_hypergraph_stats(i, include_neighbors=True)
    curv = compute_hlrc(e, i, stats)
    
    # Pair summary (deduplicated)
    pair_rows = []
    edge_to_nodes = i.groupby("hyperedge_id")["gene_symbol"].apply(list).to_dict()
    curv_lookup = curv.set_index("hyperedge_id")["hlrc"].to_dict()
    
    for eid, nodes in edge_to_nodes.items():
        if eid not in curv_lookup: continue
        val = curv_lookup[eid]
        for a, b in combinations(sorted(nodes), 2):
            pair_rows.append({"pair_key": ":".join([a, b]), "hlrc": val})
            
    pdf = pd.DataFrame(pair_rows).groupby("pair_key")["hlrc"].min().reset_index(name="min_hlrc_backbone")
    pdf["is_overlap_family"] = pdf["pair_key"].isin(overlap_keys).astype(int)
    
    obs_mean = pdf[pdf["is_overlap_family"] == 1]["min_hlrc_backbone"].mean()
    bg_mean = pdf[pdf["is_overlap_family"] == 0]["min_hlrc_backbone"].mean()
    
    res = {"topology": "STRING", "backbone": "ON", "overlap_mean_hlrc": obs_mean, "background_mean_hlrc": bg_mean, "delta": obs_mean - bg_mean}
    save_parquet(pd.DataFrame([res]), root / "results/tables/sensitivity_backbone_on_summary.parquet")
    logger.info(f"  - Sensitivity (Backbone ON) Mean HLRC: Overlap={obs_mean:.3f}, Background={bg_mean:.3f}")
    logger.info("Phase 7 complete.")

def phase_8_tiered_validation(config, root):
    logger.info("--- Phase 8: Tiered Validation Layers (Patient & Pharmacologic) ---")
    logger.info("    - Calculating TMB, Driver Co-occurrences, and cleaning clinical covariates...")
    
        # Patient Survival Validation (TCGA Bridge) (1)
    tcga_path = root / "data_processed/tcga_clinical_core.parquet"
    if tcga_path.exists():
        logger.info("\n  - Tier 1: Executing TCGA Survival Cox PH Hazards Bridge.")
        tcga_df = pd.read_parquet(tcga_path)
        overlap_path = root / "results/tables/phase13_cross_topology_families.parquet"
        if overlap_path.exists():
            overlap_df = pd.read_parquet(overlap_path)

            survival_results = []
            schoenfeld_results = []
            target_histologies = ("LUAD", "BRCA")

            for family in overlap_df["undirected_key"]:
                g1, g2 = family.split(":")

                if f"{g1}_mutation" in tcga_df.columns:
                    mutation_gene, partner_gene = g1, g2
                elif f"{g2}_mutation" in tcga_df.columns:
                    mutation_gene, partner_gene = g2, g1
                else:
                    continue

                for histology in target_histologies:
                    cdr, ph_diag = run_survival_bridge(
                        tcga_df,
                        mutation_gene=mutation_gene,
                        partner_gene=partner_gene,
                        histology_value=histology,
                    )
                    if not cdr.empty:
                        survival_results.append(cdr)
                    if not ph_diag.empty:
                        schoenfeld_results.append(ph_diag)

            if survival_results:
                sdf = pd.concat(survival_results, ignore_index=True)
                save_parquet(sdf, root / "results/tables/tcga_survival_validation.parquet")
                n_sig = int((sdf["p_value"] < 0.05).sum())
                logger.info(f"    - TCGA bridge complete ({n_sig} nominally significant survival associations found).")
            else:
                logger.info("    - No valid LUAD/BRCA survival fits were produced.")

            if schoenfeld_results:
                ph_df = pd.concat(schoenfeld_results, ignore_index=True)
                save_parquet(ph_df, root / "results/tables/tcga_schoenfeld_diagnostics.parquet")
                flagged = ph_df[ph_df["ph_flag"] == True]["histology"].nunique()
                logger.info(f"    - Schoenfeld diagnostics saved; PH flags observed in {flagged} cohort(s).")
            else:
                logger.info("    - No Schoenfeld diagnostics were generated.")
    else:
        logger.info("\n  - TCGA clinical data missing. Skipping Tier 1.")

    # Sanger Validation Bridge (2)
    sanger_ext_path = root / "data_external/cmp/project_score_v2/Project_score_combined_Sanger_v2_Broad_21Q2_fitness_scores_scaled_bayesian_factors_20250624.tsv"
    sanger_mut_path = root / "data/cell model passports/mutations_all_20260316.csv"
    sanger_map_path = root / "data/cell model passports/model_list_20260323.csv"
    if all(p.exists() for p in [sanger_ext_path, sanger_mut_path, sanger_map_path]):
        logger.info("\n  - Tier 2: Validating via Independent Sanger/COSMIC Cohorts...")
        overlap_path = root / "results/tables/phase13_cross_topology_families.parquet"
        disc_path = root / "results/tables/all_systematic_discovery_pairs.parquet"
        if overlap_path.exists() and disc_path.exists():
            overlap_df_t2 = pd.read_parquet(overlap_path)
            discovery_t2 = pd.read_parquet(disc_path)
            families = []
            for _, row in overlap_df_t2.iterrows():
                matches = discovery_t2[discovery_t2["undirected_key"] == row["undirected_key"]].sort_values("p_value")
                if matches.empty: continue
                best = matches.iloc[0]
                families.append({**row.to_dict(), "delta_dependency": best["delta_dependency"], "mutation_type": best["mutation_type"]})
            if families:
                families_df = pd.DataFrame(families)
                models_t2 = pd.read_parquet(root / "data_processed/models.parquet")[["ModelID", "SangerModelID"]].dropna()
                mutation_lookup = build_matched_sanger_mutation_lookup(
                    sanger_mut_path, sanger_map_path,
                    hotspot_min_models=config.get("mutation_min_mutant_models", 5)
                )
                mutation_lookup = {k: v.rename(columns=lambda c: strip_gene(c)) for k, v in mutation_lookup.items()}
                external = load_project_score_matrix(sanger_ext_path, source_filter="sanger").merge(models_t2, on="SangerModelID", how="inner")
                result_df = validate_family_set(families_df, external, mutation_lookup)
                save_parquet(result_df, root / "results/tables/sanger_cohort_validation.parquet")
                n_testable = result_df["external_gene_available"].sum() if "external_gene_available" in result_df.columns else len(result_df)
                n_concordant = result_df["same_direction_as_discovery"].sum() if "same_direction_as_discovery" in result_df.columns else 0
                logger.info(f"    - Sanger replication complete ({n_concordant}/{n_testable} concordant pairs).")
            else:
                logger.info("    - No testable families for Sanger validation.")
    else:
        logger.info("\n  - Sanger validation data missing. Skipping Tier 2.")

    # Pharmacologic Validation via PRISM (3)
    prism_resp_path = root / "data/depmap/PRISM_repurposing_secondary/secondary-screen-dose-response-curve-parameters.csv"
    braf_path = root / "data_processed/mutations_hotspot_binary.parquet"
    if prism_resp_path.exists() and braf_path.exists():
        logger.info("\n  - Tier 3: Evaluating Pharmacologic Selectivity via PRISM...")
        resp = pd.read_csv(prism_resp_path, usecols=['depmap_id', 'name', 'target', 'auc'], low_memory=False)
        braf_mut = pd.read_parquet(braf_path).set_index("ModelID")["BRAF"]
        mek = resp[resp['target'].fillna('').str.contains('MAP2K1|MAP2K2|MEK', case=False)].copy()
        prism_rows = []
        for drug, ddf in mek.groupby('name'):
            ddf = ddf.copy()
            ddf['braf_mut'] = ddf['depmap_id'].map(braf_mut)
            ddf = ddf.dropna(subset=['braf_mut', 'auc'])
            if len(ddf) < 25: continue
            delta, p, nm, nw, se = welch_delta_p(ddf['braf_mut'].astype(bool).to_numpy(), ddf['auc'].to_numpy())
            if np.isfinite(delta):
                prism_rows.append({'drug': drug, 'target': ddf['target'].iloc[0], 'delta_auc': delta, 'p_value': p})
        if prism_rows:
            rdf = pd.DataFrame(prism_rows)
            rdf['q_value'] = bh_qvalues(rdf['p_value'])
            rdf = rdf.sort_values('p_value')
            save_parquet(rdf, root / "results/tables/prism_pharmacologic_validation.parquet")
            n_nom = int((rdf['p_value'] < 0.05).sum())
            n_fdr = int((rdf['q_value'] < 0.05).sum())
            logger.info(f"    - PRISM bridge complete ({n_nom} nominal, {n_fdr} FDR-significant).")
        else:
            logger.info("    - No PRISM drug results passed filters.")
    else:
        logger.info("\n  - PRISM data missing. Skipping Tier 3.")
        
    logger.info("\nPhase 8 complete.")

def main():
    config_path = ROOT / "configs/pipeline_config.json"
    if len(sys.argv) > 1:
        config_path = Path(sys.argv[1]).resolve()
        logger.info(f"--- Using Custom Config: {config_path} ---")
    
    config = load_config(config_path)
    
    # Re-seed everything for strict reproducibility
    seed = config.get("random_seed", DEFAULT_SEED)
    np.random.seed(seed)
    random.seed(seed)
    
    phases = [
        phase_0_preflight,
        phase_1_first_pass,
        phase_2_topology_build,
        phase_3_systematic_discovery,
        phase_4_topology_replication,
        phase_5_cross_topology_audit,
        phase_6_tight_null_framework,
        phase_7_sensitivity_backbone,
        phase_8_tiered_validation
    ]
    
    for phase in phases:
        try:
            phase(config, ROOT)
        except Exception as e:
            logger.info(f"CRITICAL FAILURE in {phase.__name__}: {e}")
            sys.exit(1)
            
    logger.info("\n--- REPRODUCIBILITY COMPLETE ---")
    logger.info("Primary Endpoint: results/tables/tight_null_framework_summary.parquet")

if __name__ == "__main__":
    main()
