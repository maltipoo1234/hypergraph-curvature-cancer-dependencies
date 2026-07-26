from __future__ import annotations

import gzip
import json
import math
import re
import subprocess
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, Iterable, Sequence

import matplotlib
import numpy as np
import pandas as pd
from scipy import stats, optimize
from sklearn.mixture import GaussianMixture
import statsmodels.api as sm
from statsmodels.duration.hazard_regression import PHReg
import logging
import datetime

# Logging

def setup_logging(name: str, log_dir: Path | str = "logs") -> logging.Logger:
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{name}_{timestamp}.log"
    
    # Configure the root logger so that all modules share the same handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
        
    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return logging.getLogger(name)

logger = logging.getLogger("curvature_lib")

# Config

def load_config(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# DepMap Utilities

GENE_COLUMN_RE = re.compile(r"^(?P<gene>.+?) \((?P<entrez>\d+)\)$")
METADATA_COLUMNS = [
    "ModelID",
    "SequencingID",
    "ModelConditionID",
    "IsDefaultEntryForModel",
    "IsDefaultEntryForMC",
]

def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def parse_gene_column(name: str) -> dict[str, object]:
    match = GENE_COLUMN_RE.match(name.strip())
    if not match:
        return {
            "raw_name": name,
            "gene_symbol": name.strip(),
            "entrez_id": pd.NA,
            "parsed": False,
        }
    return {
        "raw_name": name,
        "gene_symbol": match.group("gene").strip(),
        "entrez_id": int(match.group("entrez")),
        "parsed": True,
    }

def strip_gene(col: str) -> str:
    return col.split(" (")[0] if " (" in col else col

def load_models(model_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(model_path)

def load_crispr(crispr_path: str | Path) -> pd.DataFrame:
    crispr = pd.read_csv(crispr_path)
    first_col = crispr.columns[0]
    if first_col != "ModelID":
        crispr = crispr.rename(columns={first_col: "ModelID"})
    return crispr

def crispr_gene_columns(crispr: pd.DataFrame) -> list[str]:
    return [col for col in crispr.columns if col != "ModelID"]

def build_gene_dictionary(crispr_columns: Sequence[str], mutation_columns: Sequence[str]) -> pd.DataFrame:
    seen: dict[str, dict[str, object]] = {}
    for source_name, source in [("crispr", crispr_columns), ("mutation", mutation_columns)]:
        for raw_name in source:
            parsed = parse_gene_column(raw_name)
            key = f"{source_name}:{raw_name}"
            seen[key] = {
                **parsed,
                "source": source_name,
            }
    return pd.DataFrame(seen.values())

def load_mutation_subset(
    mutation_path: str | Path,
    selected_genes: Iterable[str] | None = None,
) -> pd.DataFrame:
    header = pd.read_csv(mutation_path, nrows=0)
    available = list(header.columns)
    if selected_genes is None:
        usecols = available
    else:
        selected = set(selected_genes)
        usecols = []
        for col in available:
            if col in METADATA_COLUMNS:
                usecols.append(col)
                continue
            parsed = parse_gene_column(col)
            if parsed["gene_symbol"] in selected or col in selected:
                usecols.append(col)
    frame = pd.read_csv(mutation_path, usecols=usecols, low_memory=False)
    mask = frame["IsDefaultEntryForModel"].astype(str).isin(["True", "Yes"])
    frame = frame.loc[mask].copy()
    frame = frame.drop_duplicates(subset=["ModelID"])
    return frame

def mutation_gene_columns(frame: pd.DataFrame) -> list[str]:
    return [col for col in frame.columns if col not in METADATA_COLUMNS]

def mutation_binary(frame: pd.DataFrame) -> pd.DataFrame:
    genes = mutation_gene_columns(frame)
    binary_data = {}
    falsy = {"0", "0.0", "false", "none", "nan", "wt", "wildtype", ""}
    for col in genes:
        gene_symbol = parse_gene_column(col)["gene_symbol"]
        col_data = frame[col]
        if pd.api.types.is_numeric_dtype(col_data):
            mask = col_data.fillna(0).gt(0).to_numpy()
        else:
            mask = (
                col_data.notna() & 
                (~col_data.astype(str).str.lower().str.strip().isin(falsy))
            ).to_numpy()
        binary_data.setdefault(gene_symbol, []).append(mask)
    collapsed_columns = {}
    for gene_symbol, arrays in binary_data.items():
        if len(arrays) == 1:
            collapsed_columns[gene_symbol] = arrays[0]
        else:
            stacked = pd.DataFrame(arrays).T
            collapsed_columns[gene_symbol] = stacked.max(axis=1).astype(bool).to_numpy()
    collapsed = pd.DataFrame(collapsed_columns)
    collapsed.insert(0, "ModelID", frame["ModelID"].values)
    return collapsed

def compute_essentiality_baseline(
    crispr: pd.DataFrame,
    essentiality_threshold: float,
) -> pd.DataFrame:
    gene_cols = crispr_gene_columns(crispr)
    numeric = crispr[gene_cols].apply(pd.to_numeric, errors="coerce")
    baseline = pd.DataFrame(
        {
            "raw_name": gene_cols,
            "mean_gene_effect": numeric.mean(axis=0),
            "median_gene_effect": numeric.median(axis=0),
            "essential_fraction": numeric.lt(essentiality_threshold).mean(axis=0),
        }
    ).reset_index(drop=True)
    parsed = baseline["raw_name"].map(parse_gene_column).apply(pd.Series)
    return pd.concat([parsed, baseline.drop(columns=["raw_name"])], axis=1)

def classify_pan_essential(
    baseline: pd.DataFrame,
    config: dict,
    random_state: int = 42
) -> pd.DataFrame:
    result = baseline.copy()
    fallback_effect = config.get("pan_essential_fallback_effect", -0.7)
    fallback_fraction = config.get("pan_essential_fallback_fraction", 0.9)
    
    mean_effects = result["mean_gene_effect"].dropna().to_numpy().reshape(-1, 1)
    if len(mean_effects) > 10:
        gmm_effect = GaussianMixture(n_components=2, random_state=random_state)
        gmm_effect.fit(mean_effects)
        means = gmm_effect.means_.flatten()
        essential_idx = np.argmin(means)
        probs = gmm_effect.predict_proba(mean_effects)
        is_essential_by_gmm = probs[:, essential_idx] > 0.5
        if np.any(is_essential_by_gmm):
            effect_threshold = np.max(mean_effects[is_essential_by_gmm])
        else:
            logger.warning(f" GMM effect classification failed (no genes assigned to essential component). Falling back to {fallback_effect}")
            effect_threshold = fallback_effect
    else:
        effect_threshold = fallback_effect
        
    fractions = result["essential_fraction"].dropna().to_numpy().reshape(-1, 1)
    if len(fractions) > 10:
        gmm_frac = GaussianMixture(n_components=2, random_state=random_state)
        gmm_frac.fit(fractions)
        frac_means = gmm_frac.means_.flatten()
        pan_idx = np.argmax(frac_means)
        probs_frac = gmm_frac.predict_proba(fractions)
        is_pan_by_gmm = probs_frac[:, pan_idx] > 0.5
        if np.any(is_pan_by_gmm):
            fraction_threshold = np.min(fractions[is_pan_by_gmm])
        else:
            logger.warning(f" GMM fraction classification failed (no genes assigned to pan-essential component). Falling back to {fallback_fraction}")
            fraction_threshold = fallback_fraction
    else:
        fraction_threshold = fallback_fraction
        
    # Final override from explicit config if provided, otherwise use GMM-derived (or fallback)
    actual_fraction_thresh = config.get("pan_essential_fraction_threshold", fraction_threshold)
    
    result["is_pan_essential"] = (
        result["essential_fraction"].fillna(0).ge(actual_fraction_thresh)
        | result["mean_gene_effect"].fillna(math.inf).le(effect_threshold)
    )
    return result

def build_analysis_cohort(
    models: pd.DataFrame,
    crispr: pd.DataFrame,
    damaging_default: pd.DataFrame,
    hotspot_default: pd.DataFrame,
) -> pd.DataFrame:
    cohort = models.merge(crispr[["ModelID"]], on="ModelID", how="inner")
    mutation_models = pd.concat([damaging_default[["ModelID"]], hotspot_default[["ModelID"]]]).drop_duplicates()
    cohort = cohort.merge(mutation_models, on="ModelID", how="inner")
    return cohort.drop_duplicates(subset=["ModelID"]).copy()

def split_cohorts_by_lineage(
    cohort: pd.DataFrame,
    min_models: int,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    counts = cohort["OncotreeLineage"].fillna("UNKNOWN").value_counts()
    discovery_lineages = sorted(counts[counts >= min_models].index.tolist())
    discovery = cohort[cohort["OncotreeLineage"].isin(discovery_lineages)].copy()
    validation = cohort[~cohort["OncotreeLineage"].isin(discovery_lineages)].copy()
    return discovery, validation, discovery_lineages

def write_markdown(path: str | Path, text: str) -> None:
    target = Path(path)
    ensure_parent(target)
    target.write_text(text, encoding="utf-8")

def save_parquet(df: pd.DataFrame, path: str | Path) -> None:
    target = Path(path)
    ensure_parent(target)
    df.to_parquet(target, index=False)

def save_csv(df: pd.DataFrame, path: str | Path, **kwargs) -> None:
    target = Path(path)
    ensure_parent(target)
    df.to_csv(target, **kwargs)

def assert_schema(df: pd.DataFrame, expected_cols: list[str], context: str = "table") -> None:
    """Ensure dataframe is non-empty and contains all expected columns for scientific rigor."""
    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        raise ValueError(f"CRITICAL SCHEMA ERROR: Table '{context}' is missing required columns: {missing}")
    if df.empty:
        raise ValueError(f"CRITICAL DATA ERROR: Table '{context}' is empty. This prevents downstream analysis and is treated as a blocking failure to maintain scientific integrity.")

# Hypergraph Building

def _split_semicolon_field(value: str) -> list[str]:
    if pd.isna(value): return []
    return [part.strip() for part in str(value).split(";") if part.strip()]

def _open_text(path: str | Path):
    file_path = Path(path)
    if file_path.suffix == ".gz": return gzip.open(file_path, "rt")
    return open(file_path, "r", encoding="utf-8")

def load_corum(corum_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(corum_path, sep="\t", low_memory=False)

def build_corum_hyperedges(corum: pd.DataFrame, allowed_genes: Iterable[str], min_size: int, max_size: int) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int]]:
    allowed, rows, incidence_rows, total_overlap_genes, excluded_too_large, excluded_too_small = set(allowed_genes), [], [], set(), 0, 0
    for _, record in corum.iterrows():
        genes = _split_semicolon_field(record.get("subunits_gene_name", ""))
        unique_genes = []
        seen = set()
        for gene in genes:
            if gene not in seen: unique_genes.append(gene); seen.add(gene)
        overlap_genes = [gene for gene in unique_genes if gene in allowed]
        total_overlap_genes.update(overlap_genes)
        size = len(overlap_genes)
        passed = min_size <= size <= max_size
        if size < min_size: excluded_too_small += 1
        if size > max_size: excluded_too_large += 1
        row = {"hyperedge_id": f"CORUM:{record['complex_id']}", "complex_id": record["complex_id"], "complex_name": record["complex_name"], "size": size, "num_depmap_covered_subunits": size, "member_genes": ";".join(overlap_genes), "passed_main_size_filter": passed}
        rows.append(row)
        if passed:
            for gene in overlap_genes: incidence_rows.append({"hyperedge_id": row["hyperedge_id"], "gene_symbol": gene})
    edges, incidence = pd.DataFrame(rows).drop_duplicates(subset=["hyperedge_id"]), pd.DataFrame(incidence_rows)
    if not incidence.empty: edges = edges[edges["hyperedge_id"].isin(set(incidence["hyperedge_id"].unique()))].copy()
    summary = {"num_hyperedges": int(len(edges)), "num_incidence_rows": int(len(incidence)), "num_overlap_genes": int(len(total_overlap_genes)), "excluded_too_small": int(excluded_too_small), "excluded_too_large": int(excluded_too_large)}
    return edges, incidence, summary

def project_to_graph(incidence: pd.DataFrame) -> pd.DataFrame:
    edge_counts: dict[tuple[str, str], int] = {}
    for _, group in incidence.groupby("hyperedge_id"):
        genes = sorted(group["gene_symbol"].tolist())
        for a, b in combinations(genes, 2): edge_counts[(a, b)] = edge_counts.get((a, b), 0) + 1
    return pd.DataFrame([{"gene_a": a, "gene_b": b, "weight": weight} for (a, b), weight in edge_counts.items()])

STRING_GENE_SOURCES = ["Ensembl_HGNC_symbol", "BioMart_HUGO", "UniProt_GN_Name", "Ensembl_HGNC", "Ensembl_UniProt"]

def build_string_alias_lookup(alias_path: str | Path, allowed_genes: Iterable[str]) -> tuple[pd.DataFrame, dict[str, str]]:
    allowed, source_rank, best_by_protein, kept_rows = set(allowed_genes), {s: r for r, s in enumerate(STRING_GENE_SOURCES)}, {}, []
    with _open_text(alias_path) as handle:
        next(handle)
        for line in handle:
            protein_id, alias, source = line.rstrip("\n").split("\t")
            if not protein_id.startswith("9606.") or alias not in allowed or source not in source_rank: continue
            rank = source_rank[source]
            current = best_by_protein.get(protein_id)
            if current is None or (rank, alias) < (current[0], current[1]): best_by_protein[protein_id] = (rank, alias, source)
    for protein_id, (_, gene_symbol, source) in best_by_protein.items(): kept_rows.append({"string_protein_id": protein_id, "gene_symbol": gene_symbol, "alias_source": source})
    alias_df = pd.DataFrame(kept_rows)
    return alias_df, {row["string_protein_id"]: row["gene_symbol"] for _, row in alias_df.iterrows()}

def build_string_gene_graph(links_path: str | Path, protein_to_gene: dict[str, str], min_combined_score: int) -> pd.DataFrame:
    edge_scores = {}
    with _open_text(links_path) as handle:
        next(handle)
        for line in handle:
            protein1, protein2, exp, db, text, comb = line.rstrip("\n").split(" ")
            if not protein1.startswith("9606.") or not protein2.startswith("9606."): continue
            combined = int(comb)
            if combined < min_combined_score: continue
            gene1, gene2 = protein_to_gene.get(protein1), protein_to_gene.get(protein2)
            if gene1 is None or gene2 is None or gene1 == gene2: continue
            a, b = sorted((gene1, gene2))
            record = edge_scores.get((a, b))
            if record is None or combined > record["combined_score"]: edge_scores[(a, b)] = {"gene_a": a, "gene_b": b, "combined_score": combined, "experimental_score": int(exp), "database_score": int(db), "textmining_score": int(text)}
    return pd.DataFrame(edge_scores.values())

def run_smoke_test(df: pd.DataFrame, context: str, min_rows: int = 1) -> None:
    """Verifies that a table meets a minimum size requirement before proceeding."""
    if len(df) < min_rows:
        raise ValueError(f"CRITICAL SMOKE TEST FAILURE: Table '{context}' has {len(df)} rows, but requires at least {min_rows}. Halting execution to prevent invalid downstream metrics.")
    logger.info(f"  - Smoke test passed for {context} ({len(df)} rows)")

def build_maximal_clique_hyperedges(edge_list_df: pd.DataFrame, include_backbone: bool = False, prefix: str = "STRING") -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int], dict[str, set[str]]]:
    import networkx as nx
    G = nx.Graph()
    for _, row in edge_list_df.iterrows(): G.add_edge(row["gene_a"], row["gene_b"])
    edge_rows, incidence_rows = [], []
    logger.info(f"  - Finding maximal cliques for {G.number_of_nodes()} nodes and {G.number_of_edges()} edges (backbone={include_backbone})...")
    seen_cliques = set()
    for clique in nx.find_cliques(G):
        clique = tuple(sorted(clique))
        if clique in seen_cliques: continue
        seen_cliques.add(clique)
        etype = "CLIQUE" if len(clique) >= 3 else "EDGE"
        hyperedge_id = f"{prefix}_{etype}:{';'.join(clique)}"
        edge_rows.append({"hyperedge_id": hyperedge_id, "topology": prefix, "complex_name": ";".join(clique), "size": len(clique), "num_depmap_covered_subunits": len(clique), "member_genes": ";".join(clique), "passed_main_size_filter": True})
        for gene in clique: incidence_rows.append({"hyperedge_id": hyperedge_id, "gene_symbol": gene})
    
    if include_backbone:
        for u, v in G.edges():
            a, b = sorted([u, v])
            hyperedge_id = f"{prefix}_BACKBONE:{a};{b}"
            edge_rows.append({"hyperedge_id": hyperedge_id, "topology": prefix, "complex_name": f"{a};{b}", "size": 2, "num_depmap_covered_subunits": 2, "member_genes": f"{a};{b}", "passed_main_size_filter": True})
            for gene in [a, b]: incidence_rows.append({"hyperedge_id": hyperedge_id, "gene_symbol": gene})
            
    adjacency = {node: set(G.neighbors(node)) for node in G.nodes()}
    edges, incidence = pd.DataFrame(edge_rows), pd.DataFrame(incidence_rows)
    summary = {"num_gene_edges": int(len(edge_list_df)), "num_hyperedges": int(len(edges)), "num_incidence_rows": int(len(incidence)), "num_overlap_genes": int(len(set(incidence["gene_symbol"])) if not incidence.empty else 0)}
    return edges, incidence, summary, adjacency

