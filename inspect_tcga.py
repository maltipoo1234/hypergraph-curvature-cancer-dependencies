import pandas as pd
from pathlib import Path
root = Path("/Users/jiyunlee/Desktop/project/curvature")
tcga_path = root / "data_processed/tcga_clinical_core.parquet"
if tcga_path.exists():
    tcga_df = pd.read_parquet(tcga_path)
    print("TCGA clinical data shape:", tcga_df.shape)
    print("TCGA columns (sample):", tcga_df.columns[:20].tolist())
    print("LUAD samples:", (tcga_df["OncotreeLineage"].astype(str).str.upper() == "LUAD").sum())
    print("BRCA samples:", (tcga_df["OncotreeLineage"].astype(str).str.upper() == "BRCA").sum())
    
    overlap_path = root / "results/tables/phase13_cross_topology_families.parquet"
    overlap_df = pd.read_parquet(overlap_path)
    print("Overlap families to test:", len(overlap_df))
    for family in overlap_df["undirected_key"]:
        g1, g2 = family.split(":")
        if f"{g1}_mutation" in tcga_df.columns: print(f"Found mutation for {g1}")
        if f"{g2}_mutation" in tcga_df.columns: print(f"Found mutation for {g2}")
