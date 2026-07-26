from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd
import numpy as np
import random
from scipy import stats
from sklearn.metrics import roc_auc_score, average_precision_score

# Seeding
DEFAULT_SEED = 42
np.random.seed(DEFAULT_SEED)
random.seed(DEFAULT_SEED)

# Import from our consolidated library
from curvature_lib import (
    save_parquet, write_markdown, load_project_score_matrix, strip_gene,
    validate_family_set, build_matched_sanger_mutation_lookup,
    welch_delta_p, load_config, random_effects_meta_analysis, bh_qvalues,
    bayesian_hierarchical_model, project_to_graph, compute_projected_graph_pair_metrics,
    setup_logging
)

ROOT = Path(__file__).resolve().parent
logger = setup_logging("curvature_validation", ROOT / "logs")

def preflight_check(root):
    logger.info("--- Validation Preflight Check ---")
    required_tables = [
        "results/tables/phase13_cross_topology_families.parquet",
        "results/tables/all_systematic_discovery_pairs.parquet"
    ]
    missing = [t for t in required_tables if not (root / t).exists()]
    if missing:
        logger.info(f"ERROR: Missing required pipeline outputs. Please run curvature_pipeline.py first.")
        logger.info(f"Missing files: {missing}")
        return False
    
    # Check for external data
    external_data = {
        "Sanger": root / "data_external/cmp/project_score_v2/Project_score_combined_Sanger_v2_Broad_21Q2_fitness_scores_scaled_bayesian_factors_20250624.tsv",
        "DepMap 25Q3": root / "data/depmap/25Q3/CRISPRGeneEffect.csv"
    }
    for name, path in external_data.items():
        if not path.exists():
            logger.info(f"Warning: {name} data not found. This validation layer will be skipped.")
            
    return True

