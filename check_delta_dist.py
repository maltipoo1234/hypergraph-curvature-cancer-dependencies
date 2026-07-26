import pandas as pd
from pathlib import Path

root = Path("/Users/jiyunlee/Desktop/project/curvature")
discovery = pd.read_parquet(root / "results/tables/all_systematic_discovery_pairs.parquet")
fdr_only = discovery[discovery["fdr"] <= 0.1]
print("Delta dependency stats for FDR <= 0.1:")
print(fdr_only["delta_dependency"].describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]))