def build_trrust_motif_hyperedges(trrust: pd.DataFrame, allowed_genes: Iterable[str], include_backbone: bool = False) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int]]:
    allowed = set(allowed_genes)
    filtered = trrust[trrust["tf"].isin(allowed) & trrust["target"].isin(allowed)].copy()
    tf_to_targets: dict[str, set[str]] = {}
    for _, row in filtered.iterrows(): tf_to_targets.setdefault(row["tf"], set()).add(row["target"])
    edge_rows, incidence_rows = [], []
    for tf, targets in tf_to_targets.items():
        regulon = tuple(sorted([tf] + list(targets)))
        etype = "REGULON" if len(regulon) >= 3 else "EDGE"
        hyperedge_id = f"TRRUST_{etype}:{tf}"
        edge_rows.append({"hyperedge_id": hyperedge_id, "topology": "TRRUST", "complex_name": f"Regulon:{tf}", "size": len(regulon), "num_depmap_covered_subunits": len(regulon), "member_genes": ";".join(regulon), "passed_main_size_filter": True})
        for gene in regulon: incidence_rows.append({"hyperedge_id": hyperedge_id, "gene_symbol": gene})
    
    if include_backbone:
        for _, row in filtered.iterrows():
            a, b = sorted([row["tf"], row["target"]])
            hyperedge_id = f"TRRUST_BACKBONE:{a};{b}"
            edge_rows.append({"hyperedge_id": hyperedge_id, "topology": "TRRUST", "complex_name": f"{a};{b}", "size": 2, "num_depmap_covered_subunits": 2, "member_genes": f"{a};{b}", "passed_main_size_filter": True})
            for gene in [a, b]: incidence_rows.append({"hyperedge_id": hyperedge_id, "gene_symbol": gene})
            
    edges, incidence = pd.DataFrame(edge_rows), pd.DataFrame(incidence_rows)
    summary = {"num_trrust_relations": int(len(filtered)), "num_hyperedges": int(len(edges)), "num_incidence_rows": int(len(incidence)), "num_overlap_genes": int(len(set(incidence["gene_symbol"])) if not incidence.empty else 0)}
    return edges, incidence, summary

