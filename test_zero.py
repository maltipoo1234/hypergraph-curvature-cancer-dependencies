import pandas as pd
import numpy as np
from pathlib import Path
from curvature_lib import matched_null_samples, summarize_nulls

root = Path("/Users/jiyunlee/Desktop/project/curvature")
discovery = pd.read_parquet(root / "results/tables/all_systematic_discovery_pairs.parquet")
corum_summary = pd.read_parquet(root / "results/tables/corum_family_pair_summary.parquet")
string_summary = pd.read_parquet(root / "results/tables/string_family_pair_summary.parquet")

rng = np.random.default_rng(42)
features = ["log_pair_hyperedge_count", "log_pair_max_node_degree", "log_mean_edge_node_degree", "mean_pair_essentiality", "log_mean_hyperedge_size"]

threshold = 0.0
fdr = discovery[(discovery["fdr"] <= 0.1) & (discovery["delta_dependency"] <= threshold)].copy()

cor = set(fdr.loc[fdr["topology"] == "corum", "undirected_key"])
string = set(fdr.loc[fdr["topology"] == "string", "undirected_key"])
overlap_keys = sorted(cor & string)

overlap_rows = []
for key in overlap_keys:
    c_subset = fdr[(fdr["topology"] == "corum") & (fdr["undirected_key"] == key)].sort_values("p_value")
    s_subset = fdr[(fdr["topology"] == "string") & (fdr["undirected_key"] == key)].sort_values("p_value")
    c_curv_sub = corum_summary[corum_summary["pair_key"] == key]
    s_curv_sub = string_summary[string_summary["pair_key"] == key]
    
    if c_subset.empty or s_subset.empty or c_curv_sub.empty or s_curv_sub.empty: continue
    overlap_rows.append({"undirected_key": key})

overlap_df = pd.DataFrame(overlap_rows)
str_sum_copy = string_summary.copy()
str_sum_copy["is_overlap_family"] = str_sum_copy["pair_key"].isin(set(overlap_df["undirected_key"])).astype(int)

# Run with more iterations
nulls_m = matched_null_samples(str_sum_copy, "is_overlap_family", rng, iterations=10000, max_iterations=50000, metric="min_hlrc", features=features)
summ_m = summarize_nulls(nulls_m)
print(summ_m)
