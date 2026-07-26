#!/usr/bin/env python3
"""
Build tcga_clinical_core.parquet from raw TCGA data.

Reads:
  - data_external/tcga/TCGA-CDR-SupplementalTableS1.xlsx  (clinical endpoints)
  - data_external/tcga/mc3.v0.2.8.PUBLIC.maf.gz           (somatic mutations)
  - data_external/tcga/GDC-PANCAN.htseq_fpkm-uq.tsv      (expression, optional)

Writes:
  - data_processed/tcga_clinical_core.parquet

The output file is consumed by Phase 8 (Tier 1: TCGA Survival Cox PH Bridge)
in curvature_pipeline.py.
"""

import logging
import numpy as np
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("build_tcga_data")

ROOT = Path(__file__).resolve().parent

# Variant classification categories (following DepMap / MC3 conventions)
DAMAGING_CLASSES = {
    "Frame_Shift_Del", "Frame_Shift_Ins", "Nonsense_Mutation",
    "Splice_Site", "Translation_Start_Site", "Nonstop_Mutation",
}
HOTSPOT_CLASSES = {
    "Missense_Mutation", "In_Frame_Del", "In_Frame_Ins",
}
ALL_NONSILENT = DAMAGING_CLASSES | HOTSPOT_CLASSES


def _barcode_to_patient(barcode: str) -> str:
    """TCGA-XX-XXXX-01A-... → TCGA-XX-XXXX"""
    parts = str(barcode).split("-")
    if len(parts) >= 3:
        return "-".join(parts[:3])
    return barcode