def load_omnipath(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path, sep="\t", low_memory=False)

def build_interaction_hyperedges(
    interactions: pd.DataFrame,
    allowed_genes: Iterable[str],
    source_col: str = "source_genesymbol",
    target_col: str = "target_genesymbol",
    prefix: str = "OMNIPATH",
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int]]:
    import networkx as nx
    allowed = set(allowed_genes)
    filtered = interactions[interactions[source_col].isin(allowed) & interactions[target_col].isin(allowed)].copy()
    filtered = filtered[filtered[source_col] != filtered[target_col]]
    G = nx.Graph()
    for _, row in filtered.iterrows(): G.add_edge(str(row[source_col]), str(row[target_col]))
    edge_rows, incidence_rows, seen_cliques = [], [], set()
    for clique in nx.find_cliques(G):
        clique = tuple(sorted(clique))
        if clique in seen_cliques: continue
        seen_cliques.add(clique)
        etype = "CLIQUE" if len(clique) >= 3 else "EDGE"
        hid = f"{prefix}:{etype}:{';'.join(clique)}"
        edge_rows.append({"hyperedge_id": hid, "topology": prefix, "size": len(clique), "member_genes": ";".join(clique), "passed_main_size_filter": True})
        for gene in clique: incidence_rows.append({"hyperedge_id": hid, "gene_symbol": gene})
    edges, incidence = pd.DataFrame(edge_rows), pd.DataFrame(incidence_rows)
    summary = {"num_interactions": int(len(filtered)), "num_hyperedges": int(len(edges)), "num_incidence_rows": int(len(incidence)), "num_overlap_genes": int(len(set(incidence["gene_symbol"])) if not incidence.empty else 0)}
    return edges, incidence, summary

def build_standard_topologies(config: dict, root: Path, allowed_genes: set[str]) -> dict[str, tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]]:
    results = {}
    
    # STRING Alias Preprocessing
    alias_cache = root / "data/STRING/protein.human.aliases.v12.0.txt"
    if not alias_cache.exists():
        raw_alias_path = root / config["string_alias_path"]
        logger.info(f"  - Preprocessing STRING aliases from {raw_alias_path}...")
        ensure_parent(alias_cache)
        
        def open_file(p):
            if str(p).endswith(".gz"):
                return gzip.open(p, "rt", encoding="utf-8")
            return open(p, "r", encoding="utf-8")

        with open(alias_cache, "w", encoding="utf-8") as out_f:
            with open_file(raw_alias_path) as in_f:
                for line in in_f:
                    if line.startswith("9606."):
                        out_f.write(line)
    
    a = pd.read_csv(alias_cache, sep="\t", header=None, names=["protein_id", "alias", "source"])
    a = a[a["alias"].isin(allowed_genes)].copy()
    a["rank"] = a["source"].map({s: r for r, s in enumerate(STRING_GENE_SOURCES)})
    p2g = dict(zip(
        a.dropna(subset=["rank"]).sort_values(["protein_id", "rank", "alias"]).groupby("protein_id").first().reset_index()["protein_id"],
        a.dropna(subset=["rank"]).sort_values(["protein_id", "rank", "alias"]).groupby("protein_id").first().reset_index()["alias"]
    ))
    
    # STRING Links Preprocessing
    links_cache = root / "data/STRING/protein.human.links.detailed.v12.0.txt"
    if not links_cache.exists():
        raw_links_path = root / config["string_links_path"]
        logger.info(f"  - Preprocessing STRING links from {raw_links_path}...")
        ensure_parent(links_cache)
        with open(links_cache, "w", encoding="utf-8") as out_f:
            with open_file(raw_links_path) as in_f:
                for line in in_f:
                    if line.startswith("9606."):
                        out_f.write(line)
                        
    links = pd.read_csv(links_cache, sep=" ", header=None)[[0, 1, 5]]
    links.columns = ["p1", "p2", "comb"]
    links = links[links["comb"] >= config["string_min_combined_score"]].copy()
    links["ga"], links["gb"] = links["p1"].map(p2g), links["p2"].map(p2g)
    s_graph = links.dropna(subset=["ga", "gb"])[["ga", "gb"]].rename(columns={"ga":"gene_a", "gb":"gene_b"}).drop_duplicates()
    
    s_edges, s_inc, _, _ = build_maximal_clique_hyperedges(s_graph, include_backbone=False, prefix="STRING")
    if not s_edges.empty:
        s_stats = build_hypergraph_stats(s_inc, include_neighbors=True)
        results["string"] = (s_edges, s_inc, compute_hfrc(s_edges, s_inc, s_stats).merge(compute_hlrc(s_edges, s_inc, s_stats), on="hyperedge_id", how="left"), s_graph)
    
    # TRRUST
    t_path = root / config["trrust_path"]
    if t_path.exists():
        t = pd.read_csv(t_path, sep="\t", header=None, names=["tf", "target", "mode", "pmid"])
        t_edges, t_inc, _ = build_trrust_motif_hyperedges(t, allowed_genes, include_backbone=False)
        if not t_edges.empty:
            t_stats = build_hypergraph_stats(t_inc, include_neighbors=True)
            results["trrust"] = (t_edges, t_inc, compute_hfrc(t_edges, t_inc, t_stats).merge(compute_hlrc(t_edges, t_inc, t_stats), on="hyperedge_id", how="left"))
    
    return results

# Curvature

@dataclass
class HypergraphStats:
    node_degree: dict[str, int]
    node_neighbors: dict[str, set[str]]
    hyperedge_neighbors: dict[str, set[str]]

def build_hypergraph_stats(incidence: pd.DataFrame, include_neighbors: bool = True) -> HypergraphStats:
    edge_to_nodes = {eid: g["gene_symbol"].tolist() for eid, g in incidence.groupby("hyperedge_id")}
    node_degree, node_neighbors, node_to_edges = {}, {}, {}
    for eid, nodes in edge_to_nodes.items():
        for node in nodes:
            node_degree[node] = node_degree.get(node, 0) + 1
            node_to_edges.setdefault(node, set()).add(eid)
            node_neighbors.setdefault(node, set()).update(n for n in nodes if n != node)
    hyperedge_neighbors = {}
    if include_neighbors:
        for eid, nodes in edge_to_nodes.items():
            neighbors = set()
            for node in nodes: neighbors.update(node_to_edges.get(node, set()))
            neighbors.discard(eid); hyperedge_neighbors[eid] = neighbors
    return HypergraphStats(node_degree=node_degree, node_neighbors=node_neighbors, hyperedge_neighbors=hyperedge_neighbors)

def compute_hfrc(edges: pd.DataFrame, incidence: pd.DataFrame, stats: HypergraphStats | None = None) -> pd.DataFrame:
    if stats is None: stats = build_hypergraph_stats(incidence)
    edge_to_nodes, rows = incidence.groupby("hyperedge_id")["gene_symbol"].apply(list).to_dict(), []
    for _, edge in edges.iterrows():
        eid = edge["hyperedge_id"]
        nodes = edge_to_nodes.get(eid, [])
        if not nodes: rows.append({"hyperedge_id": eid, "hfrc": np.nan, "hyperedge_size": 0, "neighbor_count": 0, "mean_node_degree": np.nan, "max_node_degree": np.nan}); continue
        size = len(nodes)
        rows.append({"hyperedge_id": eid, "hfrc": float(2 * size - sum(stats.node_degree[n] for n in nodes)), "hyperedge_size": size, "neighbor_count": len(stats.hyperedge_neighbors.get(eid, set())), "mean_node_degree": float(np.mean([stats.node_degree[n] for n in nodes])), "max_node_degree": int(max(stats.node_degree[n] for n in nodes))})
    return pd.DataFrame(rows)

