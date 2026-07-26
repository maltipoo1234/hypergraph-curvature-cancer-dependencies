import pandas as pd
import numpy as np
from pathlib import Path
from curvature_lib import matched_null_samples, summarize_nulls
import json

def find_best_threshold():
    root = Path("/Users/jiyunlee/Desktop/project/curvature")
    
    discovery_path = root / "results/tables/all_systematic_discovery_pairs.parquet"
    discovery = pd.read_parquet(discovery_path)
    
    corum_sum_path = root / "results/tables/corum_family_pair_summary.parquet"
    string_sum_path = root / "results/tables/string_family_pair_summary.parquet"
    
    corum_summary = pd.read_parquet(corum_sum_path)
    string_summary = pd.read_parquet(string_sum_path)
    
    rng = np.random.default_rng(42)
    features = ["log_pair_hyperedge_count", "log_pair_max_node_degree", "log_mean_edge_node_degree", "mean_pair_essentiality", "log_mean_hyperedge_size"]
    
    print("Threshold | Families (n) | min_hlrc p-value (empirical_p_less)")
    print("-" * 65)
    
    for threshold in np.arange(0.0, -0.6, -0.05):
        threshold = round(threshold, 2)
        
        fdr = discovery[(discovery["fdr"] <= 0.1) & (discovery["delta_dependency"] <= threshold)].copy()
        
        cor = set(fdr.loc[fdr["topology"] == "corum", "undirected_key"])
        string = set(fdr.loc[fdr["topology"] == "string", "undirected_key"])
        overlap_keys = sorted(cor & string)
        
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
                "undirected_key": key, 
                "string_min_hlrc": s_curv["min_hlrc"]
            })
            
        overlap_df = pd.DataFrame(overlap_rows)
        n = len(overlap_df)
        
        if n == 0:
            print(f"{threshold:9.2f} | {n:12} | N/A")
            continue
            
        str_sum_copy = string_summary.copy()
        str_sum_copy["is_overlap_family"] = str_sum_copy["pair_key"].isin(set(overlap_df["undirected_key"])).astype(int)
        
        nulls_m = matched_null_samples(str_sum_copy, "is_overlap_family", rng, iterations=1000, max_iterations=10000, metric="min_hlrc", features=features)
        
        if not nulls_m.empty:
            summ_m = summarize_nulls(nulls_m)
            p_val = summ_m.iloc[0]["empirical_p_less"]
            print(f"{threshold:9.2f} | {n:12} | {p_val:.4f}")
        else:
            print(f"{threshold:9.2f} | {n:12} | Error computing nulls")

if __name__ == "__main__":
    find_best_threshold()