def summarize_validation(df: pd.DataFrame, context: str) -> pd.DataFrame:
    """Compute concordance and meta-analytic summary for a validation result."""
    valid = df[df["external_gene_available"]].copy()
    if valid.empty: return pd.DataFrame()
    
    # Concordance: same direction as discovery (discovery delta < 0 and external delta < 0)
    concordant = valid["same_direction_as_discovery"].sum()
    total = len(valid)
    concordance_rate = concordant / total if total > 0 else 0
    
    # Meta-analysis (Random Effects) on effect sizes
    meta_subset = valid[np.isfinite(valid["external_delta_dependency"]) & np.isfinite(valid["external_se"])]
    if not meta_subset.empty:
        effects = meta_subset["external_delta_dependency"].to_numpy()
        ses = meta_subset["external_se"].to_numpy()
        
        # Frequentist
        meta = random_effects_meta_analysis(effects, ses)
        
        # Bayesian
        bayes = bayesian_hierarchical_model(effects, ses, iterations=5000)
    else:
        meta = {"mu": np.nan, "se": np.nan, "p": np.nan, "i2": np.nan}
        bayes = {"p_negative": np.nan, "mu_mean": np.nan, "rhat_mu": np.nan}

    def _wilson_interval(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
        if n <= 0:
            return np.nan, np.nan
        phat = k / n
        denom = 1 + (z**2 / n)
        center = (phat + (z**2 / (2 * n))) / denom
        half = (z * np.sqrt((phat * (1 - phat) + (z**2 / (4 * n))) / n)) / denom
        return float(max(0.0, center - half)), float(min(1.0, center + half))

    def _wald_interval(mu: float, se: float, z: float = 1.96) -> tuple[float, float]:
        if not np.isfinite(mu) or not np.isfinite(se):
            return np.nan, np.nan
        return float(mu - z * se), float(mu + z * se)

    conc_low, conc_high = _wilson_interval(int(concordant), int(total))
    meta_low, meta_high = _wald_interval(float(meta["mu"]), float(meta["se"]))
    summary = {
        "context": context,
        "n_total_families": len(df),
        "n_testable_families": total,
        "n_concordant_families": int(concordant),
        "concordance_rate": float(concordance_rate),
        "concordance_ci_low": conc_low,
        "concordance_ci_high": conc_high,
        "n_nominally_significant": int(valid["passes_external_nominal"].sum()),
        "meta_mu": float(meta["mu"]),
        "meta_se": float(meta["se"]),
        "meta_ci_low": meta_low,
        "meta_ci_high": meta_high,
        "meta_p": float(meta["p"]),
        "meta_i2": float(meta["i2"]),
        "bayes_p_negative": float(bayes["p_negative"]),
        "bayes_mu_mean": float(bayes["mu_mean"]),
        "bayes_rhat_mu": float(bayes["rhat_mu"])
    }
    return pd.DataFrame([summary])

def _infer_log_effect_se(effect: float, p_value: float) -> float:
    if not np.isfinite(effect) or not np.isfinite(p_value) or p_value <= 0 or p_value >= 1:
        return np.nan
    z = stats.norm.isf(p_value / 2.0)
    if not np.isfinite(z) or z <= 0:
        return np.nan
    return float(abs(effect) / z)

def _wald_interval(mu: float, se: float, z: float = 1.96) -> tuple[float, float]:
    if not np.isfinite(mu) or not np.isfinite(se):
        return np.nan, np.nan
    return float(mu - z * se), float(mu + z * se)

def _summarize_random_effects(
    df: pd.DataFrame,
    *,
    effect_col: str,
    se_col: str,
    group_col: str,
    context: str,
    subgroup_col: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    work = df.copy()
    if effect_col not in work.columns or group_col not in work.columns:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    if se_col not in work.columns:
        work[se_col] = np.nan

    if "cox_p_value" in work.columns and effect_col == "log_hazard_ratio":
        missing_se = work[se_col].isna()
        if missing_se.any():
            work.loc[missing_se, se_col] = work.loc[missing_se].apply(
                lambda r: _infer_log_effect_se(r.get(effect_col, np.nan), r.get("cox_p_value", np.nan)),
                axis=1,
            )

    valid = work[np.isfinite(work[effect_col]) & np.isfinite(work[se_col])].copy()
    if valid.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    effects = valid[effect_col].to_numpy(dtype=float)
    ses = valid[se_col].to_numpy(dtype=float)
    meta = random_effects_meta_analysis(effects, ses)
    ci_low, ci_high = _wald_interval(meta["mu"], meta["se"])

    summary = pd.DataFrame([{
        "context": context,
        "endpoint_type": "continuous",
        "effect_col": effect_col,
        "se_col": se_col,
        "n_rows": int(len(valid)),
        "n_unique_groups": int(valid[group_col].nunique()),
        "meta_mu": float(meta["mu"]),
        "meta_se": float(meta["se"]),
        "meta_ci_low": ci_low,
        "meta_ci_high": ci_high,
        "meta_p": float(meta["p"]),
        "meta_i2": float(meta["i2"]),
        "meta_tau2": float(meta["tau2"]),
    }])

    loo_rows = []
    for group_value in sorted(valid[group_col].astype(str).unique()):
        subset = valid[valid[group_col].astype(str) != group_value]
        if subset.empty:
            continue
        if len(subset) < 2:
            loo_rows.append({
                "context": context,
                "omitted_group": group_value,
                "n_remaining": len(subset),
                "meta_mu": np.nan,
                "meta_se": np.nan,
                "meta_ci_low": np.nan,
                "meta_ci_high": np.nan,
                "meta_p": np.nan,
                "meta_i2": np.nan,
                "meta_tau2": np.nan,
            })
            continue
        loo_meta = random_effects_meta_analysis(subset[effect_col].to_numpy(dtype=float), subset[se_col].to_numpy(dtype=float))
        loo_low, loo_high = _wald_interval(loo_meta["mu"], loo_meta["se"])
        loo_rows.append({
            "context": context,
            "omitted_group": group_value,
            "n_remaining": int(len(subset)),
            "meta_mu": float(loo_meta["mu"]),
            "meta_se": float(loo_meta["se"]),
            "meta_ci_low": loo_low,
            "meta_ci_high": loo_high,
            "meta_p": float(loo_meta["p"]),
            "meta_i2": float(loo_meta["i2"]),
            "meta_tau2": float(loo_meta["tau2"]),
        })

    loo_df = pd.DataFrame(loo_rows)

    subgroup_df = pd.DataFrame()
    if subgroup_col and subgroup_col in valid.columns:
        subgroup_rows = []
        for subgroup_value, sub in valid.groupby(subgroup_col, dropna=False):
            if len(sub) < 2:
                continue
            sub_meta = random_effects_meta_analysis(sub[effect_col].to_numpy(dtype=float), sub[se_col].to_numpy(dtype=float))
            sub_low, sub_high = _wald_interval(sub_meta["mu"], sub_meta["se"])
            subgroup_rows.append({
                "context": context,
                "subgroup_col": subgroup_col,
                "subgroup_value": str(subgroup_value),
                "n_rows": int(len(sub)),
                "meta_mu": float(sub_meta["mu"]),
                "meta_se": float(sub_meta["se"]),
                "meta_ci_low": sub_low,
                "meta_ci_high": sub_high,
                "meta_p": float(sub_meta["p"]),
                "meta_i2": float(sub_meta["i2"]),
                "meta_tau2": float(sub_meta["tau2"]),
            })
        subgroup_df = pd.DataFrame(subgroup_rows)

    return summary, loo_df, subgroup_df

def run_sanger_validation(root, config):
    logger.info("\n--- Tier 1: Independent CRISPR Replication (Sanger) ---")
    ext_path = root / "data_external/cmp/project_score_v2/Project_score_combined_Sanger_v2_Broad_21Q2_fitness_scores_scaled_bayesian_factors_20250624.tsv"
    mutations_path = root / "data/cell model passports/mutations_all_20260316.csv"
    model_map_path = root / "data/cell model passports/model_list_20260323.csv"
    
    if not all(p.exists() for p in [ext_path, mutations_path, model_map_path]):
        logger.info("  - Skipping Sanger: required external data missing.")
        return

    overlap = pd.read_parquet(root / "results/tables/phase13_cross_topology_families.parquet")
    if overlap.empty:
        logger.info("  - Skipping Sanger: No overlap families to validate.")
        return
        
    discovery = pd.read_parquet(root / "results/tables/all_systematic_discovery_pairs.parquet")
    
    families = []
    for _, row in overlap.iterrows():
        matches = discovery[discovery["undirected_key"] == row["undirected_key"]].sort_values("p_value")
        if matches.empty: continue
        best = matches.iloc[0]
        families.append({**row.to_dict(), "delta_dependency": best["delta_dependency"], "mutation_type": best["mutation_type"]})
    
    if not families:
        logger.info("  - Skipping Sanger: No testable families found in discovery.")
        return
        
    families_df = pd.DataFrame(families)

    models = pd.read_parquet(root / "data_processed/models.parquet")[["ModelID", "SangerModelID"]].dropna()
    mutation_lookup = build_matched_sanger_mutation_lookup(
        mutations_path, 
        model_map_path, 
        hotspot_min_models=config.get("mutation_min_mutant_models", 5)
    )
    mutation_lookup = {k: v.rename(columns=lambda c: strip_gene(c)) for k, v in mutation_lookup.items()}

    external = load_project_score_matrix(ext_path, source_filter="sanger").merge(models, on="SangerModelID", how="inner")
    result_df = validate_family_set(families_df, external, mutation_lookup)
    save_parquet(result_df, root / "results/tables/phase13_external_cmp_sanger_validation.parquet")
    
    summ = summarize_validation(result_df, "Sanger")
    save_parquet(summ, root / "results/tables/phase13_external_cmp_sanger_summary.parquet")
    logger.info(f"  - Sanger complete. Concordance: {summ['n_concordant_families'].iloc[0]}/{summ['n_testable_families'].iloc[0]}, Meta-P: {summ['meta_p'].iloc[0]:.5f}, P_neg: {summ['bayes_p_negative'].iloc[0]:.4f}, R-hat: {summ['bayes_rhat_mu'].iloc[0]:.3f}")

def run_depmap25q3_validation(root, config):
    logger.info("\n--- Tier 1: Independent CRISPR Replication (DepMap 25Q3) ---")
    model_path = root / "data/depmap/25Q3/Model.csv"
    crispr_path = root / "data/depmap/25Q3/CRISPRGeneEffect.csv"
    
    if not (model_path.exists() and crispr_path.exists()):
        logger.info("  - Skipping 25Q3: required external data missing.")
        return

    overlap = pd.read_parquet(root / "results/tables/phase13_cross_topology_families.parquet")
    if overlap.empty:
        logger.info("  - Skipping 25Q3: No overlap families to validate.")
        return
        
    discovery = pd.read_parquet(root / "results/tables/all_systematic_discovery_pairs.parquet")
    
    families = []
    for _, row in overlap.iterrows():
        matches = discovery[discovery["undirected_key"] == row["undirected_key"]].sort_values("p_value")
        if matches.empty: continue
        best = matches.iloc[0]
        families.append({**row.to_dict(), "delta_dependency": best["delta_dependency"], "mutation_type": best["mutation_type"]})
    
    if not families:
        logger.info("  - Skipping 25Q3: No testable families found in discovery.")
        return
        
    families_df = pd.DataFrame(families)

    model_25q3 = pd.read_csv(model_path, usecols=["ModelID"])
    crispr_25q3 = pd.read_csv(crispr_path, low_memory=False)
    first_col = crispr_25q3.columns[0]
    crispr_25q3 = crispr_25q3.rename(columns={first_col: "ModelID", **{c: strip_gene(c) for c in crispr_25q3.columns if c != first_col}})
    crispr_25q3 = crispr_25q3[crispr_25q3["ModelID"].isin(model_25q3["ModelID"])]

    damaging = pd.read_parquet(root / "data_processed/mutations_damaging_binary.parquet")
    hotspot = pd.read_parquet(root / "data_processed/mutations_hotspot_binary.parquet")
    mutation_lookup = {"damaging": damaging, "hotspot": hotspot}

    result_df = validate_family_set(families_df, crispr_25q3, mutation_lookup)
    save_parquet(result_df, root / "results/tables/phase13_external_depmap25q3_validation.parquet")
    
    summ = summarize_validation(result_df, "DepMap 25Q3")
    save_parquet(summ, root / "results/tables/phase13_external_depmap25q3_summary.parquet")
    logger.info(f"  - 25Q3 complete. Concordance: {summ['n_concordant_families'].iloc[0]}/{summ['n_testable_families'].iloc[0]}, Meta-P: {summ['meta_p'].iloc[0]:.5f}, P_neg: {summ['bayes_p_negative'].iloc[0]:.4f}, R-hat: {summ['bayes_rhat_mu'].iloc[0]:.3f}")

def run_prism_validation(root):
    logger.info("\n--- Tier 3: Pharmacologic Bridge (PRISM) ---")
    resp_path = root / 'data/depmap/PRISM_repurposing_secondary/secondary-screen-dose-response-curve-parameters.csv'
    if not resp_path.exists():
        logger.info("  - Skipping PRISM: required data missing.")
        return
        
    resp = pd.read_csv(resp_path, usecols=['depmap_id', 'name', 'target', 'auc'], low_memory=False)
    
    # Switch to hotspot mutations for BRAF
    braf_path = root / "data_processed/mutations_hotspot_binary.parquet"
    if not braf_path.exists():
        logger.info("  - Skipping PRISM: BRAF mutation data missing.")
        return
        
    braf_mut = pd.read_parquet(braf_path).set_index("ModelID")["BRAF"]
    
    # Filter for MEK inhibitors (MAP2K1, MAP2K2, MEK)
    mek = resp[resp['target'].fillna('').str.contains('MAP2K1|MAP2K2|MEK', case=False)].copy()
    rows = []
    
    for drug, ddf in mek.groupby('name'):
        ddf['braf_mut'] = ddf['depmap_id'].map(braf_mut)
        ddf = ddf.dropna(subset=['braf_mut', 'auc'])
        if len(ddf) < 25: continue
        delta, p, nm, nw, se = welch_delta_p(ddf['braf_mut'].astype(bool).to_numpy(), ddf['auc'].to_numpy())
        if np.isfinite(delta):
            rows.append({'drug': drug, 'target': ddf['target'].iloc[0], 'delta_auc': delta, 'p_value': p})
            
    if rows:
        rdf = pd.DataFrame(rows)
        rdf['q_value'] = bh_qvalues(rdf['p_value'])
        rdf = rdf.sort_values('p_value')
        save_parquet(rdf, root / 'results/tables/phase25_prism_mek_validation.parquet')
        n_nom = (rdf['p_value'] < 0.05).sum()
        n_fdr = (rdf['q_value'] < 0.05).sum()
        logger.info(f"  - PRISM complete. Significant hits: {n_nom} nominal, {n_fdr} FDR-significant")

def run_overlap_continuous_meta_summaries(root):
    logger.info("\n--- Continuous Validation Meta-Analysis ---")
    outputs = []

    for context, path in [
        ("Sanger", root / "results/tables/phase13_external_cmp_sanger_validation.parquet"),
        ("DepMap 25Q3", root / "results/tables/phase13_external_depmap25q3_validation.parquet"),
    ]:
        if not path.exists():
            continue
        df = pd.read_parquet(path)
        summary, loo_df, _ = _summarize_random_effects(
            df,
            effect_col="external_delta_dependency",
            se_col="external_se",
            group_col="undirected_key",
            context=context,
        )
        if not summary.empty:
            outputs.append(summary.assign(source="external_validation"))
            save_parquet(summary, root / f"results/tables/{context.lower().replace(' ', '_')}_continuous_meta_summary.parquet")
        if not loo_df.empty:
            save_parquet(loo_df, root / f"results/tables/{context.lower().replace(' ', '_')}_leave_one_out.parquet")

    tcga_path = root / "results/tables/phase17_tcga_patient_bridge.parquet"
    if tcga_path.exists():
        tcga = pd.read_parquet(tcga_path)
        if "log_hazard_ratio" not in tcga.columns and "hazard_ratio" in tcga.columns:
            tcga = tcga.copy()
            tcga["log_hazard_ratio"] = np.log(tcga["hazard_ratio"].where(tcga["hazard_ratio"] > 0))
        summary, loo_df, subgroup_df = _summarize_random_effects(
            tcga,
            effect_col="log_hazard_ratio",
            se_col="log_hazard_ratio_se",
            group_col="undirected_key",
            context="TCGA bridge",
            subgroup_col="tumor_type",
        )
        if not summary.empty:
            outputs.append(summary.assign(source="tcga_bridge"))
            save_parquet(summary, root / "results/tables/tcga_bridge_meta_summary.parquet")
        if not loo_df.empty:
            save_parquet(loo_df, root / "results/tables/tcga_bridge_leave_one_family_out.parquet")
        if not subgroup_df.empty:
            save_parquet(subgroup_df, root / "results/tables/tcga_bridge_tumor_type_meta.parquet")

    if outputs:
        summary_df = pd.concat(outputs, ignore_index=True)
        save_parquet(summary_df, root / "results/tables/continuous_validation_meta_overview.parquet")
        lines = ["# Continuous Validation Meta-Analysis", ""]
        for _, row in summary_df.iterrows():
            lines.append(
                f"- {row['context']}: mu={row['meta_mu']:.3f} "
                f"(95% CI {row['meta_ci_low']:.3f}, {row['meta_ci_high']:.3f}), "
                f"p={row['meta_p']:.3g}, I2={row['meta_i2']:.3f}"
            )
        write_markdown(root / "results/reports/continuous_validation_meta.md", "\n".join(lines))

def _load_projected_graph(root: Path, topology: str) -> pd.DataFrame:
    if topology == "string":
        graph_path = root / "data_processed/string_gene_graph.parquet"
        if graph_path.exists():
            return pd.read_parquet(graph_path)
        inc_path = root / "data_processed/hypergraph_string_clique_incidence.parquet"
        if inc_path.exists():
            return project_to_graph(pd.read_parquet(inc_path))
        return pd.DataFrame(columns=["gene_a", "gene_b", "weight"])

    if topology == "corum":
        inc_path = root / "data_processed/hypergraph_corum_incidence.parquet"
    elif topology == "trrust":
        inc_path = root / "data_processed/hypergraph_trrust_regulon_incidence.parquet"
    else:
        return pd.DataFrame(columns=["gene_a", "gene_b", "weight"])

    if not inc_path.exists():
        return pd.DataFrame(columns=["gene_a", "gene_b", "weight"])
    return project_to_graph(pd.read_parquet(inc_path))

def _attach_graph_metrics(root: Path, pair_df: pd.DataFrame, topology: str) -> pd.DataFrame:
    projected = _load_projected_graph(root, topology)
    metrics = compute_projected_graph_pair_metrics(projected, pair_df["pair_key"].tolist(), seed=DEFAULT_SEED)
    return pair_df.merge(metrics, on="pair_key", how="left")

def _summarize_metric_benchmark(df: pd.DataFrame, cohort: str, topology: str, label_col: str) -> pd.DataFrame:
    score_specs = {
        "hlrc": "hlrc_score",
        "hfrc": "hfrc_score",
        "pagerank": "pair_pagerank_mean",
        "betweenness": "pair_betweenness_mean",
        "jaccard": "pair_jaccard",
        "degree": "pair_degree_mean",
    }
    rows = []
    work = df.copy()
    work[label_col] = work[label_col].astype(float)
    work = work[np.isfinite(work[label_col])]
    if work.empty:
        return pd.DataFrame()

    for metric_name, score_col in score_specs.items():
        sub = work.dropna(subset=[score_col]).copy()
        if sub.empty:
            continue
        y = sub[label_col].astype(int).to_numpy()
        x = sub[score_col].astype(float).to_numpy()
        n_total = len(sub)
        n_pos = int(y.sum())
        n_neg = int(n_total - n_pos)

        auc = np.nan
        ap = np.nan
        rho = np.nan
        rho_p = np.nan
        mw_p = np.nan

        if n_pos > 0 and n_neg > 0:
            auc = float(roc_auc_score(y, x))
            rho, rho_p = stats.spearmanr(x, y)
            pos_vals = x[y == 1]
            neg_vals = x[y == 0]
            mw_p = float(stats.mannwhitneyu(pos_vals, neg_vals, alternative="greater").pvalue)
        if n_pos > 0:
            ap = float(average_precision_score(y, x))

        ranked = sub.sort_values(score_col, ascending=False)
        top_3 = ranked.head(min(3, len(ranked)))
        top_5 = ranked.head(min(5, len(ranked)))
        top_10pct_n = max(1, int(np.ceil(len(ranked) * 0.1)))
        top_10pct = ranked.head(top_10pct_n)

        rows.append({
            "cohort": cohort,
            "topology": topology,
            "endpoint_type": "binary",
            "label_name": label_col,
            "metric_name": metric_name,
            "score_column": score_col,
            "n_total": n_total,
            "n_positive": n_pos,
            "n_negative": n_neg,
            "positive_rate": float(n_pos / n_total) if n_total else np.nan,
            "roc_auc": auc,
            "average_precision": ap,
            "spearman_rho": float(rho) if np.isfinite(rho) else np.nan,
            "spearman_p": float(rho_p) if np.isfinite(rho_p) else np.nan,
            "mannwhitney_p": mw_p,
            "top_3_positive_rate": float(top_3[label_col].mean()) if len(top_3) else np.nan,
            "top_5_positive_rate": float(top_5[label_col].mean()) if len(top_5) else np.nan,
            "top_10pct_positive_rate": float(top_10pct[label_col].mean()) if len(top_10pct) else np.nan,
            "median_score_positive": float(sub.loc[sub[label_col] == 1, score_col].median()) if n_pos > 0 else np.nan,
            "median_score_negative": float(sub.loc[sub[label_col] == 0, score_col].median()) if n_neg > 0 else np.nan,
        })

    return pd.DataFrame(rows)

def _summarize_continuous_metric_benchmark(df: pd.DataFrame, cohort: str, topology: str, value_col: str) -> pd.DataFrame:
    score_specs = {
        "hlrc": "hlrc_score",
        "hfrc": "hfrc_score",
        "pagerank": "pair_pagerank_mean",
        "betweenness": "pair_betweenness_mean",
        "jaccard": "pair_jaccard",
        "degree": "pair_degree_mean",
    }
    rows = []
    work = df.copy()
    work = work[np.isfinite(work[value_col])]
    if work.empty:
        return pd.DataFrame()

    target = (-work[value_col].astype(float)).to_numpy()
    for metric_name, score_col in score_specs.items():
        sub = work.dropna(subset=[score_col]).copy()
        if sub.empty:
            continue
        x = sub[score_col].astype(float).to_numpy()
        y = (-sub[value_col].astype(float)).to_numpy()
        rho, rho_p = stats.spearmanr(x, y)
        pearson_r, pearson_p = stats.pearsonr(x, y) if len(sub) > 2 else (np.nan, np.nan)
        rows.append({
            "cohort": cohort,
            "topology": topology,
            "endpoint_type": "continuous",
            "label_name": value_col,
            "metric_name": metric_name,
            "score_column": score_col,
            "n_total": len(sub),
            "n_positive": np.nan,
            "n_negative": np.nan,
            "positive_rate": np.nan,
            "roc_auc": np.nan,
            "average_precision": np.nan,
            "spearman_rho": float(rho) if np.isfinite(rho) else np.nan,
            "spearman_p": float(rho_p) if np.isfinite(rho_p) else np.nan,
            "pearson_r": float(pearson_r) if np.isfinite(pearson_r) else np.nan,
            "pearson_p": float(pearson_p) if np.isfinite(pearson_p) else np.nan,
            "mannwhitney_p": np.nan,
            "top_3_positive_rate": np.nan,
            "top_5_positive_rate": np.nan,
            "top_10pct_positive_rate": np.nan,
            "median_score_positive": np.nan,
            "median_score_negative": np.nan,
        })

    return pd.DataFrame(rows)

def run_graph_metric_benchmark(root):
    logger.info("\n--- Benchmark: HLRC vs Standard Graph Metrics ---")
    overlap_path = root / "results/tables/phase13_cross_topology_families.parquet"
    internal_path = root / "results/tables/all_discovery_validation_heldout.parquet"
    if not overlap_path.exists() or not internal_path.exists():
        logger.info("  - Skipping benchmark: prerequisite validation tables are missing.")
        return

    overlap = pd.read_parquet(overlap_path)
    internal = pd.read_parquet(internal_path)
    benchmark_frames = []

    topology_sources = {
        "corum": root / "results/tables/corum_family_pair_summary.parquet",
        "string": root / "results/tables/string_family_pair_summary.parquet",
        "trrust": root / "results/tables/trrust_family_pair_summary.parquet",
    }

    for topology, pair_path in topology_sources.items():
        if not pair_path.exists():
            continue
        pair_df = pd.read_parquet(pair_path).copy()
        metrics_df = _attach_graph_metrics(root, pair_df[["pair_key", "min_hlrc", "min_hfrc"]].copy(), topology)
        metrics_df["topology"] = topology
        metrics_df["hlrc_score"] = -metrics_df["min_hlrc"]
        metrics_df["hfrc_score"] = -metrics_df["min_hfrc"]
        benchmark_frames.append(metrics_df)

        if "undirected_key" in internal.columns:
            internal_topo = internal[internal["topology"] == topology].copy()
            if not internal_topo.empty:
                internal_join = internal_topo.merge(metrics_df, left_on="undirected_key", right_on="pair_key", how="inner")
                if not internal_join.empty:
                    benchmark = _summarize_metric_benchmark(internal_join, "internal_heldout", topology, "passes_validation_nominal")
                    if not benchmark.empty:
                        benchmark_frames.append(benchmark.assign(frame_type="summary"))
                    cont = _summarize_continuous_metric_benchmark(internal_join, "internal_heldout", topology, "delta_dependency")
                    if not cont.empty:
                        benchmark_frames.append(cont.assign(frame_type="summary"))

        if topology in {"corum", "string"} and not overlap.empty:
            ext_join = overlap.merge(metrics_df, left_on="undirected_key", right_on="pair_key", how="inner")
            if not ext_join.empty:
                for ext_name, ext_path in [
                    ("sanger", root / "results/tables/phase13_external_cmp_sanger_validation.parquet"),
                    ("depmap25q3", root / "results/tables/phase13_external_depmap25q3_validation.parquet"),
                ]:
                    if not ext_path.exists():
                        continue
                    ext = pd.read_parquet(ext_path)
                    merged = ext_join.merge(ext[[
                        "undirected_key",
                        "same_direction_as_discovery",
                        "passes_external_nominal",
                        "external_delta_dependency",
                    ]], on="undirected_key", how="inner")
                    if merged.empty:
                        continue
                    for label_col in ["same_direction_as_discovery", "passes_external_nominal"]:
                        summary = _summarize_metric_benchmark(merged, f"{ext_name}_{label_col}", topology, label_col)
                        if not summary.empty:
                            benchmark_frames.append(summary.assign(frame_type="summary"))
                    cont = _summarize_continuous_metric_benchmark(merged, f"{ext_name}_neg_delta_dependency", topology, "external_delta_dependency")
                    if not cont.empty:
                        benchmark_frames.append(cont.assign(frame_type="summary"))

    if not benchmark_frames:
        logger.info("  - Benchmark skipped: no joined benchmark frames were produced.")
        return

    pair_frames = [df for df in benchmark_frames if isinstance(df, pd.DataFrame) and "pair_key" in df.columns]
    summary_frames = [df for df in benchmark_frames if isinstance(df, pd.DataFrame) and "metric_name" in df.columns]

    if pair_frames:
        pair_out = pd.concat(pair_frames, ignore_index=True).drop_duplicates()
        save_parquet(pair_out, root / "results/tables/graph_metric_benchmark_pairs.parquet")

    if summary_frames:
        summary_out = pd.concat(summary_frames, ignore_index=True).drop_duplicates()
        save_parquet(summary_out, root / "results/tables/graph_metric_benchmark_summary.parquet")

        best_rows = []
        for (cohort, topology, endpoint_type, label_name), group in summary_out.groupby(["cohort", "topology", "endpoint_type", "label_name"], dropna=False):
            if endpoint_type == "continuous":
                score_order = group.sort_values(["spearman_rho", "pearson_r"], ascending=False)
            else:
                score_order = group.sort_values(["average_precision", "roc_auc"], ascending=False)
            if not score_order.empty:
                best_rows.append({
                    "cohort": cohort,
                    "topology": topology,
                    "endpoint_type": endpoint_type,
                    "label_name": label_name,
                    "best_metric": score_order.iloc[0]["metric_name"],
                    "best_average_precision": score_order.iloc[0]["average_precision"],
                    "best_roc_auc": score_order.iloc[0]["roc_auc"],
                    "best_spearman_rho": score_order.iloc[0].get("spearman_rho", np.nan),
                    "best_pearson_r": score_order.iloc[0].get("pearson_r", np.nan),
                })
        if best_rows:
            best_df = pd.DataFrame(best_rows)
            save_parquet(best_df, root / "results/tables/graph_metric_benchmark_best.parquet")

            report_lines = ["# Graph Metric Benchmark", ""]
            for _, row in best_df.iterrows():
                if row["endpoint_type"] == "continuous":
                    report_lines.append(
                        f"- {row['cohort']} / {row['topology']} / {row['endpoint_type']} / {row['label_name']}: "
                        f"best={row['best_metric']} "
                        f"(rho={row['best_spearman_rho']:.3f}, r={row['best_pearson_r']:.3f})"
                    )
                else:
                    report_lines.append(
                        f"- {row['cohort']} / {row['topology']} / {row['endpoint_type']} / {row['label_name']}: "
                        f"best={row['best_metric']} "
                        f"(AP={row['best_average_precision']:.3f}, AUC={row['best_roc_auc']:.3f})"
                    )
            write_markdown(root / "results/reports/graph_metric_benchmark.md", "\n".join(report_lines))

    logger.info("  - Benchmark tables written to results/tables/graph_metric_benchmark_*.parquet")

def main():
    config_path = ROOT / "configs/pipeline_config.json"
    if len(sys.argv) > 1:
        config_path = Path(sys.argv[1]).resolve()
        logger.info(f"--- Using Custom Config: {config_path} ---")

    config = load_config(config_path)
    
    # Re-seed for strict reproducibility
    seed = config.get("random_seed", DEFAULT_SEED)
    np.random.seed(seed)
    random.seed(seed)

    if not preflight_check(ROOT):
        sys.exit(1)
    
    run_sanger_validation(ROOT, config)
    run_depmap25q3_validation(ROOT, config)
    run_prism_validation(ROOT)
    run_graph_metric_benchmark(ROOT)
    run_overlap_continuous_meta_summaries(ROOT)

if __name__ == "__main__":
    main()