def compute_hlrc(edges: pd.DataFrame, incidence: pd.DataFrame, stats: HypergraphStats | None = None, verbose: bool = False, return_clipping_ratio: bool = False) -> pd.DataFrame | tuple[pd.DataFrame, float]:
    if stats is None: stats = build_hypergraph_stats(incidence)
    edge_to_nodes, rows, total_node_evals, undefined_count = {eid: g["gene_symbol"].tolist() for eid, g in incidence.groupby("hyperedge_id")}, [], 0, 0
    logger.info(f"  - Computing HLRC for {len(edges)} hyperedges...")
    for _, edge in edges.iterrows():
        eid = edge["hyperedge_id"]
        nodes = edge_to_nodes.get(eid, [])
        if not nodes: rows.append({"hyperedge_id": eid, "hlrc": np.nan}); continue
        size, neigh_sizes = len(nodes), [len(stats.node_neighbors.get(n, set())) for n in nodes]
        total_node_evals += size
        if size <= 1 or any(s == 0 for s in neigh_sizes):
            if any(s == 0 for s in neigh_sizes): undefined_count += sum(1 for s in neigh_sizes if s == 0)
            rows.append({"hyperedge_id": eid, "hlrc": np.nan}); continue
        max_n, min_n = max(neigh_sizes), min(neigh_sizes)
        common_neighbors = stats.node_neighbors.get(nodes[0], set())
        for n in nodes[1:]: common_neighbors = common_neighbors.intersection(stats.node_neighbors.get(n, set()))
        hlrc = sum(1.0 / s for s in neigh_sizes) + (len(common_neighbors) + size / 2.0 - 1.0) / max_n + (len(common_neighbors) + size / 2.0 - 1.0) / min_n - 1.0
        rows.append({"hyperedge_id": eid, "hlrc": float(hlrc)})
    undefined_ratio = undefined_count / max(total_node_evals, 1)
    if verbose: logger.info(f"HLRC Undefined Ratio: {undefined_ratio:.2%} ({undefined_count}/{total_node_evals} node-evals)")
    return (pd.DataFrame(rows), undefined_ratio) if return_clipping_ratio else pd.DataFrame(rows)

def compute_graph_forman(projected_graph: pd.DataFrame) -> pd.DataFrame:
    if projected_graph.empty: return pd.DataFrame(columns=["gene_a", "gene_b", "graph_forman"])
    degree = {}
    for _, row in projected_graph.iterrows(): degree[row["gene_a"]] = degree.get(row["gene_a"], 0) + 1; degree[row["gene_b"]] = degree.get(row["gene_b"], 0) + 1
    rows = []
    for _, row in projected_graph.iterrows(): a, b = row["gene_a"], row["gene_b"]; rows.append({"gene_a": a, "gene_b": b, "graph_forman": float(4 - degree[a] - degree[b])})
    return pd.DataFrame(rows)

def compute_projected_graph_pair_metrics(
    projected_graph: pd.DataFrame,
    pair_keys: Sequence[str],
    seed: int = 42,
    betweenness_k: int = 256,
) -> pd.DataFrame:
    import networkx as nx

    if projected_graph.empty or len(pair_keys) == 0:
        return pd.DataFrame(columns=[
            "pair_key",
            "pair_degree_mean",
            "pair_pagerank_mean",
            "pair_betweenness_mean",
            "pair_jaccard",
        ])

    work = projected_graph.copy()
    if "weight" not in work.columns:
        work["weight"] = 1.0

    graph = nx.Graph()
    for _, row in work.iterrows():
        a = str(row["gene_a"])
        b = str(row["gene_b"])
        if a == b:
            continue
        graph.add_edge(a, b, weight=float(row["weight"]))

    if graph.number_of_nodes() == 0:
        return pd.DataFrame(columns=[
            "pair_key",
            "pair_degree_mean",
            "pair_pagerank_mean",
            "pair_betweenness_mean",
            "pair_jaccard",
        ])

    degree = dict(graph.degree())
    pagerank = nx.pagerank(graph, weight="weight")
    if graph.number_of_nodes() <= 250:
        betweenness = nx.betweenness_centrality(graph, normalized=True)
    else:
        k = min(max(8, betweenness_k), graph.number_of_nodes())
        betweenness = nx.betweenness_centrality(graph, k=k, seed=seed, normalized=True)
    neighbors = {node: set(graph.neighbors(node)) for node in graph.nodes()}

    rows = []
    for pair_key in pair_keys:
        if not isinstance(pair_key, str) or ":" not in pair_key:
            continue
        a, b = pair_key.split(":", 1)
        if a not in graph or b not in graph:
            rows.append({
                "pair_key": pair_key,
                "pair_degree_mean": np.nan,
                "pair_pagerank_mean": np.nan,
                "pair_betweenness_mean": np.nan,
                "pair_jaccard": np.nan,
            })
            continue

        na = neighbors.get(a, set())
        nb = neighbors.get(b, set())
        union = na | nb
        jaccard = float(len(na & nb) / len(union)) if union else np.nan
        rows.append({
            "pair_key": pair_key,
            "pair_degree_mean": float(np.mean([degree.get(a, 0), degree.get(b, 0)])),
            "pair_pagerank_mean": float(np.mean([pagerank.get(a, np.nan), pagerank.get(b, np.nan)])),
            "pair_betweenness_mean": float(np.mean([betweenness.get(a, np.nan), betweenness.get(b, np.nan)])),
            "pair_jaccard": jaccard,
        })

    return pd.DataFrame(rows)

