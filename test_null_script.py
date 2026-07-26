import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

ROOT = Path("/Users/jiyunlee/Desktop/project/curvature")
overlap_path = ROOT / "results/tables/overlap_family_pairs.parquet"
string_path = ROOT / "results/tables/string_family_pair_summary.parquet"

overlap_df = pd.read_parquet(overlap_path)
string_summary = pd.read_parquet(string_path)
string_summary["is_overlap_family"] = string_summary["pair_key"].isin(
    set(overlap_df["undirected_key"])
).astype(int)

features = [
    "log_pair_hyperedge_count",
    "pair_max_node_degree",
    "mean_edge_node_degree",
    "mean_pair_essentiality",
]
rng = np.random.default_rng(42)
frame = string_summary
case_flag = "is_overlap_family"
metric = "min_hlrc"
neighbor_pool_size = 50

case_df = frame[frame[case_flag] == 1].copy().reset_index(drop=True)
pos_flags = [c for c in frame.columns if c.startswith("is_")]
bg_mask = (frame[pos_flags] == 0).all(axis=1)
bg_df = frame[bg_mask].copy().reset_index(drop=True)

bg_vals_pre = bg_df[features].to_numpy()
q75_pre, q25_pre = np.percentile(bg_vals_pre, [75, 25], axis=0)
bg_iqr_pre = q75_pre - q25_pre

print("Features:", features)
print("IQR:", bg_iqr_pre)
print("Std:", bg_vals_pre.std(axis=0))

valid_mask = bg_iqr_pre > 0
if not np.all(valid_mask):
    dropped = [f for f, v in zip(features, valid_mask) if not v]
    print(f"Dropping zero-variance (IQR=0) matching features: {dropped}")
    features = [f for f, v in zip(features, valid_mask) if v]
else:
    print("No features dropped.")

bg_vals = bg_df[features].to_numpy()
bg_median = np.median(bg_vals, axis=0)
q75, q25 = np.percentile(bg_vals, [75, 25], axis=0)
bg_iqr = q75 - q25

print("Bg median:", bg_median)
print("Bg IQR:", bg_iqr)

case_vals = case_df[features].to_numpy()
print("Case mean:", case_vals.mean(axis=0))
print("Case median:", np.median(case_vals, axis=0))

from curvature_lib import matched_null_samples
rng = np.random.default_rng(42)
null_df = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=1000, neighbor_pool_size=50, metric="min_hlrc", features=features)
print("With 50 pool size, robust scaling:")
print("P-value est:", (sum(null_df["iter_null_value"] <= null_df["observed_value"].iloc[0]) + 1) / (len(null_df) + 1))
print("Null mean:", null_df["iter_null_value"].mean(), "Null std:", null_df["iter_null_value"].std())

rng = np.random.default_rng(42)
null_df_500 = matched_null_samples(string_summary, "is_overlap_family", rng, iterations=1000, neighbor_pool_size=500, metric="min_hlrc", features=features)
print("With 500 pool size, robust scaling:")
print("P-value est:", (sum(null_df_500["iter_null_value"] <= null_df_500["observed_value"].iloc[0]) + 1) / (len(null_df_500) + 1))
print("Null mean:", null_df_500["iter_null_value"].mean(), "Null std:", null_df_500["iter_null_value"].std())