def build_tcga_clinical_core():
    # Determine which genes we need mutations for
    overlap_path = ROOT / "results/tables/phase13_cross_topology_families.parquet"
    if not overlap_path.exists():
        logger.error("Cannot find overlap families. Run the main pipeline first.")
        return

    overlap = pd.read_parquet(overlap_path)
    mutation_genes = set()   # genes that appear as the mutation_gene in a family
    partner_genes = set()    # genes that appear as the partner_gene
    all_family_genes = set()

    for _, row in overlap.iterrows():
        mutation_genes.add(row["mutation_gene"])
        partner_genes.add(row["partner_gene"])
        g1, g2 = row["undirected_key"].split(":")
        all_family_genes.update([g1, g2])

    # Also add key driver genes used as covariates by run_survival_bridge
    covariate_genes = {"KRAS", "TP53"}
    genes_needing_mutation = all_family_genes | covariate_genes

    logger.info(f"Need mutation status for {len(genes_needing_mutation)} genes: {sorted(genes_needing_mutation)}")

    # Load TCGA CDR clinical data

    cdr_path = ROOT / "data_external/tcga/TCGA-CDR-SupplementalTableS1.xlsx"
    if not cdr_path.exists():
        logger.error(f"TCGA CDR file not found: {cdr_path}")
        return

    logger.info("Loading TCGA CDR clinical data...")
    cdr = pd.read_excel(cdr_path, sheet_name="TCGA-CDR")
    logger.info(f"  CDR shape: {cdr.shape}")

    # Build clean clinical DataFrame
    clinical = pd.DataFrame()
    clinical["sample_id"] = cdr["bcr_patient_barcode"].astype(str)
    clinical["OncotreeLineage"] = cdr["type"].astype(str)

    # Survival endpoints
    clinical["PFI"] = pd.to_numeric(cdr["PFI"], errors="coerce")
    clinical["PFI.time"] = pd.to_numeric(cdr["PFI.time"], errors="coerce")
    clinical["OS"] = pd.to_numeric(cdr["OS"], errors="coerce")
    clinical["OS.time"] = pd.to_numeric(cdr["OS.time"], errors="coerce")

    # Covariates expected by run_survival_bridge
    clinical["age"] = pd.to_numeric(cdr["age_at_initial_pathologic_diagnosis"], errors="coerce")
    clinical["gender"] = cdr["gender"].astype(str)

    # Stage: simplify AJCC staging to I/II/III/IV
    raw_stage = cdr["ajcc_pathologic_tumor_stage"].astype(str).str.upper()
    stage_map = {}
    for s in raw_stage.unique():
        if "IV" in s:
            stage_map[s] = "IV"
        elif "III" in s:
            stage_map[s] = "III"
        elif "II" in s:
            stage_map[s] = "II"
        elif "I" in s:
            stage_map[s] = "I"
        else:
            stage_map[s] = np.nan
    clinical["simplified_stage"] = raw_stage.map(stage_map)

    clinical = clinical.set_index("sample_id")
    logger.info(f"  Clinical base: {len(clinical)} patients, columns: {clinical.columns.tolist()}")

    # Parse MC3 MAF for somatic mutations
    maf_path = ROOT / "data_external/tcga/mc3.v0.2.8.PUBLIC.maf.gz"
    if not maf_path.exists():
        logger.error(f"MC3 MAF not found: {maf_path}")
        return

    logger.info("Loading MC3 MAF (this may take a minute for the 750 MB file)...")
    # Only load columns we need to save memory
    maf = pd.read_csv(
        maf_path, sep="\t", comment="#", low_memory=False,
        usecols=["Hugo_Symbol", "Variant_Classification", "Tumor_Sample_Barcode"]
    )
    logger.info(f"  MAF raw rows: {len(maf):,}")

    # Filter to non-silent mutations only
    maf = maf[maf["Variant_Classification"].isin(ALL_NONSILENT)].copy()
    logger.info(f"  After non-silent filter: {len(maf):,}")

    # Map barcode to patient ID
    maf["patient_id"] = maf["Tumor_Sample_Barcode"].apply(_barcode_to_patient)

    # Filter to genes we care about
    maf_filtered = maf[maf["Hugo_Symbol"].isin(genes_needing_mutation)].copy()
    logger.info(f"  Mutations in target genes: {len(maf_filtered):,}")

    # Build binary mutation matrix: patient × gene → 0/1
    mutation_pairs = maf_filtered[["patient_id", "Hugo_Symbol"]].drop_duplicates()
    mutation_pairs["mutated"] = 1
    mutation_matrix = mutation_pairs.pivot_table(
        index="patient_id", columns="Hugo_Symbol", values="mutated",
        aggfunc="max", fill_value=0
    )
    # Ensure all needed genes have columns (fill 0 for genes with no mutations)
    for gene in genes_needing_mutation:
        if gene not in mutation_matrix.columns:
            mutation_matrix[gene] = 0

    logger.info(f"  Mutation matrix: {mutation_matrix.shape[0]} patients × {mutation_matrix.shape[1]} genes")

    # Create {gene}_mutation columns
    mutation_df = pd.DataFrame(index=mutation_matrix.index)
    for gene in sorted(genes_needing_mutation):
        mutation_df[f"{gene}_mutation"] = mutation_matrix[gene].astype(int)

    # Also compute TMB (total non-silent mutation count per patient)
    tmb = maf.groupby("patient_id").size().rename("raw_TMB")
    mutation_df = mutation_df.join(tmb, how="left")
    mutation_df["raw_TMB"] = mutation_df["raw_TMB"].fillna(0)
    mutation_df["log_TMB"] = np.log1p(mutation_df["raw_TMB"])

    # Load expression data for partner genes
    expr_path = ROOT / "data_external/tcga/GDC-PANCAN.htseq_fpkm-uq.tsv"
    expr_df = pd.DataFrame()
    if expr_path.exists():
        logger.info("Loading GDC PanCan expression data (may take a moment)...")
        # This file is large. Read just the header to get sample columns, then
        # load only the rows we need.
        expr_raw = pd.read_csv(expr_path, sep="\t", index_col=0, nrows=0)
        sample_cols = expr_raw.columns.tolist()
        logger.info(f"  Expression matrix has {len(sample_cols)} samples")

        try:
            expr_raw = pd.read_csv(expr_path, sep="\t", index_col=0, low_memory=False)
            logger.info(f"  Expression matrix shape: {expr_raw.shape}")

            # Gene IDs are like ENSG00000141510.11 - need to strip version
            expr_raw.index = expr_raw.index.astype(str).str.split(".").str[0]

            partner_ensembl_map = {}
            known_map = {
                "ENSG00000168036": "CTNNB1",
                "ENSG00000135446": "CDK4",
                "ENSG00000169032": "MAP2K1",
                "ENSG00000134086": "VHL",
                "ENSG00000100393": "EP300",
                "ENSG00000005339": "CREBBP",
                "ENSG00000148737": "TCF7L2",
                "ENSG00000015676": "NUDCD3",
                "ENSG00000073756": "PTGS2",
                "ENSG00000109320": "NFKB1",
                "ENSG00000164362": "TERT",
                "ENSG00000127616": "SMARCA4",
                "ENSG00000080503": "SMARCA2",
                "ENSG00000091831": "ESR1",
                "ENSG00000171862": "PTEN",
                "ENSG00000141510": "TP53",
                "ENSG00000133703": "KRAS",
                "ENSG00000213281": "NRAS",
                "ENSG00000157764": "BRAF",
                "ENSG00000134982": "APC",
                "ENSG00000091831": "ESR1",
                "ENSG00000111186": "WDR35",
                "ENSG00000174574": "IL2",
                "ENSG00000147168": "IL2RG",
                "ENSG00000113328": "CCND1",
                "ENSG00000073756": "PTGS2",
                "ENSG00000168065": "IFT122",
                "ENSG00000144535": "DCP2",
                "ENSG00000114127": "XRN1",
                "ENSG00000170270": "AP3B2",
                "ENSG00000171680": "AP3M2",
                "ENSG00000113263": "ITGA6",
                "ENSG00000113163": "CD151",
                "ENSG00000108433": "SHOC2",
            }

            # Build expression for partner genes
            for ensembl_id, hugo in known_map.items():
                if hugo in partner_genes and ensembl_id in expr_raw.index:
                    partner_ensembl_map[ensembl_id] = hugo

            if partner_ensembl_map:
                expr_subset = expr_raw.loc[list(partner_ensembl_map.keys())].T
                expr_subset.columns = [f"{partner_ensembl_map[c]}_expression" for c in expr_subset.columns]
                # Map sample barcodes to patient IDs
                expr_subset.index = expr_subset.index.map(_barcode_to_patient)
                # Average duplicate patient entries (multiple aliquots)
                expr_subset = expr_subset.groupby(expr_subset.index).mean()
                # Log2 transform FPKM-UQ values
                expr_subset = np.log2(expr_subset + 1)
                expr_df = expr_subset
                logger.info(f"  Matched expression for {len(partner_ensembl_map)} partner genes")
            else:
                logger.warning("  Could not map any partner genes to expression data")
        except Exception as e:
            logger.warning(f"  Failed to load expression data: {e}. Continuing without it.")
    else:
        logger.info("  Expression data not found. Continuing without it (optional).")

    # Merge everything and save
    logger.info("Merging clinical + mutations + expression...")
    result = clinical.join(mutation_df, how="left")

    if not expr_df.empty:
        result = result.join(expr_df, how="left")

    # Fill missing mutation values with 0 (patient not in MAF → wildtype)
    mut_cols = [c for c in result.columns if c.endswith("_mutation")]
    result[mut_cols] = result[mut_cols].fillna(0).astype(int)

    # Drop patients with no survival data
    result = result.dropna(subset=["PFI.time", "PFI"])
    result = result.reset_index().rename(columns={"index": "sample_id"})

    logger.info(f"Final TCGA clinical core: {result.shape}")
    logger.info(f"  Columns: {result.columns.tolist()}")

    # Sanity checks
    for hist in ["LUAD", "BRCA"]:
        subset = result[result["OncotreeLineage"] == hist]
        logger.info(f"  {hist}: {len(subset)} patients")
        for gene in sorted(genes_needing_mutation):
            n_mut = int(subset[f"{gene}_mutation"].sum())
            if n_mut > 0:
                logger.info(f"    {gene}: {n_mut} mutated")

    out_path = ROOT / "data_processed/tcga_clinical_core.parquet"
    result.to_parquet(out_path, index=False)
    logger.info(f"Saved to {out_path}")


if __name__ == "__main__":
    build_tcga_clinical_core()