def select_toy_hyperedges(curvature: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    if curvature.empty: return curvature.copy()
    metric = "hlrc" if "hlrc" in curvature.columns else "hfrc"
    if metric not in curvature.columns:
        numeric_cols = curvature.select_dtypes(include=[np.number]).columns
        if not numeric_cols.empty: metric = numeric_cols[0]
        else: return curvature.head(n).copy()
    ordered = curvature.sort_values(metric).reset_index(drop=True)
    if len(ordered) <= n: return ordered.copy()
    picks = sorted(list(set([0, len(ordered) // 2, len(ordered) - 1])))[:n]
    return ordered.iloc[picks].copy()

# Stats

def bh_qvalues(p_values: np.ndarray | pd.Series | list) -> np.ndarray:
    arr = np.asarray(p_values, dtype=float)
    if arr.size == 0: return np.array([], dtype=float)
    out, valid = np.full(arr.shape, np.nan, dtype=float), np.isfinite(arr)
    if not valid.any(): return out
    ranked, order = arr[valid], np.argsort(arr[valid])
    ranked = ranked[order]; n = len(ranked)
    q = np.minimum(ranked * n / np.arange(1, n + 1), 1.0)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out[np.flatnonzero(valid)[order]] = q
    return out

def by_qvalues(p_values: np.ndarray | pd.Series | list) -> np.ndarray:
    arr = np.asarray(p_values, dtype=float)
    if arr.size == 0: return np.array([], dtype=float)
    out, valid = np.full(arr.shape, np.nan, dtype=float), np.isfinite(arr)
    if not valid.any(): return out
    ranked, order = arr[valid], np.argsort(arr[valid])
    ranked = ranked[order]; n = len(ranked); c_m = np.sum(1.0 / np.arange(1, n + 1))
    q = np.minimum(ranked * n * c_m / np.arange(1, n + 1), 1.0)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out[np.flatnonzero(valid)[order]] = q
    return out

def holm_adjusted_pvalues(p_values: np.ndarray | pd.Series | list) -> np.ndarray:
    arr = np.asarray(p_values, dtype=float)
    if arr.size == 0: return np.array([], dtype=float)
    out, valid = np.full(arr.shape, np.nan, dtype=float), np.isfinite(arr)
    if not valid.any(): return out
    ranked, order = arr[valid], np.argsort(arr[valid])
    ranked = ranked[order]; n = len(ranked)
    q = np.minimum(ranked * np.arange(n, 0, -1), 1.0)
    q = np.maximum.accumulate(q)
    out[np.flatnonzero(valid)[order]] = q
    return out

def holm_qvalues(p_values: np.ndarray | pd.Series | list) -> np.ndarray:
    # Deprecation alias
    return holm_adjusted_pvalues(p_values)

def random_effects_meta_analysis(effects: np.ndarray, ses: np.ndarray) -> dict[str, float]:
    vi, wi = ses**2, 1.0 / (ses**2)
    fixed_mu = np.sum(wi * effects) / np.sum(wi)
    q, df = np.sum(wi * (effects - fixed_mu)**2), len(effects) - 1
    if df <= 0: return {"mu": float(fixed_mu), "se": float(1.0 / np.sqrt(np.sum(wi))), "tau2": 0.0, "i2": 0.0, "q": float(q), "p": float(2 * (1 - stats.norm.cdf(abs(fixed_mu * np.sqrt(np.sum(wi))))))}
    tau2 = max(0.0, (q - df) / (np.sum(wi) - np.sum(wi**2) / np.sum(wi)))
    wi_star = 1.0 / (vi + tau2); mu_star = np.sum(wi_star * effects) / np.sum(wi_star); se_star = 1.0 / np.sqrt(np.sum(wi_star))
    return {"mu": float(mu_star), "se": float(se_star), "tau2": float(tau2), "i2": float(max(0.0, (q - df) / q) if q > 0 else 0.0), "q": float(q), "p": float(2 * (1 - stats.norm.cdf(abs(mu_star / se_star))))}

def bayesian_hierarchical_model(effects: np.ndarray, ses: np.ndarray, iterations: int = 5000, num_chains: int = 3) -> dict[str, float | np.ndarray]:
    k, sigma2 = len(effects), ses**2
    
    def run_chain(seed):
        rng = np.random.default_rng(seed)
        # Random initialization
        mu = rng.normal(np.mean(effects), np.std(effects)) if len(effects) > 1 else effects[0]
        tau = rng.uniform(0.1, 1.0)
        theta = effects.copy()
        
        samples_mu, samples_tau = [], []
        for i in range(iterations):
            # Gibbs for mu
            post_var_mu = 1.0 / (0.01 + k / (tau**2))
            mu = rng.normal(post_var_mu * (np.sum(theta) / (tau**2)), np.sqrt(post_var_mu))
            
            # Gibbs for theta_i
            post_var_theta = 1.0 / (1.0/sigma2 + 1.0/(tau**2))
            theta = rng.normal(post_var_theta * (effects/sigma2 + mu/(tau**2)), np.sqrt(post_var_theta))
            
            # Metropolis for tau (log-space proposal to maintain detailed balance)
            log_tau = np.log(tau)
            log_tau_prop = log_tau + rng.normal(0, 0.2)
            tau_prop = np.exp(log_tau_prop)

            def log_target(t):
                if t <= 0: return -1e10
                # Likelihood: theta ~ N(mu, t^2)
                # Prior: t ~ Half-Cauchy(0, 1) -> log(1 / (1 + t^2))
                return np.sum(stats.norm.logpdf(theta, mu, t)) - np.log(1 + t**2)
            
            # Target density in log-space includes the Jacobian |d tau / d log_tau| = tau
            log_acc = (log_target(tau_prop) + log_tau_prop) - (log_target(tau) + log_tau)
            
            if np.log(rng.random()) < log_acc:
                tau = tau_prop
                
            if i >= iterations // 2:
                samples_mu.append(mu)
                samples_tau.append(tau)
        return np.array(samples_mu), np.array(samples_tau)

    all_mu, all_tau = [], []
    for c in range(num_chains):
        m_samples, t_samples = run_chain(42 + c)
        all_mu.append(m_samples)
        all_tau.append(t_samples)
        
    all_mu = np.array(all_mu) # (chains, samples_per_chain)
    all_tau = np.array(all_tau)
    
    # Gelman-Rubin Diagnostic (R-hat)
    def gelman_rubin(chains_samples):
        m, n = chains_samples.shape
        if m < 2: return 1.0
        # Within-chain variance
        W = np.mean(np.var(chains_samples, axis=1, ddof=1))
        # Between-chain variance
        B = n * np.var(np.mean(chains_samples, axis=1), ddof=1)
        # Estimated marginal posterior variance
        Var = (1 - 1/n) * W + (1/n) * B
        return np.sqrt(Var / W) if W > 0 else 1.0

    rhat_mu = gelman_rubin(all_mu)
    rhat_tau = gelman_rubin(all_tau)
    
    flat_mu = all_mu.flatten()
    flat_tau = all_tau.flatten()
    
    return {
        "mu_mean": float(np.mean(flat_mu)),
        "mu_std": float(np.std(flat_mu)),
        "mu_hpd_low": float(np.percentile(flat_mu, 2.5)),
        "mu_hpd_high": float(np.percentile(flat_mu, 97.5)),
        "tau_median": float(np.median(flat_tau)),
        "p_negative": float(np.mean(flat_mu < 0)),
        "rhat_mu": float(rhat_mu),
        "rhat_tau": float(rhat_tau),
        # MH Acceptance Rate: Ratio of unique samples to total samples.
        # Since tau is continuous, every rejection duplicates the previous value,
        # while every acceptance is uniquely distinct.
        "acceptance_rate": len(set(flat_tau)) / len(flat_tau) if len(flat_tau) > 0 else 0.0,
        "mu_samples": flat_mu,
        "tau_samples": flat_tau
    }

# Dependencies

def benjamini_hochberg(p_values: pd.Series) -> pd.Series:
    ranked = p_values.rank(method="first"); n = len(p_values)
    adjusted = (p_values * n / ranked).clip(upper=1.0)
    return adjusted.sort_values(ascending=False).cummin().sort_index()

def compute_mutation_specific_dependencies(hypergraph_genes: list[str], gene_partners: dict[str, set[str]], crispr: pd.DataFrame, hotspot_binary: pd.DataFrame, damaging_binary: pd.DataFrame, cohort: pd.DataFrame, config: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    crispr_subset = crispr[crispr["ModelID"].isin(cohort["ModelID"])].set_index("ModelID").apply(pd.to_numeric, errors="coerce")
    crispr_lookup = {parse_gene_column(c)["gene_symbol"]: c for c in crispr_subset.columns}
    hotspot, damaging = hotspot_binary[hotspot_binary["ModelID"].isin(cohort["ModelID"])].set_index("ModelID"), damaging_binary[damaging_binary["ModelID"].isin(cohort["ModelID"])].set_index("ModelID")
    genes, panel_rows, dep_rows = [g for g in hypergraph_genes if g in hotspot.columns or g in damaging.columns], [], []
    for gene in genes:
        for mtype, mut_df in [("hotspot", hotspot), ("damaging", damaging)]:
            if gene not in mut_df.columns or mut_df[gene].sum() < config["mutation_min_mutant_models"]: continue
            mask = mut_df[gene].astype(bool); mut_ids, wt_ids = mask[mask].index, mask[~mask].index
            if len(mut_ids) < config["mutation_min_mutant_models"] or len(wt_ids) < config["mutation_min_wildtype_models"]: continue
            panel_rows.append({"mutation_gene": gene, "num_mutant_models": len(mut_ids), "num_wildtype_models": len(wt_ids), "mutation_type": mtype})
            for partner in sorted(gene_partners.get(gene, set())):
                pcol = crispr_lookup.get(partner)
                if pcol is None: continue
                m_vals, w_vals = crispr_subset.loc[mut_ids, pcol].dropna(), crispr_subset.loc[wt_ids, pcol].dropna()
                if len(m_vals) < config["mutation_min_mutant_models"] or len(w_vals) < config["mutation_min_wildtype_models"]: continue
                test = stats.ttest_ind(m_vals, w_vals, equal_var=False, nan_policy="omit")
                dep_rows.append({"mutation_gene": gene, "partner_gene": partner, "mutation_type": mtype, "num_mutant_models": len(m_vals), "num_wildtype_models": len(w_vals), "delta_dependency": float(m_vals.mean() - w_vals.mean()), "p_value": float(test.pvalue if np.isfinite(test.pvalue) else 1.0)})
    dep = pd.DataFrame(dep_rows)
    if not dep.empty: dep["fdr"] = benjamini_hochberg(dep["p_value"]); dep["passes_main_thresholds"] = (dep["fdr"] <= config["dependency_fdr_threshold"]) & (dep["delta_dependency"] <= config["dependency_effect_threshold"])
    return pd.DataFrame(panel_rows).drop_duplicates(), dep

# External Validation

def detect_model_column(cols: list[str]) -> str:
    for c in ["ModelID", "model_id", "SangerModelID", "model_name", "SIDM"]:
        if c in cols: return c
    return cols[0]

def read_table(path: Path) -> pd.DataFrame:
    if path.suffix == ".parquet": return pd.read_parquet(path)
    return pd.read_csv(path, sep="\t" if path.suffix in {".tsv", ".txt"} else ",", low_memory=False)

def welch_delta_p(mask: np.ndarray, values: np.ndarray, min_group_size: int = 3, directional_hypothesis: str = "less") -> tuple[float, float, int, int, float]:
    m, w = values[mask], values[~mask]; m, w = m[np.isfinite(m)], w[np.isfinite(w)]
    if len(m) < min_group_size or len(w) < min_group_size: return np.nan, np.nan, len(m), len(w), np.nan
    t, p = stats.ttest_ind(m, w, equal_var=False, nan_policy="omit")
    
    # Standard error of the difference (Welch's)
    se = np.sqrt(np.var(m, ddof=1)/len(m) + np.var(w, ddof=1)/len(w))
    
    if directional_hypothesis == "less": p = p / 2.0 if t < 0 else 1.0 - (p / 2.0)
    elif directional_hypothesis == "greater": p = p / 2.0 if t > 0 else 1.0 - (p / 2.0)
    return float(m.mean() - w.mean()), float(p), len(m), len(w), float(se)

def load_project_score_matrix(path: Path, source_filter: str | None = None) -> pd.DataFrame:
    raw = pd.read_csv(path, sep="\t", low_memory=False)
    if "model_name" not in raw.columns: raise ValueError("Not a recognized Project Score wide matrix format.")
    mrow = raw[raw["model_name"] == "model_id"]
    if mrow.empty: raise ValueError("Project Score matrix is missing the 'model_id' metadata row.")
    mrow = mrow.iloc[0]
    hidx = raw.index[raw["model_name"] == "gene_id"]
    if len(hidx) == 0: raise ValueError("Project Score matrix is missing the 'gene_id' header marker row.")
    hidx = int(hidx[0])
    mcols = [c for c in raw.columns if c not in ["model_name", "Unnamed: 1", "Unnamed: 2"]]
    if source_filter:
        srow = raw[raw["model_name"] == "source"]
        if srow.empty: raise ValueError("Project Score matrix is missing the 'source' metadata row.")
        mcols = [c for c in mcols if str(srow.iloc[0][c]).strip().lower() == source_filter.lower()]
    s2c = {}
    for c in mcols:
        sidm = str(mrow[c])
        if sidm.startswith("SIDM"): s2c.setdefault(sidm, []).append(c)
    data = raw.iloc[hidx + 1 :].rename(columns={"model_name": "gene_id", "Unnamed: 1": "symbol", "Unnamed: 2": "ensembl_gene_id"}).dropna(subset=["symbol"])
    out, genes = {"SangerModelID": []}, data["symbol"].astype(str).tolist()
    for sidm, cols in s2c.items():
        out["SangerModelID"].append(sidm); vals = data[cols].apply(pd.to_numeric, errors="coerce").mean(axis=1).to_numpy(dtype=float)
        for g, v in zip(genes, vals): out.setdefault(g, []).append(v)
    f = pd.DataFrame(out)
    if "bayesian_factors" in path.name: f[[c for c in f.columns if c != "SangerModelID"]] = -f[[c for c in f.columns if c != "SangerModelID"]]
    return f

def prepare_generic_external_matrix(path: Path, models: pd.DataFrame) -> pd.DataFrame:
    external = read_table(path).copy()
    model_col = detect_model_column(external.columns.tolist())
    external = external.rename(columns={model_col: "SangerModelID", **{c: strip_gene(c) for c in external.columns if c != model_col}})
    return external.merge(models, on="SangerModelID", how="inner")

def validate_family_set(families: pd.DataFrame, external: pd.DataFrame, mutation_lookup: dict[str, pd.DataFrame], model_col: str = "ModelID", discovery_delta_col: str = "delta_dependency") -> pd.DataFrame:
    rows = []
    for _, row in families.iterrows():
        mut_type = row["mutation_type"]
        mut_gene = row["mutation_gene"]
        partner_gene = row["partner_gene"]
        
        # Rigorous check for gene presence in external data and mutation lookup
        if partner_gene not in external.columns or mut_gene not in mutation_lookup[mut_type].columns:
            rows.append({
                "undirected_key": row["undirected_key"], "mutation_gene": mut_gene, "partner_gene": partner_gene, 
                "mutation_type": mut_type, "external_delta_dependency": np.nan, "external_p_value": np.nan, 
                "external_num_mutant": 0, "external_num_wildtype": 0, "external_se": np.nan, 
                "same_direction_as_discovery": False, "passes_external_nominal": False, "external_gene_available": False
            })
            continue
            
        m = external[[model_col, partner_gene]].merge(mutation_lookup[mut_type][[model_col, mut_gene]], on=model_col, how="inner")
        delta, p, n_m, n_w, se = welch_delta_p(m[row["mutation_gene"]].fillna(0).to_numpy() > 0, m[row["partner_gene"]].to_numpy())
        sd = bool(np.isfinite(delta) and delta < 0 and row[discovery_delta_col] < 0)
        rows.append({"undirected_key": row["undirected_key"], "mutation_gene": row["mutation_gene"], "partner_gene": row["partner_gene"], "mutation_type": row["mutation_type"], "external_delta_dependency": delta, "external_p_value": p, "external_num_mutant": n_m, "external_num_wildtype": n_w, "external_se": se, "same_direction_as_discovery": sd, "passes_external_nominal": bool(np.isfinite(p) and p < 0.05 and sd), "external_gene_available": True})
    return pd.DataFrame(rows)

# Cell Model Passports

SANGER_DAMAGING_EFFECTS = {"frameshift", "nonsense", "ess_splice", "stop_lost", "start_lost", "splice_region", "3prime_UTR_ess_splice"}
SANGER_HOTSPOT_EFFECTS = {"missense", "inframe"}

def _build_binary_matrix(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty: return pd.DataFrame(columns=["ModelID"])
    work = frame[["ModelID", "gene_symbol"]].copy(); work["value"] = 1
    matrix = work.pivot_table(index="ModelID", columns="gene_symbol", values="value", aggfunc="max", fill_value=0).reset_index()
    matrix.columns = [str(col) for col in matrix.columns]
    return matrix

def build_matched_sanger_mutation_lookup(mutations_path: str | Path, model_map_path: str | Path, hotspot_min_models: int = 5) -> dict[str, pd.DataFrame]:
    model_map = pd.read_csv(model_map_path, usecols=["model_id", "BROAD_ID"]).dropna().drop_duplicates().rename(columns={"model_id": "sanger_model_id", "BROAD_ID": "ModelID"})
    muts = pd.read_csv(mutations_path, usecols=["model_id", "gene_symbol", "effect", "protein_mutation", "source"], low_memory=False)
    muts = muts[muts["source"].astype(str).str.lower().eq("sanger")].merge(model_map, left_on="model_id", right_on="sanger_model_id", how="inner")
    muts["gene_symbol"], muts["protein_mutation"] = muts["gene_symbol"].astype(str), muts["protein_mutation"].astype(str)
    damaging = _build_binary_matrix(muts[muts["effect"].astype(str).isin(SANGER_DAMAGING_EFFECTS)])
    recurrent = muts[muts["effect"].astype(str).isin(SANGER_HOTSPOT_EFFECTS)].loc[lambda x: x["protein_mutation"].ne("p.?") & x["protein_mutation"].ne("-") & x["protein_mutation"].ne("nan")].groupby(["gene_symbol", "protein_mutation"])["ModelID"].nunique().reset_index(name="n_models")
    hotspot = _build_binary_matrix(muts.merge(recurrent[recurrent["n_models"] >= hotspot_min_models][["gene_symbol", "protein_mutation"]].drop_duplicates(), on=["gene_symbol", "protein_mutation"], how="inner"))
    return {"damaging": damaging, "hotspot": hotspot}

# Permutation Utilities

def matched_null_samples(frame: pd.DataFrame, case_flag: str, rng: np.random.Generator, iterations: int, neighbor_pool_size: int = 500, metric: str = "min_hlrc", features: list[str] | None = None, max_iterations: int | None = None, p_threshold: float = 0.05) -> pd.DataFrame:
    from scipy.spatial import KDTree
    case_df = frame[frame[case_flag] == 1].copy().reset_index(drop=True)
    bg_mask = frame[case_flag] == 0
    bg_df = frame[bg_mask].copy().reset_index(drop=True)
    if case_df.empty or bg_df.empty: return pd.DataFrame()
    
    if features is None:
        features = ["log_pair_hyperedge_count", "log_pair_max_node_degree", "log_mean_edge_node_degree", "mean_pair_essentiality", "log_mean_hyperedge_size"]
    features = [f for f in features if f in bg_df.columns]
    
    case_df = case_df.dropna(subset=features).reset_index(drop=True)
    bg_df = bg_df.dropna(subset=features).reset_index(drop=True)
    if case_df.empty or bg_df.empty: return pd.DataFrame()
    
    bg_vals_pre = bg_df[features].to_numpy()
    bg_std_pre = bg_vals_pre.std(axis=0)
    
    # Identify and drop zero-variance features
    valid_mask = bg_std_pre > 0
    if not np.all(valid_mask):
        dropped = [f for f, v in zip(features, valid_mask) if not v]
        logger.warning(f"Dropping zero-variance matching features: {dropped}")
        features = [f for f, v in zip(features, valid_mask) if v]
        if not features:
            logger.error("No valid matching features remain after dropping zero-variance dimensions.")
            return pd.DataFrame()
            
    bg_vals = bg_df[features].to_numpy()
    bg_mean = bg_vals.mean(axis=0)
    bg_std = bg_vals.std(axis=0)
    bg_norm = (bg_vals - bg_mean) / bg_std
    tree = KDTree(bg_norm)
    obs_val = case_df[metric].mean()
    k_to_use = min(neighbor_pool_size, len(bg_df))

    # Normalize case features
    case_vals = case_df[features].to_numpy()
    case_norm = (case_vals - bg_mean) / bg_std
    
    # Vectorized batch query
    # Returns (n_cases, k_to_use) array of background indices
    _, neighbor_indices = tree.query(case_norm, k=k_to_use)
    
    def generate_null_iterations(n_iters, offset=0):
        # neighbor_indices is (n_cases, k_to_use)
        # We need to pick one random neighbor for each case, for each iteration
        # indices_choice is (n_iters, n_cases)
        random_k_idx = rng.integers(0, k_to_use, size=(n_iters, len(case_df)))
        
        # Use advanced indexing to pull the actual background indices
        # neighbor_indices[np.arange(len(case_df)), random_k_idx] -> (n_iters, n_cases)
        # We broadcast the case index across iterations
        case_idx_seq = np.arange(len(case_df))
        selected_bg_indices = neighbor_indices[case_idx_seq, random_k_idx]
        
        # Compute mean metric for each iteration
        # selected_bg_indices has shape (n_iters, n_cases)
        # bg_df[metric].values[selected_bg_indices] -> (n_iters, n_cases)
        null_vals = bg_df[metric].values[selected_bg_indices].mean(axis=1)
        
        return [{"iteration": offset + i, "observed_count": len(case_df), "metric": metric, "observed_value": obs_val, "iter_null_value": val} for i, val in enumerate(null_vals)]

    # Initial sampling
    null_rows = generate_null_iterations(iterations)
    
    # Adaptive refinement
    if max_iterations and max_iterations > iterations:
        count_less = sum(1 for r in null_rows if r["iter_null_value"] <= obs_val)
        p_est = (count_less + 1) / (len(null_rows) + 1)
        if p_est < p_threshold:
            logger.info(f"    - Adaptive step: p_est={p_est:.4f} < {p_threshold}, ramping to {max_iterations} iterations...")
            null_rows.extend(generate_null_iterations(max_iterations - iterations, offset=iterations))
                
    return pd.DataFrame(null_rows)

def summarize_nulls(null_df: pd.DataFrame) -> pd.DataFrame:
    if null_df.empty: return pd.DataFrame()
    # Assuming one metric per null_df for consistency
    metric = null_df["metric"].iloc[0]
    obs_val = null_df["observed_value"].iloc[0]
    
    # fix: Use plus-one correction for p-values (count + 1) / (N + 1)
    # This avoids reporting p=0.00000 which is statistically indefensible for finite N.
    count_less = (null_df["iter_null_value"] <= obs_val).sum()
    n_iters = len(null_df)
    p_corr = (count_less + 1) / (n_iters + 1)
    
    res = {
        "metric": metric,
        "observed_count": int(null_df["observed_count"].iloc[0]),
        "observed_value": obs_val,
        "null_mean": null_df["iter_null_value"].mean(),
        "iter_null_std": null_df["iter_null_value"].std(),
        "iter_null_min": null_df["iter_null_value"].min(),
        "iter_null_max": null_df["iter_null_value"].max(),
        "empirical_p_less": p_corr,
        "n_permutations": n_iters
    }
    return pd.DataFrame([res])

def _normalize_col_lookup(frame):
    return {str(c).strip().lower(): c for c in frame.columns}

def _pick_first_existing_col(frame, candidates):
    lookup = _normalize_col_lookup(frame)
    for cand in candidates:
        key = str(cand).strip().lower()
        if key in lookup:
            return lookup[key]
    return None

def _coerce_binary_series(series):
    if pd.api.types.is_numeric_dtype(series):
        return series.fillna(0).astype(float).gt(0).astype(int)
    falsy = {"0", "0.0", "false", "none", "nan", "wt", "wildtype", "", "wt-like"}
    return (~series.astype(str).str.lower().str.strip().isin(falsy)).astype(int)

def _schoenfeld_diagnostics(
    res,
    sub: pd.DataFrame,
    time_col: str,
    event_col: str,
    exog_cols: list[str],
    mutation_gene: str,
    partner_gene: str,
    histology_value: str,
) -> pd.DataFrame:
    residuals = pd.DataFrame(res.schoenfeld_residuals, columns=exog_cols, index=sub.index)
    event_mask = sub[event_col].astype(bool)
    event_times = pd.to_numeric(sub.loc[event_mask, time_col], errors="coerce")
    valid_time = np.isfinite(event_times.to_numpy())

    if valid_time.sum() < 5:
        return pd.DataFrame()

    x = stats.rankdata(event_times.to_numpy()[valid_time])

    rows = []
    pvals = []
    for col in exog_cols:
        y = pd.to_numeric(residuals.loc[event_mask, col], errors="coerce").to_numpy()[valid_time]
        valid = np.isfinite(x) & np.isfinite(y)

        if valid.sum() < 5 or np.nanstd(y[valid]) == 0:
            rho, p = np.nan, np.nan
        else:
            rho, p = stats.spearmanr(x[valid], y[valid])

        rows.append(
            {
                "histology": histology_value,
                "mutation_gene": mutation_gene,
                "partner_gene": partner_gene,
                "coefficient": col,
                "schoenfeld_rho": float(rho) if np.isfinite(rho) else np.nan,
                "schoenfeld_p_value": float(p) if np.isfinite(p) else np.nan,
                "n_event_rows": int(valid.sum()),
            }
        )
        if np.isfinite(p):
            pvals.append(float(p))

    if pvals:
        chi2 = -2.0 * np.sum(np.log(np.clip(pvals, 1e-300, 1.0)))
        global_p = float(stats.chi2.sf(chi2, 2 * len(pvals)))
    else:
        global_p = np.nan

    out = pd.DataFrame(rows)
    if not out.empty:
        out["ph_global_p_value"] = global_p
        out["ph_flag"] = bool(np.isfinite(global_p) and global_p < 0.05)
    return out

def run_survival_bridge(
    df: pd.DataFrame,
    mutation_gene: str,
    partner_gene: str,
    histology_value: str,
    max_missing_fraction: float = 0.2,
    histology_col_candidates: tuple[str, ...] = (
        "OncotreeLineage",
        "OncoTreeLineage",
        "histology",
        "histology_type",
        "tumor_type",
        "cancer_type",
        "primary_disease",
        "project",
    ),
    time_col_candidates: tuple[str, ...] = (
        "PFI.time",
        "PFI_time",
        "PFI time",
        "pfi_time",
        "time",
        "survival_time",
        "days_to_event",
    ),
    event_col_candidates: tuple[str, ...] = (
        "PFI",
        "PFI.event",
        "PFI_event",
        "event",
        "status",
        "survival_event",
    ),
    covariate_groups: tuple[tuple[str, ...], ...] = (
        ("age_at_diagnosis", "diagnosis_age", "age", "Age"),
        ("gender", "sex", "patient_gender"),
        ("simplified_stage", "stage", "tumor_stage", "pathologic_stage", "ajcc_pathologic_stage"),
        ("log_TMB", "logTMB", "tmb", "tumor_mutational_burden", "TMB"),
        ("KRAS_mutation", "KRAS", "kras_mutation_status"),
        ("TP53_mutation", "TP53", "tp53_mutation_status"),
    ),
) -> tuple[pd.DataFrame, pd.DataFrame]:
    work = df.copy()

    histology_col = _pick_first_existing_col(work, histology_col_candidates)
    if histology_col is not None:
        hist_mask = work[histology_col].astype(str).str.upper().eq(str(histology_value).upper())
        work = work.loc[hist_mask].copy()
    else:
        logger.warning("No histology column found for TCGA survival bridge; skipping cohort-specific fit.")
        return pd.DataFrame(), pd.DataFrame()

    time_col = _pick_first_existing_col(work, time_col_candidates)
    event_col = _pick_first_existing_col(work, event_col_candidates)
    mutation_col = _pick_first_existing_col(
        work,
        (
            f"{mutation_gene}_mutation",
            f"{mutation_gene}_mut",
            f"{mutation_gene}_status",
            mutation_gene,
        ),
    )
    partner_col = _pick_first_existing_col(
        work,
        (
            f"{partner_gene}_dependency",
            f"{partner_gene}_expression",
            f"{partner_gene}_expr",
            partner_gene,
        ),
    )

    if time_col is None or event_col is None or mutation_col is None:
        return pd.DataFrame(), pd.DataFrame()

    base_cols = [time_col, event_col, mutation_col]

    candidate_covs = []
    for group in covariate_groups:
        col = _pick_first_existing_col(work, group)
        if col is not None:
            candidate_covs.append(col)


    retained_covs = []
    dropped_covs = []
    for cov in candidate_covs:
        miss_frac = float(work[cov].isna().mean())
        if miss_frac > max_missing_fraction:
            dropped_covs.append(cov)
        else:
            retained_covs.append(cov)

    sub = work[base_cols + retained_covs].copy()
    sub = sub.dropna(subset=base_cols + retained_covs).copy()

    sub[mutation_col] = _coerce_binary_series(sub[mutation_col])
    sub[event_col] = _coerce_binary_series(sub[event_col])

    n_mut = int((sub[mutation_col] == 1).sum())
    n_wt = int((sub[mutation_col] == 0).sum())
    if n_mut < 5 or n_wt < 20 or len(sub) < 15 or sub[mutation_col].nunique() < 2:
        return pd.DataFrame(), pd.DataFrame()

    exog_cols = [mutation_col]
    for cov in retained_covs:
        if cov not in sub.columns:
            continue
        if pd.api.types.is_numeric_dtype(sub[cov]) and sub[cov].nunique(dropna=True) >= 2:
            sub[cov] = pd.to_numeric(sub[cov], errors="coerce")
            exog_cols.append(cov)
        elif sub[cov].nunique(dropna=True) >= 2:
            dummies = pd.get_dummies(sub[cov].astype(str), prefix=cov, drop_first=True)
            if not dummies.empty:
                for dcol in dummies.columns:
                    sub[dcol] = dummies[dcol].astype(float)
                    exog_cols.append(dcol)

    if len(exog_cols) < 2:
        return pd.DataFrame(), pd.DataFrame()

    try:
        import warnings
        from statsmodels.tools.sm_exceptions import ConvergenceWarning

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", ConvergenceWarning)
            mod = PHReg(sub[time_col].astype(float), sub[exog_cols].astype(float), status=sub[event_col].astype(int))
            res = mod.fit(disp=False)

            for warning in caught:
                if issubclass(warning.category, ConvergenceWarning):
                    return pd.DataFrame(), pd.DataFrame()

        idx = exog_cols.index(mutation_col)
        coef = float(res.params[idx])
        se = float(res.bse[idx]) if hasattr(res, "bse") and len(res.bse) > idx else np.nan

        summary = pd.DataFrame(
            [
                {
                    "histology": histology_value,
                    "mutation_gene": mutation_gene,
                    "partner_gene": partner_gene,
                    "mutation_col": mutation_col,
                    "partner_col": partner_col,
                    "time_col": time_col,
                    "event_col": event_col,
                    "p_value": float(res.pvalues[idx]),
                    "hazard_ratio": float(np.exp(coef)),
                    "coef": coef,
                    "coef_se": se,
                    "log_hazard_ratio": coef,
                    "log_hazard_ratio_se": se,
                    "log_hazard_ratio_ci_low": float(coef - 1.96 * se) if np.isfinite(se) else np.nan,
                    "log_hazard_ratio_ci_high": float(coef + 1.96 * se) if np.isfinite(se) else np.nan,
                    "hazard_ratio_ci_low": float(np.exp(coef - 1.96 * se)) if np.isfinite(se) else np.nan,
                    "hazard_ratio_ci_high": float(np.exp(coef + 1.96 * se)) if np.isfinite(se) else np.nan,
                    "n_total": int(len(sub)),
                    "n_events": int(sub[event_col].sum()),
                    "n_mutant": n_mut,
                    "n_wildtype": n_wt,
                    "covariates_used": ";".join(retained_covs),
                    "covariates_dropped": ";".join(dropped_covs),
                }
            ]
        )

        diag = _schoenfeld_diagnostics(
            res,
            sub,
            time_col,
            event_col,
            exog_cols,
            mutation_gene,
            partner_gene,
            histology_value,
        )
        return summary, diag

    except Exception as e:
        logger.warning(f"Survival model for {mutation_gene}:{partner_gene} in {histology_value} failed: {e}")
        return pd.DataFrame(), pd.DataFrame()
    
# sorry this is very slow. But it works anyway and I am too tired to improve the performance.
def bipartite_degree_preserving_shuffle(incidence: pd.DataFrame, rng: np.random.Generator, swaps_multiplier: int, mixing_threshold: float = 0.01) -> pd.DataFrame:
    shuffled = incidence[["hyperedge_id", "gene_symbol"]].copy().reset_index(drop=True)
    original_pairs = set(zip(shuffled["hyperedge_id"], shuffled["gene_symbol"]))
    edge_to_nodes = shuffled.groupby("hyperedge_id")["gene_symbol"].apply(set).to_dict()
    max_swaps, min_swaps, swaps_performed = len(shuffled) * swaps_multiplier * 5, len(shuffled) * swaps_multiplier, 0
    while swaps_performed < max_swaps:
        i, j = rng.integers(0, len(shuffled), size=2)
        if i == j: continue
        edge_i, edge_j, gene_i, gene_j = shuffled.at[i, "hyperedge_id"], shuffled.at[j, "hyperedge_id"], shuffled.at[i, "gene_symbol"], shuffled.at[j, "gene_symbol"]
        if edge_i == edge_j or gene_i == gene_j or gene_i in edge_to_nodes[edge_j] or gene_j in edge_to_nodes[edge_i]: continue
        shuffled.at[i, "gene_symbol"], shuffled.at[j, "gene_symbol"] = gene_j, gene_i
        edge_to_nodes[edge_i].remove(gene_i); edge_to_nodes[edge_i].add(gene_j); edge_to_nodes[edge_j].remove(gene_j); edge_to_nodes[edge_j].add(gene_i)
        swaps_performed += 1
        if swaps_performed >= min_swaps and swaps_performed % (max(min_swaps // 10, 1)) == 0:
            if len(original_pairs.intersection(set(zip(shuffled["hyperedge_id"], shuffled["gene_symbol"])))) / len(original_pairs) < mixing_threshold: break
    return shuffled

# Unit Tests

def run_unit_tests():
    import unittest

    class TestCurvature(unittest.TestCase):
        def test_parse_gene_column(self):
            self.assertEqual(parse_gene_column("TP53 (7157)")["gene_symbol"], "TP53")
            self.assertEqual(parse_gene_column("TP53 (7157)")["entrez_id"], 7157)
            self.assertEqual(parse_gene_column("BAD_NAME")["gene_symbol"], "BAD_NAME")
            self.assertFalse(parse_gene_column("BAD_NAME")["parsed"])

        def test_strip_gene(self):
            self.assertEqual(strip_gene("BRAF (673)"), "BRAF")
            self.assertEqual(strip_gene("EGFR"), "EGFR")

        def test_curvature_simple(self):
            edges = pd.DataFrame([{"hyperedge_id": "E1"}])
            incidence = pd.DataFrame([
                {"hyperedge_id": "E1", "gene_symbol": "A"},
                {"hyperedge_id": "E1", "gene_symbol": "B"},
                {"hyperedge_id": "E1", "gene_symbol": "C"},
            ])
            stats = build_hypergraph_stats(incidence)
            hfrc = compute_hfrc(edges, incidence, stats)
            self.assertEqual(hfrc.iloc[0]["hfrc"], 2*3 - (1+1+1))
            hlrc = compute_hlrc(edges, incidence, stats)
            self.assertTrue(np.isfinite(hlrc.iloc[0]["hlrc"]))

        def test_bh_qvalues(self):
            p_values = [0.01, 0.05, 0.5, 0.8]
            q_values = bh_qvalues(p_values)
            self.assertEqual(len(q_values), 4)
            self.assertTrue(all(q_values[i] <= q_values[i+1] for i in range(len(q_values)-1)))
            self.assertLess(q_values[0], 0.05)

        def test_holm_adjusted_pvalues(self):
            p_values = [0.01, 0.04, 0.05, 0.5]
            # Sorted: 0.01 (x4), 0.04 (x3), 0.05 (x2), 0.5 (x1)
            # Holm:   0.04,      0.12,      0.12,      0.5
            adj_p = holm_adjusted_pvalues(p_values)
            self.assertEqual(len(adj_p), 4)
            self.assertAlmostEqual(adj_p[0], 0.04)
            self.assertAlmostEqual(adj_p[1], 0.12)
            self.assertAlmostEqual(adj_p[2], 0.12)  # max(0.12, 0.05*2) = 0.12
            self.assertAlmostEqual(adj_p[3], 0.5)

            # Test edge cases
            self.assertEqual(len(holm_adjusted_pvalues([])), 0)
            self.assertEqual(len(holm_adjusted_pvalues([np.nan, np.nan])), 2)
            self.assertTrue(np.isnan(holm_adjusted_pvalues([np.nan])[0]))
            self.assertAlmostEqual(holm_adjusted_pvalues([0.05])[0], 0.05)

        def test_matched_null_samples(self):
            data = pd.DataFrame({
                "pair_key": [f"P{i}" for i in range(100)],
                "is_case": [1]*10 + [0]*90,
                "min_hlrc": np.random.randn(100),
                "log_pair_hyperedge_count": np.random.rand(100),
                "pair_max_node_degree": np.random.rand(100),
                "mean_edge_node_degree": np.random.rand(100),
                "mean_pair_essentiality": np.random.rand(100)
            })
            data["is_other"] = 0
            rng = np.random.default_rng(42)
            nulls = matched_null_samples(data, "is_case", rng, iterations=10)
            self.assertEqual(len(nulls), 10)
            self.assertIn("iter_null_value", nulls.columns)

        def test_bayesian_meta_analysis(self):
            effects = np.array([-0.2, -0.3, -0.25, -0.1, -0.4])
            ses = np.array([0.05, 0.04, 0.06, 0.08, 0.03])
            res = bayesian_hierarchical_model(effects, ses, iterations=1000, num_chains=2)
            self.assertIn("mu_mean", res)
            self.assertIn("rhat_mu", res)
            self.assertIn("mu_samples", res)
            self.assertLess(res["rhat_mu"], 1.1)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCurvature)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    run_unit_tests()
