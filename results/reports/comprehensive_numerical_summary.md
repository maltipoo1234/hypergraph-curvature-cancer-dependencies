# Hypergraph Curvature Pipeline: Comprehensive Numerical Summary

- **Generated On:** 2026-06-26 21:01:06
- **Total Input Files Processed:** 39
- **Target Purpose:** Direct manuscript results writing and statistical verification.

## Table of Contents
1. [all_discovery_validation_heldout.parquet](#file-all_discovery_validation_heldout-parquet)
2. [all_systematic_discovery_pairs.parquet](#file-all_systematic_discovery_pairs-parquet)
3. [candidate_dependency_pairs.parquet](#file-candidate_dependency_pairs-parquet)
4. [continuous_validation_meta_overview.parquet](#file-continuous_validation_meta_overview-parquet)
5. [corum_family_pair_summary.parquet](#file-corum_family_pair_summary-parquet)
6. [degree_matched_permutation_summary.parquet](#file-degree_matched_permutation_summary-parquet)
7. [depmap_25q3_continuous_meta_summary.parquet](#file-depmap_25q3_continuous_meta_summary-parquet)
8. [depmap_25q3_leave_one_out.parquet](#file-depmap_25q3_leave_one_out-parquet)
9. [graph_metric_benchmark_best.parquet](#file-graph_metric_benchmark_best-parquet)
10. [graph_metric_benchmark_pairs.parquet](#file-graph_metric_benchmark_pairs-parquet)
11. [graph_metric_benchmark_summary.parquet](#file-graph_metric_benchmark_summary-parquet)
12. [phase13_cross_topology_families.parquet](#file-phase13_cross_topology_families-parquet)
13. [phase13_degree_preserving_shuffle_summary.parquet](#file-phase13_degree_preserving_shuffle_summary-parquet)
14. [phase13_external_cmp_sanger_summary.parquet](#file-phase13_external_cmp_sanger_summary-parquet)
15. [phase13_external_cmp_sanger_validation.parquet](#file-phase13_external_cmp_sanger_validation-parquet)
16. [phase13_external_depmap25q3_summary.parquet](#file-phase13_external_depmap25q3_summary-parquet)
17. [phase13_external_depmap25q3_validation.parquet](#file-phase13_external_depmap25q3_validation-parquet)
18. [phase13_family_dependency_stats.parquet](#file-phase13_family_dependency_stats-parquet)
19. [phase14_benchmark_universe.parquet](#file-phase14_benchmark_universe-parquet)
20. [phase17_tcga_patient_bridge.parquet](#file-phase17_tcga_patient_bridge-parquet)
21. [phase25_prism_cdks_validation.parquet](#file-phase25_prism_cdks_validation-parquet)
22. [phase25_prism_mek_validation.parquet](#file-phase25_prism_mek_validation-parquet)
23. [prism_pharmacologic_validation.parquet](#file-prism_pharmacologic_validation-parquet)
24. [robustness_summary.csv](#file-robustness_summary-csv)
25. [sanger_cohort_validation.parquet](#file-sanger_cohort_validation-parquet)
26. [sanger_continuous_meta_summary.parquet](#file-sanger_continuous_meta_summary-parquet)
27. [sanger_leave_one_out.parquet](#file-sanger_leave_one_out-parquet)
28. [sensitivity_backbone_off_summary.parquet](#file-sensitivity_backbone_off_summary-parquet)
29. [sensitivity_backbone_on_summary.parquet](#file-sensitivity_backbone_on_summary-parquet)
30. [string_family_pair_summary.parquet](#file-string_family_pair_summary-parquet)
31. [tcga_bridge_leave_one_family_out.parquet](#file-tcga_bridge_leave_one_family_out-parquet)
32. [tcga_bridge_meta_summary.parquet](#file-tcga_bridge_meta_summary-parquet)
33. [tcga_bridge_tumor_type_meta.parquet](#file-tcga_bridge_tumor_type_meta-parquet)
34. [tcga_schoenfeld_diagnostics.parquet](#file-tcga_schoenfeld_diagnostics-parquet)
35. [tcga_survival_validation.parquet](#file-tcga_survival_validation-parquet)
36. [tight_null_framework_summary.parquet](#file-tight_null_framework_summary-parquet)
37. [tight_null_lofo_fragility.parquet](#file-tight_null_lofo_fragility-parquet)
38. [trrust_family_pair_summary.parquet](#file-trrust_family_pair_summary-parquet)
39. [validation_candidate_dependency_pairs.parquet](#file-validation_candidate_dependency_pairs-parquet)

---

## File: all_discovery_validation_heldout.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/all_discovery_validation_heldout.parquet`
- **Matrix Dimensions:** 96260 rows × 12 columns

### 1. Data Schema & Quality Audit

| Column Name               | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------------|:--------|-----------------:|-------------:|:---------|
| mutation_gene             | object  |            96260 |            0 | 0.00%    |
| partner_gene              | object  |            96260 |            0 | 0.00%    |
| mutation_type             | object  |            96260 |            0 | 0.00%    |
| num_mutant_models         | int64   |            96260 |            0 | 0.00%    |
| num_wildtype_models       | int64   |            96260 |            0 | 0.00%    |
| delta_dependency          | float64 |            96260 |            0 | 0.00%    |
| p_value                   | float64 |            96260 |            0 | 0.00%    |
| fdr                       | float64 |            96260 |            0 | 0.00%    |
| passes_main_thresholds    | bool    |            96260 |            0 | 0.00%    |
| topology                  | object  |            96260 |            0 | 0.00%    |
| undirected_key            | object  |            96260 |            0 | 0.00%    |
| passes_validation_nominal | bool    |            96260 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                           |   count | unique   | top        | freq   | mean       | std       | min       | 25%        | 50%        | 75%        | max        |
|:--------------------------|--------:|:---------|:-----------|:-------|:-----------|:----------|:----------|:-----------|:-----------|:-----------|:-----------|
| mutation_gene             |   96260 | 776      | TP53       | 2848   | —          | —         | —         | —          | —          | —          | —          |
| partner_gene              |   96260 | 6317     | MYC        | 217    | —          | —         | —         | —          | —          | —          | —          |
| mutation_type             |   96260 | 2        | damaging   | 81446  | —          | —         | —         | —          | —          | —          | —          |
| num_mutant_models         |   96260 | —        | —          | —      | 14.042302  | 37.842272 | 3.000000  | 3.000000   | 4.000000   | 7.000000   | 246.000000 |
| num_wildtype_models       |   96260 | —        | —          | —      | 425.870445 | 41.556841 | 12.000000 | 433.000000 | 437.000000 | 438.000000 | 438.000000 |
| delta_dependency          |   96260 | —        | —          | —      | 0.000143   | 0.111691  | -1.613158 | -0.044721  | 0.000217   | 0.046525   | 1.469538   |
| p_value                   |   96260 | —        | —          | —      | 0.465135   | 0.292746  | 0.000000  | 0.207822   | 0.451780   | 0.714247   | 0.999993   |
| fdr                       |   96260 | —        | —          | —      | 0.859742   | 0.157742  | 0.000000  | 0.831956   | 0.903412   | 0.952816   | 0.999996   |
| passes_main_thresholds    |   96260 | 2        | False      | 96168  | —          | —         | —         | —          | —          | —          | —          |
| topology                  |   96260 | 3        | trrust     | 72411  | —          | —         | —         | —          | —          | —          | —          |
| undirected_key            |   96260 | 75337    | EP300:TP53 | 12     | —          | —         | —         | —          | —          | —          | —          |
| passes_validation_nominal |   96260 | 2        | False      | 93150  | —          | —         | —         | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |            81446 | 84.61%                  |
| hotspot          |            14814 | 15.39%                  |

**Column Grouping: `passes_main_thresholds`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |            96168 | 99.9%                   |
| True             |               92 | 0.1%                    |

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| trrust           |            72411 | 75.22%                  |
| string           |            17613 | 18.3%                   |
| corum            |             6236 | 6.48%                   |

**Column Grouping: `passes_validation_nominal`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |            93150 | 96.77%                  |
| True             |             3110 | 3.23%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **7433** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| FOXA1           | NFKB1          | damaging        |                   3 |                   438 |          -0.184666 |         0 |     0 | False                    | trrust     | FOXA1:NFKB1      | True                        |
| EGFR            | ELF4           | damaging        |                   3 |                   438 |          -0.182387 |         0 |     0 | False                    | trrust     | EGFR:ELF4        | True                        |
| BRCA1           | TP53           | damaging        |                   3 |                   438 |          -0.654914 |         0 |     0 | True                     | string     | BRCA1:TP53       | True                        |
| BRCA1           | TP53           | damaging        |                   3 |                   438 |          -0.654914 |         0 |     0 | True                     | trrust     | BRCA1:TP53       | True                        |
| SREBF1          | B4GALT1        | damaging        |                   4 |                   437 |           0.150989 |         0 |     0 | False                    | trrust     | B4GALT1:SREBF1   | False                       |

- 💡 **Significance Hit:** Column `fdr` contains **673** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| FOXA1           | NFKB1          | damaging        |                   3 |                   438 |          -0.184666 |         0 |     0 | False                    | trrust     | FOXA1:NFKB1      | True                        |
| EGFR            | ELF4           | damaging        |                   3 |                   438 |          -0.182387 |         0 |     0 | False                    | trrust     | EGFR:ELF4        | True                        |
| BRCA1           | TP53           | damaging        |                   3 |                   438 |          -0.654914 |         0 |     0 | True                     | string     | BRCA1:TP53       | True                        |
| BRCA1           | TP53           | damaging        |                   3 |                   438 |          -0.654914 |         0 |     0 | True                     | trrust     | BRCA1:TP53       | True                        |
| SREBF1          | B4GALT1        | damaging        |                   4 |                   437 |           0.150989 |         0 |     0 | False                    | trrust     | B4GALT1:SREBF1   | False                       |


### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|---------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| ABCA1           | ABCA12         | damaging        |                   9 |                   432 |          -0.01794  |  0.720097 | 0.953402 | False                    | corum      | ABCA1:ABCA12     | False                       |
| ABCA1           | COPS2          | damaging        |                   9 |                   432 |          -0.003967 |  0.967126 | 0.993247 | False                    | corum      | ABCA1:COPS2      | False                       |
| ABCA1           | COPS5          | damaging        |                   9 |                   432 |           0.033787 |  0.683445 | 0.950058 | False                    | corum      | ABCA1:COPS5      | False                       |
| ABCA1           | FLOT1          | damaging        |                   9 |                   432 |           0.08007  |  0.169769 | 0.829035 | False                    | corum      | ABCA1:FLOT1      | False                       |
| ABCA1           | NR1H2          | damaging        |                   9 |                   432 |           0.0533   |  0.359389 | 0.888287 | False                    | corum      | ABCA1:NR1H2      | False                       |
| ABCA1           | SNTB2          | damaging        |                   9 |                   432 |           0.076195 |  0.202236 | 0.846973 | False                    | corum      | ABCA1:SNTB2      | False                       |
| ABCA1           | STX12          | damaging        |                   9 |                   432 |          -0.011368 |  0.808992 | 0.970355 | False                    | corum      | ABCA1:STX12      | False                       |
| ABCA1           | UGP2           | damaging        |                   9 |                   432 |          -0.024843 |  0.60516  | 0.932027 | False                    | corum      | ABCA1:UGP2       | False                       |
| ABCA12          | ABCA1          | damaging        |                  11 |                   430 |          -0.046231 |  0.23544  | 0.859101 | False                    | corum      | ABCA1:ABCA12     | False                       |
| ABCA12          | NR1H2          | damaging        |                  11 |                   430 |          -0.069802 |  0.098615 | 0.744506 | False                    | corum      | ABCA12:NR1H2     | False                       |
| ABCB1           | ANXA2          | damaging        |                   5 |                   436 |          -0.028348 |  0.162199 | 0.822335 | False                    | corum      | ABCB1:ANXA2      | False                       |
| ABCB1           | PPP2R3C        | damaging        |                   5 |                   436 |          -0.028707 |  0.767531 | 0.958223 | False                    | corum      | ABCB1:PPP2R3C    | False                       |
| ABCB1           | RACK1          | damaging        |                   5 |                   436 |           0.397893 |  0.069446 | 0.689596 | False                    | corum      | ABCB1:RACK1      | False                       |
| ABCB1           | SRC            | damaging        |                   5 |                   436 |           0.059231 |  0.598515 | 0.929599 | False                    | corum      | ABCB1:SRC        | False                       |
| ABCB1           | TFPI2          | damaging        |                   5 |                   436 |           0.120074 |  0.038923 | 0.603789 | False                    | corum      | ABCB1:TFPI2      | False                       |
| ABCC9           | KCNJ11         | damaging        |                   5 |                   436 |          -0.112784 |  0.261475 | 0.860452 | False                    | corum      | ABCC9:KCNJ11     | False                       |
| ABCC9           | LDHA           | damaging        |                   5 |                   436 |          -0.023807 |  0.811507 | 0.970199 | False                    | corum      | ABCC9:LDHA       | False                       |
| ABL1            | ABI1           | damaging        |                   3 |                   438 |           0.033805 |  0.831618 | 0.974257 | False                    | corum      | ABI1:ABL1        | False                       |
| ABL1            | BCAR1          | damaging        |                   3 |                   438 |          -0.157888 |  0.464481 | 0.912572 | False                    | corum      | ABL1:BCAR1       | False                       |
| ABL1            | BCR            | damaging        |                   3 |                   438 |           0.096606 |  0.239232 | 0.860848 | False                    | corum      | ABL1:BCR         | False                       |
| ABL1            | CBL            | damaging        |                   3 |                   438 |          -0.043366 |  0.086605 | 0.722981 | False                    | corum      | ABL1:CBL         | False                       |
| ABL1            | CTTN           | damaging        |                   3 |                   438 |          -0.112827 |  0.007616 | 0.389266 | False                    | corum      | ABL1:CTTN        | True                        |
| ABL1            | GRB2           | damaging        |                   3 |                   438 |           0.235047 |  0.580307 | 0.925996 | False                    | corum      | ABL1:GRB2        | False                       |
| ABL1            | MAD2L1         | damaging        |                   3 |                   438 |           0.010425 |  0.910935 | 0.98707  | False                    | corum      | ABL1:MAD2L1      | False                       |
| ABL1            | MAP2K1         | damaging        |                   3 |                   438 |           0.036061 |  0.452744 | 0.906942 | False                    | corum      | ABL1:MAP2K1      | False                       |
| ABL1            | MAP2K2         | damaging        |                   3 |                   438 |          -0.069854 |  0.579402 | 0.926212 | False                    | corum      | ABL1:MAP2K2      | False                       |
| ABL1            | MYLK           | damaging        |                   3 |                   438 |           0.10156  |  0.220442 | 0.853307 | False                    | corum      | ABL1:MYLK        | False                       |
| ABL1            | NUP155         | damaging        |                   3 |                   438 |          -0.019268 |  0.335663 | 0.886946 | False                    | corum      | ABL1:NUP155      | False                       |
| ABL1            | NUP214         | damaging        |                   3 |                   438 |           0.084703 |  0.616099 | 0.936387 | False                    | corum      | ABL1:NUP214      | False                       |
| ABL1            | SHC1           | damaging        |                   3 |                   438 |           0.12976  |  0.117828 | 0.796938 | False                    | corum      | ABL1:SHC1        | False                       |
| ABL1            | SMC4           | damaging        |                   3 |                   438 |           0.100218 |  0.65674  | 0.943648 | False                    | corum      | ABL1:SMC4        | False                       |
| ABL1            | STAT1          | damaging        |                   3 |                   438 |          -0.028157 |  0.032982 | 0.568166 | False                    | corum      | ABL1:STAT1       | True                        |
| ABL2            | HRAS           | damaging        |                   5 |                   436 |          -0.066005 |  0.507108 | 0.917947 | False                    | corum      | ABL2:HRAS        | False                       |
| ABL2            | RIN1           | damaging        |                   5 |                   436 |           0.012755 |  0.751242 | 0.957048 | False                    | corum      | ABL2:RIN1        | False                       |
| ABRAXAS2        | BABAM1         | damaging        |                   3 |                   438 |           0.077309 |  0.273511 | 0.862292 | False                    | corum      | ABRAXAS2:BABAM1  | False                       |
| ABRAXAS2        | BABAM2         | damaging        |                   3 |                   438 |           0.026072 |  0.79709  | 0.967054 | False                    | corum      | ABRAXAS2:BABAM2  | False                       |
| ABRAXAS2        | BRCC3          | damaging        |                   3 |                   438 |          -0.088398 |  0.320335 | 0.874228 | False                    | corum      | ABRAXAS2:BRCC3   | False                       |
| ACAP1           | CLTC           | damaging        |                   3 |                   438 |          -0.02176  |  0.941525 | 0.988276 | False                    | corum      | ACAP1:CLTC       | False                       |
| ACAP1           | SLC2A4         | damaging        |                   3 |                   438 |           0.010943 |  0.803587 | 0.969653 | False                    | corum      | ACAP1:SLC2A4     | False                       |
| ACE             | HSPA2          | damaging        |                   4 |                   437 |          -0.078813 |  0.551074 | 0.923541 | False                    | corum      | ACE:HSPA2        | False                       |


*... [Truncated 96180 standard row items inline] ...*

**Last 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|---------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| ZEB1            | RUNX2          | damaging        |                   5 |                   436 |           0.076514 |  0.377852 | 0.888939 | False                    | trrust     | RUNX2:ZEB1       | False                       |
| ZEB1            | S100A4         | damaging        |                   5 |                   436 |           0.013143 |  0.757275 | 0.960603 | False                    | trrust     | S100A4:ZEB1      | False                       |
| ZEB1            | SALL4          | damaging        |                   5 |                   436 |           0.05848  |  0.040405 | 0.61311  | False                    | trrust     | SALL4:ZEB1       | False                       |
| ZEB1            | SERPINB9       | damaging        |                   5 |                   436 |          -0.001245 |  0.983564 | 0.997407 | False                    | trrust     | SERPINB9:ZEB1    | False                       |
| ZEB1            | SERPINE1       | damaging        |                   5 |                   436 |           0.055887 |  0.125014 | 0.777566 | False                    | trrust     | SERPINE1:ZEB1    | False                       |
| ZEB1            | SLC9A2         | damaging        |                   5 |                   436 |          -0.065737 |  0.092103 | 0.739386 | False                    | trrust     | SLC9A2:ZEB1      | False                       |
| ZEB1            | SLCO4C1        | damaging        |                   5 |                   436 |          -0.04195  |  0.014936 | 0.448583 | False                    | trrust     | SLCO4C1:ZEB1     | True                        |
| ZEB1            | SMAD4          | damaging        |                   5 |                   436 |          -0.096716 |  0.246089 | 0.847945 | False                    | trrust     | SMAD4:ZEB1       | False                       |
| ZEB1            | SOX4           | damaging        |                   5 |                   436 |           0.013809 |  0.693699 | 0.950219 | False                    | trrust     | SOX4:ZEB1        | False                       |
| ZEB1            | SP1            | damaging        |                   5 |                   436 |          -0.105676 |  0.470345 | 0.906574 | False                    | trrust     | SP1:ZEB1         | False                       |
| ZEB1            | SPP1           | damaging        |                   5 |                   436 |           0.049865 |  0.474133 | 0.907378 | False                    | trrust     | SPP1:ZEB1        | False                       |
| ZEB1            | STAT4          | damaging        |                   5 |                   436 |           0.034545 |  0.130081 | 0.783768 | False                    | trrust     | STAT4:ZEB1       | False                       |
| ZEB1            | TAC3           | damaging        |                   5 |                   436 |          -0.117185 |  0.184245 | 0.816987 | False                    | trrust     | TAC3:ZEB1        | False                       |
| ZEB1            | TBXAS1         | damaging        |                   5 |                   436 |           0.086048 |  0.065765 | 0.69106  | False                    | trrust     | TBXAS1:ZEB1      | False                       |
| ZEB1            | TCF7L2         | damaging        |                   5 |                   436 |           0.129499 |  0.017917 | 0.4798   | False                    | trrust     | TCF7L2:ZEB1      | False                       |
| ZEB1            | TDRD1          | damaging        |                   5 |                   436 |          -0.065427 |  0.325251 | 0.876898 | False                    | trrust     | TDRD1:ZEB1       | False                       |
| ZEB1            | TEK            | damaging        |                   5 |                   436 |           0.038625 |  0.353004 | 0.883285 | False                    | trrust     | TEK:ZEB1         | False                       |
| ZEB1            | TERT           | damaging        |                   5 |                   436 |          -0.029846 |  0.715427 | 0.953907 | False                    | trrust     | TERT:ZEB1        | False                       |
| ZEB1            | TFF1           | damaging        |                   5 |                   436 |          -0.032855 |  0.455496 | 0.90431  | False                    | trrust     | TFF1:ZEB1        | False                       |
| ZEB1            | TFF3           | damaging        |                   5 |                   436 |          -0.021431 |  0.568829 | 0.928862 | False                    | trrust     | TFF3:ZEB1        | False                       |
| ZEB1            | TGFA           | damaging        |                   5 |                   436 |          -0.123665 |  0.038413 | 0.610659 | False                    | trrust     | TGFA:ZEB1        | True                        |
| ZEB1            | TGFBR3         | damaging        |                   5 |                   436 |           0.03487  |  0.459103 | 0.905143 | False                    | trrust     | TGFBR3:ZEB1      | False                       |
| ZEB1            | THBD           | damaging        |                   5 |                   436 |          -0.048467 |  0.242744 | 0.846652 | False                    | trrust     | THBD:ZEB1        | False                       |
| ZEB1            | TMPRSS2        | damaging        |                   5 |                   436 |          -0.078498 |  0.409241 | 0.895597 | False                    | trrust     | TMPRSS2:ZEB1     | False                       |
| ZEB1            | TP53           | damaging        |                   5 |                   436 |          -0.227465 |  0.330173 | 0.878364 | False                    | trrust     | TP53:ZEB1        | False                       |
| ZEB1            | TP73           | damaging        |                   5 |                   436 |           0.062518 |  0.594747 | 0.93322  | False                    | trrust     | TP73:ZEB1        | False                       |
| ZEB1            | TRIM22         | damaging        |                   5 |                   436 |          -0.008581 |  0.809112 | 0.970202 | False                    | trrust     | TRIM22:ZEB1      | False                       |
| ZEB1            | TYMS           | damaging        |                   5 |                   436 |           0.317893 |  0.247636 | 0.849114 | False                    | trrust     | TYMS:ZEB1        | False                       |
| ZEB1            | UGT1A4         | damaging        |                   5 |                   436 |           0.150221 |  0.054597 | 0.6621   | False                    | trrust     | UGT1A4:ZEB1      | False                       |
| ZEB1            | UGT2B15        | damaging        |                   5 |                   436 |          -0.048847 |  0.329404 | 0.878091 | False                    | trrust     | UGT2B15:ZEB1     | False                       |
| ZEB1            | VCAM1          | damaging        |                   5 |                   436 |           0.121142 |  0.010723 | 0.389595 | False                    | trrust     | VCAM1:ZEB1       | False                       |
| ZEB1            | VEGFA          | damaging        |                   5 |                   436 |           0.012697 |  0.783972 | 0.966153 | False                    | trrust     | VEGFA:ZEB1       | False                       |
| ZEB1            | VIM            | damaging        |                   5 |                   436 |           0.039625 |  0.260222 | 0.855447 | False                    | trrust     | VIM:ZEB1         | False                       |
| ZEB1            | VWF            | damaging        |                   5 |                   436 |          -0.033548 |  0.468726 | 0.906058 | False                    | trrust     | VWF:ZEB1         | False                       |
| ZEB1            | WNT11          | damaging        |                   5 |                   436 |          -0.059967 |  0.599376 | 0.933625 | False                    | trrust     | WNT11:ZEB1       | False                       |
| ZEB1            | WT1            | damaging        |                   5 |                   436 |          -0.004912 |  0.920942 | 0.987887 | False                    | trrust     | WT1:ZEB1         | False                       |
| ZEB1            | YWHAQ          | damaging        |                   5 |                   436 |          -0.000501 |  0.990173 | 0.998432 | False                    | trrust     | YWHAQ:ZEB1       | False                       |
| ZEB1            | YY1            | damaging        |                   5 |                   436 |           0.08047  |  0.301747 | 0.869921 | False                    | trrust     | YY1:ZEB1         | False                       |
| ZEB1            | ZEB2           | damaging        |                   5 |                   436 |           0.254487 |  0.004804 | 0.270299 | False                    | trrust     | ZEB1:ZEB2        | False                       |
| ZEB1            | ZFHX3          | damaging        |                   5 |                   420 |           0.011521 |  0.793229 | 0.968347 | False                    | trrust     | ZEB1:ZFHX3       | False                       |


---

## File: all_systematic_discovery_pairs.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/all_systematic_discovery_pairs.parquet`
- **Matrix Dimensions:** 162060 rows × 11 columns

### 1. Data Schema & Quality Audit

| Column Name            | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------------|:--------|-----------------:|-------------:|:---------|
| mutation_gene          | object  |           162060 |            0 | 0.00%    |
| partner_gene           | object  |           162060 |            0 | 0.00%    |
| mutation_type          | object  |           162060 |            0 | 0.00%    |
| num_mutant_models      | int64   |           162060 |            0 | 0.00%    |
| num_wildtype_models    | int64   |           162060 |            0 | 0.00%    |
| delta_dependency       | float64 |           162060 |            0 | 0.00%    |
| p_value                | float64 |           162060 |            0 | 0.00%    |
| fdr                    | float64 |           162060 |            0 | 0.00%    |
| passes_main_thresholds | bool    |           162060 |            0 | 0.00%    |
| topology               | object  |           162060 |            0 | 0.00%    |
| undirected_key         | object  |           162060 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                        |   count | unique   | top        | freq   | mean       | std       | min       | 25%        | 50%        | 75%        | max        |
|:-----------------------|--------:|:---------|:-----------|:-------|:-----------|:----------|:----------|:-----------|:-----------|:-----------|:-----------|
| mutation_gene          |  162060 | 1407     | TP53       | 2848   | —          | —         | —         | —          | —          | —          | —          |
| partner_gene           |  162060 | 7399     | TP53       | 340    | —          | —         | —         | —          | —          | —          | —          |
| mutation_type          |  162060 | 2        | damaging   | 139271 | —          | —         | —         | —          | —          | —          | —          |
| num_mutant_models      |  162060 | —        | —          | —      | 18.027515  | 64.479636 | 3.000000  | 3.000000   | 5.000000   | 8.000000   | 534.000000 |
| num_wildtype_models    |  162060 | —        | —          | —      | 745.902585 | 73.315291 | 22.000000 | 758.000000 | 762.000000 | 764.000000 | 764.000000 |
| delta_dependency       |  162060 | —        | —          | —      | -0.001485  | 0.112924  | -2.411054 | -0.043252  | 0.001261   | 0.045809   | 1.429472   |
| p_value                |  162060 | —        | —          | —      | 0.472846   | 0.290732  | 0.000000  | 0.219914   | 0.460101   | 0.721246   | 0.999994   |
| fdr                    |  162060 | —        | —          | —      | 0.894244   | 0.125606  | 0.000000  | 0.879984   | 0.920325   | 0.961547   | 1.000000   |
| passes_main_thresholds |  162060 | 2        | False      | 161991 | —          | —         | —         | —          | —          | —          | —          |
| topology               |  162060 | 3        | trrust     | 120258 | —          | —         | —         | —          | —          | —          | —          |
| undirected_key         |  162060 | 120600   | EP300:TP53 | 12     | —          | —         | —         | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |           139271 | 85.94%                  |
| hotspot          |            22789 | 14.06%                  |

**Column Grouping: `passes_main_thresholds`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |           161991 | 99.96%                  |
| True             |               69 | 0.04%                   |

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| trrust           |           120258 | 74.21%                  |
| string           |            31258 | 19.29%                  |
| corum            |            10544 | 6.51%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **10885** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|
| TYMS            | HSF1           | damaging        |                   3 |                   764 |           0.341246 |         0 |     0 | False                    | trrust     | HSF1:TYMS        |
| SIRT1           | IRF9           | damaging        |                   3 |                   764 |          -0.185377 |         0 |     0 | False                    | trrust     | IRF9:SIRT1       |
| LDLR            | BACE1          | damaging        |                   3 |                   764 |           0.091326 |         0 |     0 | False                    | trrust     | BACE1:LDLR       |
| XIAP            | CDH11          | damaging        |                   3 |                   764 |           0.133384 |         0 |     0 | False                    | trrust     | CDH11:XIAP       |
| GSK3B           | BCL3           | damaging        |                   3 |                   764 |           0.131565 |         0 |     0 | False                    | trrust     | BCL3:GSK3B       |

- 💡 **Significance Hit:** Column `fdr` contains **645** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|
| TYMS            | HSF1           | damaging        |                   3 |                   764 |           0.341246 |         0 |     0 | False                    | trrust     | HSF1:TYMS        |
| SIRT1           | IRF9           | damaging        |                   3 |                   764 |          -0.185377 |         0 |     0 | False                    | trrust     | IRF9:SIRT1       |
| XIAP            | CDH11          | damaging        |                   3 |                   764 |           0.133384 |         0 |     0 | False                    | trrust     | CDH11:XIAP       |
| LDLR            | BACE1          | damaging        |                   3 |                   764 |           0.091326 |         0 |     0 | False                    | trrust     | BACE1:LDLR       |
| GSK3B           | BCL3           | damaging        |                   3 |                   764 |           0.131565 |         0 |     0 | False                    | trrust     | BCL3:GSK3B       |


### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|---------:|:-------------------------|:-----------|:-----------------|
| ABCA1           | ABCA12         | damaging        |                   3 |                   764 |          -0.015171 |  0.069171 | 0.744979 | False                    | corum      | ABCA1:ABCA12     |
| ABCA1           | COPS2          | damaging        |                   3 |                   764 |          -0.184398 |  0.298858 | 0.88765  | False                    | corum      | ABCA1:COPS2      |
| ABCA1           | COPS5          | damaging        |                   3 |                   764 |          -0.083638 |  0.865929 | 0.978707 | False                    | corum      | ABCA1:COPS5      |
| ABCA1           | FLOT1          | damaging        |                   3 |                   764 |           0.184781 |  0.271279 | 0.886112 | False                    | corum      | ABCA1:FLOT1      |
| ABCA1           | NR1H2          | damaging        |                   3 |                   764 |           0.206796 |  0.232517 | 0.874033 | False                    | corum      | ABCA1:NR1H2      |
| ABCA1           | SNTB2          | damaging        |                   3 |                   764 |           0.131354 |  0.160539 | 0.851045 | False                    | corum      | ABCA1:SNTB2      |
| ABCA1           | STX12          | damaging        |                   3 |                   764 |          -0.080654 |  0.227369 | 0.873364 | False                    | corum      | ABCA1:STX12      |
| ABCA1           | UGP2           | damaging        |                   3 |                   764 |          -0.204776 |  0.411356 | 0.906446 | False                    | corum      | ABCA1:UGP2       |
| ABCA12          | ABCA1          | damaging        |                  21 |                   746 |          -0.016631 |  0.483409 | 0.917068 | False                    | corum      | ABCA1:ABCA12     |
| ABCA12          | NR1H2          | damaging        |                  21 |                   746 |          -0.041697 |  0.234994 | 0.878021 | False                    | corum      | ABCA12:NR1H2     |
| ABCB1           | ANXA2          | damaging        |                   7 |                   760 |           0.006409 |  0.635005 | 0.942629 | False                    | corum      | ABCB1:ANXA2      |
| ABCB1           | PPP2R3C        | damaging        |                   7 |                   760 |           0.107615 |  0.400576 | 0.904815 | False                    | corum      | ABCB1:PPP2R3C    |
| ABCB1           | RACK1          | damaging        |                   7 |                   760 |           0.064394 |  0.837368 | 0.972915 | False                    | corum      | ABCB1:RACK1      |
| ABCB1           | SRC            | damaging        |                   7 |                   760 |          -0.06791  |  0.402947 | 0.904935 | False                    | corum      | ABCB1:SRC        |
| ABCB1           | TFPI2          | damaging        |                   7 |                   760 |          -0.055365 |  0.082463 | 0.777722 | False                    | corum      | ABCB1:TFPI2      |
| ABCC9           | KCNJ11         | damaging        |                  17 |                   750 |           0.027765 |  0.324415 | 0.889399 | False                    | corum      | ABCC9:KCNJ11     |
| ABCC9           | LDHA           | damaging        |                  17 |                   750 |           0.01143  |  0.839845 | 0.97322  | False                    | corum      | ABCC9:LDHA       |
| ABCE1           | HBS1L          | damaging        |                   8 |                   759 |          -0.119914 |  0.149875 | 0.844167 | False                    | corum      | ABCE1:HBS1L      |
| ABCE1           | PELO           | damaging        |                   8 |                   759 |          -1.00915  |  0.014229 | 0.512058 | False                    | corum      | ABCE1:PELO       |
| ABI1            | ABL1           | damaging        |                   3 |                   764 |          -0.034648 |  0.397453 | 0.904542 | False                    | corum      | ABI1:ABL1        |
| ABI1            | BCAR1          | damaging        |                   3 |                   764 |           0.036277 |  0.062594 | 0.73089  | False                    | corum      | ABI1:BCAR1       |
| ABI1            | BRK1           | damaging        |                   3 |                   764 |           0.219681 |  0.042952 | 0.682049 | False                    | corum      | ABI1:BRK1        |
| ABI1            | CYFIP1         | damaging        |                   3 |                   764 |           0.182011 |  0.185614 | 0.864068 | False                    | corum      | ABI1:CYFIP1      |
| ABI1            | EPS8           | damaging        |                   3 |                   764 |           0.025297 |  0.723232 | 0.956448 | False                    | corum      | ABI1:EPS8        |
| ABI1            | EPS8L1         | damaging        |                   3 |                   764 |           0.086672 |  0.275836 | 0.88671  | False                    | corum      | ABI1:EPS8L1      |
| ABI1            | EPS8L2         | damaging        |                   3 |                   764 |          -0.023809 |  0.698419 | 0.952915 | False                    | corum      | ABI1:EPS8L2      |
| ABI1            | EPS8L3         | damaging        |                   3 |                   764 |          -0.06695  |  0.311847 | 0.890848 | False                    | corum      | ABI1:EPS8L3      |
| ABI1            | NCKAP1         | damaging        |                   3 |                   764 |           0.284496 |  0.156074 | 0.847394 | False                    | corum      | ABI1:NCKAP1      |
| ABI1            | SOS1           | damaging        |                   3 |                   764 |           0.001709 |  0.994724 | 0.998988 | False                    | corum      | ABI1:SOS1        |
| ABI1            | WASF2          | damaging        |                   3 |                   764 |           0.026358 |  0.849974 | 0.975416 | False                    | corum      | ABI1:WASF2       |
| ABL1            | ABI1           | damaging        |                   3 |                   764 |           0.044333 |  0.221987 | 0.872068 | False                    | corum      | ABI1:ABL1        |
| ABL1            | BCAR1          | damaging        |                   3 |                   764 |           0.010929 |  0.911283 | 0.983678 | False                    | corum      | ABL1:BCAR1       |
| ABL1            | BCR            | damaging        |                   3 |                   764 |           0.031126 |  0.695189 | 0.953071 | False                    | corum      | ABL1:BCR         |
| ABL1            | CBL            | damaging        |                   3 |                   764 |          -0.021743 |  0.756345 | 0.961295 | False                    | corum      | ABL1:CBL         |
| ABL1            | CTTN           | damaging        |                   3 |                   764 |          -0.02026  |  0.82747  | 0.971587 | False                    | corum      | ABL1:CTTN        |
| ABL1            | GRB2           | damaging        |                   3 |                   764 |           0.222592 |  0.642266 | 0.943971 | False                    | corum      | ABL1:GRB2        |
| ABL1            | MAD2L1         | damaging        |                   3 |                   764 |           0.116212 |  0.245848 | 0.878717 | False                    | corum      | ABL1:MAD2L1      |
| ABL1            | MAP2K1         | damaging        |                   3 |                   764 |          -0.044691 |  0.53893  | 0.925938 | False                    | corum      | ABL1:MAP2K1      |
| ABL1            | MAP2K2         | damaging        |                   3 |                   764 |           0.048838 |  0.570753 | 0.929854 | False                    | corum      | ABL1:MAP2K2      |
| ABL1            | MYLK           | damaging        |                   3 |                   764 |           0.117359 |  0.249176 | 0.878993 | False                    | corum      | ABL1:MYLK        |


*... [Truncated 161980 standard row items inline] ...*

**Last 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|---------:|:-------------------------|:-----------|:-----------------|
| ZNF217          | NR3C1          | damaging        |                   6 |                   761 |          -0.043274 |  0.359773 | 0.905725 | False                    | trrust     | NR3C1:ZNF217     |
| ZNF217          | NR4A1          | damaging        |                   6 |                   761 |          -0.01619  |  0.764802 | 0.969745 | False                    | trrust     | NR4A1:ZNF217     |
| ZNF217          | NT5E           | damaging        |                   6 |                   761 |          -0.087022 |  0.0343   | 0.70606  | False                    | trrust     | NT5E:ZNF217      |
| ZNF217          | PFKFB3         | damaging        |                   6 |                   761 |          -0.038338 |  0.180721 | 0.870509 | False                    | trrust     | PFKFB3:ZNF217    |
| ZNF217          | PFKFB4         | damaging        |                   6 |                   761 |           0.007086 |  0.894985 | 0.9866   | False                    | trrust     | PFKFB4:ZNF217    |
| ZNF217          | PGK1           | damaging        |                   6 |                   761 |           0.071979 |  0.785502 | 0.972881 | False                    | trrust     | PGK1:ZNF217      |
| ZNF217          | PIK3CA         | damaging        |                   6 |                   761 |           0.114319 |  0.272362 | 0.892957 | False                    | trrust     | PIK3CA:ZNF217    |
| ZNF217          | PLAU           | damaging        |                   6 |                   761 |           0.05514  |  0.336865 | 0.901862 | False                    | trrust     | PLAU:ZNF217      |
| ZNF217          | PPARA          | damaging        |                   6 |                   761 |          -0.032416 |  0.424607 | 0.917086 | False                    | trrust     | PPARA:ZNF217     |
| ZNF217          | PPP1R3C        | damaging        |                   6 |                   761 |          -0.013364 |  0.728759 | 0.963904 | False                    | trrust     | PPP1R3C:ZNF217   |
| ZNF217          | PTGES          | damaging        |                   6 |                   761 |           0.038663 |  0.062651 | 0.782133 | False                    | trrust     | PTGES:ZNF217     |
| ZNF217          | RECK           | damaging        |                   6 |                   761 |           0.079978 |  0.001921 | 0.21689  | False                    | trrust     | RECK:ZNF217      |
| ZNF217          | RORA           | damaging        |                   6 |                   761 |           0.024894 |  0.460059 | 0.921482 | False                    | trrust     | RORA:ZNF217      |
| ZNF217          | SDHB           | damaging        |                   6 |                   761 |          -0.291055 |  0.22463  | 0.882968 | False                    | trrust     | SDHB:ZNF217      |
| ZNF217          | SERPINE1       | damaging        |                   6 |                   761 |           0.022888 |  0.663383 | 0.95458  | False                    | trrust     | SERPINE1:ZNF217  |
| ZNF217          | SETD2          | damaging        |                   6 |                   761 |           0.028774 |  0.788423 | 0.973552 | False                    | trrust     | SETD2:ZNF217     |
| ZNF217          | SLC29A1        | damaging        |                   6 |                   761 |           0.042635 |  0.198046 | 0.875319 | False                    | trrust     | SLC29A1:ZNF217   |
| ZNF217          | SLC2A1         | damaging        |                   6 |                   761 |           0.249511 |  0.086282 | 0.82005  | False                    | trrust     | SLC2A1:ZNF217    |
| ZNF217          | SOCS1          | damaging        |                   6 |                   761 |           0.081285 |  0.051672 | 0.763201 | False                    | trrust     | SOCS1:ZNF217     |
| ZNF217          | STAT3          | damaging        |                   6 |                   761 |           0.025456 |  0.559544 | 0.938135 | False                    | trrust     | STAT3:ZNF217     |
| ZNF217          | TERT           | damaging        |                   6 |                   761 |          -0.028249 |  0.606731 | 0.945978 | False                    | trrust     | TERT:ZNF217      |
| ZNF217          | TFRC           | damaging        |                   6 |                   761 |          -0.18879  |  0.531049 | 0.932837 | False                    | trrust     | TFRC:ZNF217      |
| ZNF217          | TGFB3          | damaging        |                   6 |                   761 |           0.002481 |  0.946248 | 0.992931 | False                    | trrust     | TGFB3:ZNF217     |
| ZNF217          | TIMP2          | damaging        |                   6 |                   761 |          -0.025612 |  0.428284 | 0.917285 | False                    | trrust     | TIMP2:ZNF217     |
| ZNF217          | TLR2           | damaging        |                   6 |                   761 |           0.008799 |  0.811759 | 0.976039 | False                    | trrust     | TLR2:ZNF217      |
| ZNF217          | TLR6           | damaging        |                   6 |                   761 |           0.011526 |  0.705434 | 0.960183 | False                    | trrust     | TLR6:ZNF217      |
| ZNF217          | TUBB3          | damaging        |                   6 |                   761 |          -0.145482 |  0.33848  | 0.901408 | False                    | trrust     | TUBB3:ZNF217     |
| ZNF217          | TWIST1         | damaging        |                   6 |                   761 |           0.018458 |  0.78889  | 0.973569 | False                    | trrust     | TWIST1:ZNF217    |
| ZNF217          | TWIST2         | damaging        |                   6 |                   761 |          -0.014131 |  0.722146 | 0.962856 | False                    | trrust     | TWIST2:ZNF217    |
| ZNF217          | VEGFA          | damaging        |                   6 |                   761 |           0.055441 |  0.026454 | 0.660303 | False                    | trrust     | VEGFA:ZNF217     |
| ZNF217          | VEGFB          | damaging        |                   6 |                   761 |          -0.022046 |  0.649927 | 0.952182 | False                    | trrust     | VEGFB:ZNF217     |
| ZNF217          | VHL            | damaging        |                   6 |                   761 |           0.118529 |  0.324203 | 0.90075  | False                    | trrust     | VHL:ZNF217       |
| ZNF217          | VIM            | damaging        |                   6 |                   761 |           0.048345 |  0.358827 | 0.905658 | False                    | trrust     | VIM:ZNF217       |
| ZNF217          | WASF3          | damaging        |                   6 |                   761 |          -0.029486 |  0.566217 | 0.939915 | False                    | trrust     | WASF3:ZNF217     |
| ZNF217          | XPC            | damaging        |                   6 |                   761 |           0.042571 |  0.344633 | 0.902996 | False                    | trrust     | XPC:ZNF217       |
| ZNF274          | E2F3           | damaging        |                   4 |                   763 |           0.052212 |  0.682452 | 0.957121 | False                    | trrust     | E2F3:ZNF274      |
| ZNF274          | E2F4           | damaging        |                   4 |                   763 |          -0.003655 |  0.95385  | 0.99428  | False                    | trrust     | E2F4:ZNF274      |
| ZNF274          | ID1            | damaging        |                   4 |                   763 |          -0.03247  |  0.767315 | 0.970333 | False                    | trrust     | ID1:ZNF274       |
| ZNF274          | TRIM28         | damaging        |                   4 |                   763 |           0.09185  |  0.240414 | 0.886454 | False                    | trrust     | TRIM28:ZNF274    |
| ZNF335          | REST           | damaging        |                   3 |                   764 |          -0.006109 |  0.935757 | 0.991753 | False                    | trrust     | REST:ZNF335      |


---

## File: candidate_dependency_pairs.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/candidate_dependency_pairs.parquet`
- **Matrix Dimensions:** 69 rows × 11 columns

### 1. Data Schema & Quality Audit

| Column Name            | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------------|:--------|-----------------:|-------------:|:---------|
| mutation_gene          | object  |               69 |            0 | 0.00%    |
| partner_gene           | object  |               69 |            0 | 0.00%    |
| mutation_type          | object  |               69 |            0 | 0.00%    |
| num_mutant_models      | int64   |               69 |            0 | 0.00%    |
| num_wildtype_models    | int64   |               69 |            0 | 0.00%    |
| delta_dependency       | float64 |               69 |            0 | 0.00%    |
| p_value                | float64 |               69 |            0 | 0.00%    |
| fdr                    | float64 |               69 |            0 | 0.00%    |
| passes_main_thresholds | bool    |               69 |            0 | 0.00%    |
| topology               | object  |               69 |            0 | 0.00%    |
| undirected_key         | object  |               69 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                        |   count | unique   | top        | freq   | mean       | std        | min        | 25%        | 50%        | 75%        | max        |
|:-----------------------|--------:|:---------|:-----------|:-------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| mutation_gene          |      69 | 34       | RB1        | 8      | —          | —          | —          | —          | —          | —          | —          |
| partner_gene           |      69 | 47       | CTNNB1     | 4      | —          | —          | —          | —          | —          | —          | —          |
| mutation_type          |      69 | 2        | damaging   | 51     | —          | —          | —          | —          | —          | —          | —          |
| num_mutant_models      |      69 | —        | —          | —      | 84.188406  | 145.474101 | 3.000000   | 4.000000   | 39.000000  | 70.000000  | 534.000000 |
| num_wildtype_models    |      69 | —        | —          | —      | 675.971014 | 152.572159 | 233.000000 | 697.000000 | 727.000000 | 763.000000 | 764.000000 |
| delta_dependency       |      69 | —        | —          | —      | -0.397853  | 0.201425   | -0.945581  | -0.466470  | -0.331542  | -0.256750  | -0.202210  |
| p_value                |      69 | —        | —          | —      | 0.000088   | 0.000139   | 0.000000   | 0.000000   | 0.000005   | 0.000110   | 0.000506   |
| fdr                    |      69 | —        | —          | —      | 0.020283   | 0.028606   | 0.000000   | 0.000088   | 0.002878   | 0.033771   | 0.099374   |
| passes_main_thresholds |      69 | 1        | True       | 69     | —          | —          | —          | —          | —          | —          | —          |
| topology               |      69 | 3        | trrust     | 33     | —          | —          | —          | —          | —          | —          | —          |
| undirected_key         |      69 | 51       | APC:CTNNB1 | 4      | —          | —          | —          | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |               51 | 73.91%                  |
| hotspot          |               18 | 26.09%                  |

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| trrust           |               33 | 47.83%                  |
| string           |               24 | 34.78%                  |
| corum            |               12 | 17.39%                  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **69** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|
| TP53            | TP53BP1        | damaging        |                 534 |                   233 |          -0.222306 |         0 |     0 | True                     | string     | TP53:TP53BP1     |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |         0 |     0 | True                     | corum      | CDKN1A:TP53      |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |         0 |     0 | True                     | trrust     | CDKN1A:TP53      |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |         0 |     0 | True                     | corum      | APC:CTNNB1       |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |         0 |     0 | True                     | string     | APC:CTNNB1       |

- 💡 **Significance Hit:** Column `fdr` contains **57** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|------:|:-------------------------|:-----------|:-----------------|
| TP53            | TP53BP1        | damaging        |                 534 |                   233 |          -0.222306 |         0 |     0 | True                     | string     | TP53:TP53BP1     |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |         0 |     0 | True                     | corum      | CDKN1A:TP53      |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |         0 |     0 | True                     | trrust     | CDKN1A:TP53      |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |         0 |     0 | True                     | corum      | APC:CTNNB1       |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |         0 |     0 | True                     | string     | APC:CTNNB1       |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (69 rows total):

| mutation_gene   | partner_gene   | mutation_type   |   num_mutant_models |   num_wildtype_models |   delta_dependency |   p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   |
|:----------------|:---------------|:----------------|--------------------:|----------------------:|-------------------:|----------:|---------:|:-------------------------|:-----------|:-----------------|
| APC             | CTNNB1         | hotspot         |                  32 |                   735 |          -0.872441 |  3e-06    | 0.001115 | True                     | corum      | APC:CTNNB1       |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |  0        | 0        | True                     | corum      | APC:CTNNB1       |
| BRAF            | MAP2K1         | hotspot         |                  76 |                   691 |          -0.390174 |  0        | 0        | True                     | corum      | BRAF:MAP2K1      |
| CTNNB1          | TCF7L2         | hotspot         |                  20 |                   747 |          -0.46647  |  0.000105 | 0.025809 | True                     | corum      | CTNNB1:TCF7L2    |
| DCP2            | XRN1           | damaging        |                   3 |                   764 |          -0.244932 |  8.7e-05  | 0.022939 | True                     | corum      | DCP2:XRN1        |
| EP300           | CREBBP         | damaging        |                  51 |                   716 |          -0.370856 |  5e-06    | 0.001902 | True                     | corum      | CREBBP:EP300     |
| NRAS            | SHOC2          | hotspot         |                  36 |                   731 |          -0.474233 |  0        | 0.000221 | True                     | corum      | NRAS:SHOC2       |
| SMARCA4         | SMARCA2        | damaging        |                  40 |                   727 |          -0.373378 |  2.4e-05  | 0.00787  | True                     | corum      | SMARCA2:SMARCA4  |
| SPTLC3          | SPTLC1         | damaging        |                   3 |                   764 |          -0.281767 |  0.000294 | 0.06332  | True                     | corum      | SPTLC1:SPTLC3    |
| SYMPK           | CSTF1          | damaging        |                   3 |                   764 |          -0.302446 |  1e-06    | 0.00041  | True                     | corum      | CSTF1:SYMPK      |
| TP53            | CDK1           | damaging        |                 534 |                   233 |          -0.20221  |  2e-06    | 0.000873 | True                     | corum      | CDK1:TP53        |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |  0        | 0        | True                     | corum      | CDKN1A:TP53      |
| ABCE1           | RPL23A         | damaging        |                   4 |                   291 |          -0.439999 |  0.000197 | 0.041118 | True                     | string     | ABCE1:RPL23A     |
| APC             | CTNNB1         | hotspot         |                  32 |                   735 |          -0.872441 |  3e-06    | 0.001061 | True                     | string     | APC:CTNNB1       |
| APC             | CTNNB1         | damaging        |                  70 |                   697 |          -0.927101 |  0        | 0        | True                     | string     | APC:CTNNB1       |
| ARID1A          | ARID1B         | damaging        |                  65 |                   702 |          -0.263533 |  1e-06    | 0.000249 | True                     | string     | ARID1A:ARID1B    |
| BRAF            | MAP2K1         | hotspot         |                  76 |                   691 |          -0.390174 |  0        | 0        | True                     | string     | BRAF:MAP2K1      |
| BRAF            | MAPK1          | hotspot         |                  76 |                   691 |          -0.656319 |  0        | 0        | True                     | string     | BRAF:MAPK1       |
| CTNNB1          | TCF7L2         | hotspot         |                  20 |                   747 |          -0.46647  |  0.000105 | 0.025308 | True                     | string     | CTNNB1:TCF7L2    |
| DCP2            | XRN1           | damaging        |                   3 |                   764 |          -0.244932 |  8.7e-05  | 0.021086 | True                     | string     | DCP2:XRN1        |
| EIF1AX          | RPS15A         | hotspot         |                   4 |                   763 |          -0.340835 |  0.000426 | 0.076568 | True                     | string     | EIF1AX:RPS15A    |
| EP300           | CREBBP         | damaging        |                  51 |                   716 |          -0.370856 |  5e-06    | 0.001814 | True                     | string     | CREBBP:EP300     |
| KRAS            | BCL2L1         | hotspot         |                 101 |                   666 |          -0.343016 |  4e-05    | 0.011698 | True                     | string     | BCL2L1:KRAS      |
| NRAS            | RAF1           | hotspot         |                  36 |                   731 |          -0.416909 |  1e-06    | 0.000381 | True                     | string     | NRAS:RAF1        |
| NRAS            | SHOC2          | hotspot         |                  36 |                   731 |          -0.474233 |  0        | 0.000211 | True                     | string     | NRAS:SHOC2       |
| POLA1           | DONSON         | damaging        |                   3 |                   764 |          -0.330682 |  0.000152 | 0.033771 | True                     | string     | DONSON:POLA1     |
| RB1             | CDK2           | damaging        |                  55 |                   712 |          -0.303111 |  1.4e-05  | 0.004618 | True                     | string     | CDK2:RB1         |
| RB1             | E2F3           | damaging        |                  55 |                   712 |          -0.529216 |  0        | 1e-06    | True                     | string     | E2F3:RB1         |
| RB1             | SKP2           | damaging        |                  55 |                   712 |          -0.643086 |  0        | 3e-06    | True                     | string     | RB1:SKP2         |
| RB1             | TFDP1          | damaging        |                  55 |                   712 |          -0.277219 |  2e-06    | 0.000764 | True                     | string     | RB1:TFDP1        |
| SMARCA4         | SMARCA2        | damaging        |                  40 |                   727 |          -0.373378 |  2.4e-05  | 0.007319 | True                     | string     | SMARCA2:SMARCA4  |
| SPTLC3          | SPTLC1         | damaging        |                   3 |                   764 |          -0.281767 |  0.000294 | 0.057849 | True                     | string     | SPTLC1:SPTLC3    |
| STAG2           | STAG1          | damaging        |                  26 |                   741 |          -0.711204 |  5.5e-05  | 0.015169 | True                     | string     | STAG1:STAG2      |
| THRAP3          | BCLAF1         | damaging        |                   7 |                   760 |          -0.662451 |  0        | 2.7e-05  | True                     | string     | BCLAF1:THRAP3    |
| TP53            | TP53BP1        | damaging        |                 534 |                   233 |          -0.222306 |  0        | 0        | True                     | string     | TP53:TP53BP1     |
| YY1             | EP400          | damaging        |                   4 |                   763 |          -0.333544 |  0.000506 | 0.083242 | True                     | string     | EP400:YY1        |
| APC             | CDX2           | damaging        |                  70 |                   697 |          -0.20656  |  3.9e-05  | 0.015512 | True                     | trrust     | APC:CDX2         |
| APC             | SOX9           | damaging        |                  70 |                   697 |          -0.225719 |  0.000338 | 0.076712 | True                     | trrust     | APC:SOX9         |
| AR              | TP53           | damaging        |                   4 |                   763 |          -0.257811 |  5.4e-05  | 0.019784 | True                     | trrust     | AR:TP53          |
| BAX             | FPGS           | damaging        |                   3 |                   764 |          -0.588552 |  0.000458 | 0.093483 | True                     | trrust     | BAX:FPGS         |
| CD2AP           | TP53           | damaging        |                   3 |                   764 |          -0.26974  |  3e-06    | 0.002008 | True                     | trrust     | CD2AP:TP53       |
| CDK4            | PTEN           | damaging        |                   3 |                   764 |          -0.283702 |  0.0005   | 0.099374 | True                     | trrust     | CDK4:PTEN        |
| CDKN1A          | PLK1           | damaging        |                   3 |                   764 |          -0.815399 |  1e-06    | 0.000619 | True                     | trrust     | CDKN1A:PLK1      |
| CTNNB1          | TCF7L2         | hotspot         |                  20 |                   747 |          -0.46647  |  0.000105 | 0.033397 | True                     | trrust     | CTNNB1:TCF7L2    |
| E2F1            | P4HA1          | damaging        |                   3 |                   764 |          -0.204404 |  1.3e-05  | 0.006413 | True                     | trrust     | E2F1:P4HA1       |
| EP300           | CREBBP         | damaging        |                  51 |                   716 |          -0.370856 |  5e-06    | 0.002878 | True                     | trrust     | CREBBP:EP300     |
| EP300           | TSC2           | damaging        |                  51 |                   716 |          -0.264623 |  0.000285 | 0.068721 | True                     | trrust     | EP300:TSC2       |
| KHSRP           | EP300          | damaging        |                   4 |                   763 |          -0.349624 |  0        | 0        | True                     | trrust     | EP300:KHSRP      |
| KRAS            | CFLAR          | hotspot         |                 101 |                   666 |          -0.381255 |  0        | 0.000215 | True                     | trrust     | CFLAR:KRAS       |
| MCM8            | TP53           | damaging        |                   4 |                   763 |          -0.264021 |  0.000374 | 0.082679 | True                     | trrust     | MCM8:TP53        |
| MED1            | PTEN           | damaging        |                   5 |                   762 |          -0.25214  |  0.000155 | 0.043123 | True                     | trrust     | MED1:PTEN        |
| PLK1            | ING1           | damaging        |                   3 |                   764 |          -0.217086 |  0.00011  | 0.034119 | True                     | trrust     | ING1:PLK1        |
| RB1             | CDK2           | damaging        |                  55 |                   712 |          -0.303111 |  1.4e-05  | 0.006499 | True                     | trrust     | CDK2:RB1         |
| RB1             | E2F3           | damaging        |                  55 |                   712 |          -0.529216 |  0        | 2e-06    | True                     | trrust     | E2F3:RB1         |
| RB1             | SKP2           | damaging        |                  55 |                   712 |          -0.643086 |  0        | 5e-06    | True                     | trrust     | RB1:SKP2         |
| RB1             | TFDP1          | damaging        |                  55 |                   712 |          -0.277219 |  2e-06    | 0.001207 | True                     | trrust     | RB1:TFDP1        |
| SMAD4           | EGFR           | damaging        |                  39 |                   728 |          -0.322684 |  2.4e-05  | 0.01001  | True                     | trrust     | EGFR:SMAD4       |
| TERT            | ITGAV          | hotspot         |                 163 |                   604 |          -0.25675  |  0        | 2e-06    | True                     | trrust     | ITGAV:TERT       |
| TERT            | JUN            | hotspot         |                 163 |                   604 |          -0.20366  |  0        | 1e-05    | True                     | trrust     | JUN:TERT         |
| TERT            | MAPK1          | hotspot         |                 163 |                   604 |          -0.239712 |  0        | 4.2e-05  | True                     | trrust     | MAPK1:TERT       |
| TERT            | MDM2           | hotspot         |                 163 |                   604 |          -0.23174  |  3.4e-05  | 0.013867 | True                     | trrust     | MDM2:TERT        |
| TGFBR2          | PELO           | damaging        |                  25 |                   742 |          -0.603973 |  0.000311 | 0.072797 | True                     | trrust     | PELO:TGFBR2      |
| TGFBR2          | SLC7A5         | damaging        |                  25 |                   742 |          -0.264044 |  0.000123 | 0.036938 | True                     | trrust     | SLC7A5:TGFBR2    |
| TGFBR2          | WRN            | damaging        |                  25 |                   742 |          -0.945581 |  0.000127 | 0.037558 | True                     | trrust     | TGFBR2:WRN       |
| TNC             | CD58           | damaging        |                   3 |                   764 |          -0.211953 |  0.000245 | 0.061062 | True                     | trrust     | CD58:TNC         |
| TP53            | CDK1           | damaging        |                 534 |                   233 |          -0.20221  |  2e-06    | 0.001338 | True                     | trrust     | CDK1:TP53        |
| TP53            | CDKN1A         | damaging        |                 534 |                   233 |          -0.236332 |  0        | 0        | True                     | trrust     | CDKN1A:TP53      |
| TP53            | PCNA           | damaging        |                 534 |                   233 |          -0.213957 |  0        | 8.8e-05  | True                     | trrust     | PCNA:TP53        |
| TYK2            | COPS5          | damaging        |                   7 |                   760 |          -0.331542 |  0.000304 | 0.072364 | True                     | trrust     | COPS5:TYK2       |


---

## File: continuous_validation_meta_overview.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/continuous_validation_meta_overview.parquet`
- **Matrix Dimensions:** 3 rows × 14 columns

### 1. Data Schema & Quality Audit

| Column Name     | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------|:--------|-----------------:|-------------:|:---------|
| context         | object  |                3 |            0 | 0.00%    |
| endpoint_type   | object  |                3 |            0 | 0.00%    |
| effect_col      | object  |                3 |            0 | 0.00%    |
| se_col          | object  |                3 |            0 | 0.00%    |
| n_rows          | int64   |                3 |            0 | 0.00%    |
| n_unique_groups | int64   |                3 |            0 | 0.00%    |
| meta_mu         | float64 |                3 |            0 | 0.00%    |
| meta_se         | float64 |                3 |            0 | 0.00%    |
| meta_ci_low     | float64 |                3 |            0 | 0.00%    |
| meta_ci_high    | float64 |                3 |            0 | 0.00%    |
| meta_p          | float64 |                3 |            0 | 0.00%    |
| meta_i2         | float64 |                3 |            0 | 0.00%    |
| meta_tau2       | float64 |                3 |            0 | 0.00%    |
| source          | object  |                3 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                 |   count | unique   | top                       | freq   | mean      | std       | min       | 25%       | 50%       | 75%       | max        |
|:----------------|--------:|:---------|:--------------------------|:-------|:----------|:----------|:----------|:----------|:----------|:----------|:-----------|
| context         |       3 | 3        | Sanger                    | 1      | —         | —         | —         | —         | —         | —         | —          |
| endpoint_type   |       3 | 1        | continuous                | 3      | —         | —         | —         | —         | —         | —         | —          |
| effect_col      |       3 | 2        | external_delta_dependency | 2      | —         | —         | —         | —         | —         | —         | —          |
| se_col          |       3 | 2        | external_se               | 2      | —         | —         | —         | —         | —         | —         | —          |
| n_rows          |       3 | —        | —                         | —      | 42.333333 | 56.011903 | 9.000000  | 10.000000 | 11.000000 | 59.000000 | 107.000000 |
| n_unique_groups |       3 | —        | —                         | —      | 9.333333  | 1.527525  | 8.000000  | 8.500000  | 9.000000  | 10.000000 | 11.000000  |
| meta_mu         |       3 | —        | —                         | —      | -0.876399 | 1.303751  | -2.371364 | -1.326913 | -0.282462 | -0.128917 | 0.024628   |
| meta_se         |       3 | —        | —                         | —      | 0.248260  | 0.338694  | 0.046560  | 0.052748  | 0.058935  | 0.349110  | 0.639285   |
| meta_ci_low     |       3 | —        | —                         | —      | -1.362989 | 1.965402  | -3.624362 | -2.011169 | -0.397975 | -0.232302 | -0.066629  |
| meta_ci_high    |       3 | —        | —                         | —      | -0.389810 | 0.646602  | -1.118366 | -0.642657 | -0.166949 | -0.025532 | 0.115885   |
| meta_p          |       3 | —        | —                         | —      | 0.199014  | 0.344521  | 0.000002  | 0.000105  | 0.000208  | 0.298520  | 0.596833   |
| meta_i2         |       3 | —        | —                         | —      | 0.703026  | 0.360278  | 0.288638  | 0.583524  | 0.878410  | 0.910220  | 0.942031   |
| meta_tau2       |       3 | —        | —                         | —      | 0.960767  | 1.587681  | 0.033838  | 0.044138  | 0.054438  | 1.424231  | 2.794024   |
| source          |       3 | 2        | external_validation       | 2      | —         | —         | —         | —         | —         | —         | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `context`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| Sanger           |                1 | 33.33%                  |
| DepMap 25Q3      |                1 | 33.33%                  |
| TCGA bridge      |                1 | 33.33%                  |

**Column Grouping: `effect_col`**

| Value Category            |   Absolute Count | Percentage Proportion   |
|:--------------------------|-----------------:|:------------------------|
| external_delta_dependency |                2 | 66.67%                  |
| log_hazard_ratio          |                1 | 33.33%                  |

**Column Grouping: `se_col`**

| Value Category      |   Absolute Count | Percentage Proportion   |
|:--------------------|-----------------:|:------------------------|
| external_se         |                2 | 66.67%                  |
| log_hazard_ratio_se |                1 | 33.33%                  |

**Column Grouping: `source`**

| Value Category      |   Absolute Count | Percentage Proportion   |
|:--------------------|-----------------:|:------------------------|
| external_validation |                2 | 66.67%                  |
| tcga_bridge         |                1 | 33.33%                  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **2** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context     | endpoint_type   | effect_col                | se_col      |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 | source              |
|:------------|:----------------|:--------------------------|:------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|:--------------------|
| DepMap 25Q3 | continuous      | external_delta_dependency | external_se |       11 |                11 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 | 2e-06    |  0.942031 |    0.033838 | external_validation |
| Sanger      | continuous      | external_delta_dependency | external_se |        9 |                 9 | -2.37136  |  0.639285 |     -3.62436  |      -1.11837  | 0.000208 |  0.87841  |    2.79402  | external_validation |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (3 rows total):

| context     | endpoint_type   | effect_col                | se_col              |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 | source              |
|:------------|:----------------|:--------------------------|:--------------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|:--------------------|
| Sanger      | continuous      | external_delta_dependency | external_se         |        9 |                 9 | -2.37136  |  0.639285 |     -3.62436  |      -1.11837  | 0.000208 |  0.87841  |    2.79402  | external_validation |
| DepMap 25Q3 | continuous      | external_delta_dependency | external_se         |       11 |                11 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 | 2e-06    |  0.942031 |    0.033838 | external_validation |
| TCGA bridge | continuous      | log_hazard_ratio          | log_hazard_ratio_se |      107 |                 8 |  0.024628 |  0.04656  |     -0.066629 |       0.115885 | 0.596833 |  0.288638 |    0.054438 | tcga_bridge         |


---

## File: corum_family_pair_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/corum_family_pair_summary.parquet`
- **Matrix Dimensions:** 11054 rows × 19 columns

### 1. Data Schema & Quality Audit

| Column Name               | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------------|:--------|-----------------:|-------------:|:---------|
| pair_key                  | object  |            11054 |            0 | 0.00%    |
| min_hfrc                  | float64 |            11054 |            0 | 0.00%    |
| median_hfrc               | float64 |            11054 |            0 | 0.00%    |
| mean_hfrc                 | float64 |            11054 |            0 | 0.00%    |
| min_hlrc                  | float64 |            11054 |            0 | 0.00%    |
| median_hlrc               | float64 |            11054 |            0 | 0.00%    |
| mean_hlrc                 | float64 |            11054 |            0 | 0.00%    |
| mean_hyperedge_size       | float64 |            11054 |            0 | 0.00%    |
| min_hlrc_hyperedge_size   | int64   |            11054 |            0 | 0.00%    |
| mean_edge_node_degree     | float64 |            11054 |            0 | 0.00%    |
| mean_pair_essentiality    | float64 |            11054 |            0 | 0.00%    |
| pair_max_node_degree      | int64   |            11054 |            0 | 0.00%    |
| pair_hyperedge_count      | int64   |            11054 |            0 | 0.00%    |
| is_systematic_candidate   | int64   |            11054 |            0 | 0.00%    |
| is_validated_candidate    | int64   |            11054 |            0 | 0.00%    |
| log_pair_hyperedge_count  | float64 |            11054 |            0 | 0.00%    |
| log_pair_max_node_degree  | float64 |            11054 |            0 | 0.00%    |
| log_mean_edge_node_degree | float64 |            11054 |            0 | 0.00%    |
| log_mean_hyperedge_size   | float64 |            11054 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                           |   count | unique   | top       | freq   | mean       | std       | min         | 25%        | 50%        | 75%       | max       |
|:--------------------------|--------:|:---------|:----------|:-------|:-----------|:----------|:------------|:-----------|:-----------|:----------|:----------|
| pair_key                  |   11054 | 11054    | AATF:NGDN | 1      | —          | —         | —           | —          | —          | —         | —         |
| min_hfrc                  |   11054 | —        | —         | —      | -33.148996 | 40.680184 | -198.000000 | -52.000000 | -19.000000 | -4.000000 | 10.000000 |
| median_hfrc               |   11054 | —        | —         | —      | -30.923693 | 38.340813 | -198.000000 | -48.000000 | -17.500000 | -3.500000 | 10.000000 |
| mean_hfrc                 |   11054 | —        | —         | —      | -30.981402 | 38.184007 | -198.000000 | -48.000000 | -17.666667 | -3.541667 | 10.000000 |
| min_hlrc                  |   11054 | —        | —         | —      | 0.108372   | 0.452789  | -0.888728   | -0.198918  | 0.104058   | 0.437500  | 1.000000  |
| median_hlrc               |   11054 | —        | —         | —      | 0.144787   | 0.436398  | -0.888728   | -0.151599  | 0.125992   | 0.449493  | 1.000000  |
| mean_hlrc                 |   11054 | —        | —         | —      | 0.143340   | 0.435456  | -0.888728   | -0.151857  | 0.124123   | 0.448611  | 1.000000  |
| mean_hyperedge_size       |   11054 | —        | —         | —      | 5.785084   | 2.451671  | 3.000000    | 3.500000   | 5.000000   | 8.000000  | 10.000000 |
| min_hlrc_hyperedge_size   |   11054 | —        | —         | —      | 5.735752   | 2.476363  | 3.000000    | 3.000000   | 5.000000   | 8.000000  | 10.000000 |
| mean_edge_node_degree     |   11054 | —        | —         | —      | 7.417682   | 6.395090  | 1.000000    | 2.666667   | 5.333333   | 10.250000 | 43.666667 |
| mean_pair_essentiality    |   11054 | —        | —         | —      | -0.450464  | 0.516443  | -4.157716   | -0.702609  | -0.264284  | -0.063309 | 0.346915  |
| pair_max_node_degree      |   11054 | —        | —         | —      | 10.119957  | 11.610935 | 1.000000    | 3.000000   | 6.000000   | 13.000000 | 65.000000 |
| pair_hyperedge_count      |   11054 | —        | —         | —      | 1.578433   | 1.599995  | 1.000000    | 1.000000   | 1.000000   | 2.000000  | 31.000000 |
| is_systematic_candidate   |   11054 | —        | —         | —      | 0.000995   | 0.031531  | 0.000000    | 0.000000   | 0.000000   | 0.000000  | 1.000000  |
| is_validated_candidate    |   11054 | —        | —         | —      | 0.017822   | 0.132309  | 0.000000    | 0.000000   | 0.000000   | 0.000000  | 1.000000  |
| log_pair_hyperedge_count  |   11054 | —        | —         | —      | 0.865705   | 0.341736  | 0.693147    | 0.693147   | 0.693147   | 1.098612  | 3.465736  |
| log_pair_max_node_degree  |   11054 | —        | —         | —      | 2.007083   | 0.869899  | 0.693147    | 1.386294   | 1.945910   | 2.639057  | 4.189655  |
| log_mean_edge_node_degree |   11054 | —        | —         | —      | 1.878965   | 0.704977  | 0.693147    | 1.299283   | 1.845827   | 2.420368  | 3.799228  |
| log_mean_hyperedge_size   |   11054 | —        | —         | —      | 1.849110   | 0.363027  | 1.386294    | 1.504077   | 1.791759   | 2.197225  | 2.397895  |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| pair_key      |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:--------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| AATF:NGDN     |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -0.597209 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| AATF:NOL10    |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -1.06115  |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| ABCA12:NR1H2  |          0 |             0 |           0 |   0.4375   |      0.4375   |    0.4375   |                   3   |                         3 |                 2       |                 0.055105 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    1.09861  |                   1.38629 |
| ABCA1:ABCA12  |          0 |             0 |           0 |   0.4375   |      0.4375   |    0.4375   |                   3   |                         3 |                 2       |                 0.010216 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.09861  |                   1.38629 |
| ABCA1:COPS2   |         -6 |            -6 |          -6 |  -0.596591 |     -0.596591 |   -0.596591 |                   3   |                         3 |                 4       |                -0.516067 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.60944  |                   1.38629 |
| ABCA1:COPS5   |         -6 |            -6 |          -6 |  -0.596591 |     -0.596591 |   -0.596591 |                   3   |                         3 |                 4       |                -0.880454 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.60944  |                   1.38629 |
| ABCA1:FLOT1   |         -3 |            -3 |          -3 |  -0.2375   |     -0.2375   |   -0.2375   |                   3   |                         3 |                 3       |                -0.078279 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.38629  |                   1.38629 |
| ABCA1:NR1H2   |          0 |             0 |           0 |   0.4375   |      0.4375   |    0.4375   |                   3   |                         3 |                 2       |                 0.053843 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.09861  |                   1.38629 |
| ABCA1:SNTB2   |          0 |             0 |           0 |   0.4375   |      0.4375   |    0.4375   |                   3   |                         3 |                 2       |                -0.038778 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.09861  |                   1.38629 |
| ABCA1:STX12   |         -3 |            -3 |          -3 |  -0.2375   |     -0.2375   |   -0.2375   |                   3   |                         3 |                 3       |                -0.044255 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.38629  |                   1.38629 |
| ABCA1:UGP2    |          0 |             0 |           0 |   0.4375   |      0.4375   |    0.4375   |                   3   |                         3 |                 2       |                -0.184959 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.09861  |                   1.38629 |
| ABCB1:ANXA2   |        -23 |           -23 |         -23 |  -0.293162 |     -0.293162 |   -0.293162 |                   4   |                         4 |                 7.75    |                -0.04171  |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.16905  |                   1.60944 |
| ABCB1:PPP2R3C |          2 |             2 |           2 |   0.55     |      0.55     |    0.55     |                   3   |                         3 |                 1.33333 |                -0.392347 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.847298 |                   1.38629 |
| ABCB1:RACK1   |        -23 |           -23 |         -23 |  -0.293162 |     -0.293162 |   -0.293162 |                   4   |                         4 |                 7.75    |                -1.11161  |                      7 |                      1 |                         0 |                        0 |                   0.693147 |                   2.07944  |                    2.16905  |                   1.60944 |
| ABCB1:SRC     |        -23 |           -23 |         -23 |  -0.293162 |     -0.293162 |   -0.293162 |                   4   |                         4 |                 7.75    |                -0.100244 |                     20 |                      1 |                         0 |                        0 |                   0.693147 |                   3.04452  |                    2.16905  |                   1.60944 |
| ABCB1:TFPI2   |          2 |             2 |           2 |   0.55     |      0.55     |    0.55     |                   3   |                         3 |                 1.33333 |                -0.051832 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.847298 |                   1.38629 |
| ABCC9:KCNJ11  |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -0.019138 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| ABCC9:LDHA    |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -0.108554 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| ABCE1:HBS1L   |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -1.04755  |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| ABCE1:PELO    |          3 |             3 |           3 |   1        |      1        |    1        |                   3   |                         3 |                 1       |                -1.45888  |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.38629 |
| ABI1:ABL1     |        -19 |           -19 |         -19 |  -0.708734 |     -0.708734 |   -0.708734 |                   3   |                         3 |                 8.33333 |                -0.046249 |                     11 |                      1 |                         0 |                        0 |                   0.693147 |                   2.48491  |                    2.23359  |                   1.38629 |
| ABI1:BCAR1    |        -19 |           -19 |         -19 |  -0.708734 |     -0.708734 |   -0.708734 |                   3   |                         3 |                 8.33333 |                -0.127853 |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                   2.19722  |                    2.23359  |                   1.38629 |
| ABI1:BRK1     |         -3 |            -3 |          -3 |   0.418939 |      0.418939 |    0.418939 |                   5   |                         5 |                 2.6     |                -0.235824 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.28093  |                   1.79176 |
| ABI1:CYFIP1   |         -3 |            -3 |          -3 |   0.418939 |      0.418939 |    0.418939 |                   5   |                         5 |                 2.6     |                -0.177565 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.28093  |                   1.79176 |
| ABI1:EPS8     |        -12 |           -12 |         -12 |  -0.075758 |     -0.075758 |   -0.075758 |                   3   |                         3 |                 6       |                 0.006137 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.94591  |                   1.38629 |
| ABI1:EPS8L1   |        -12 |           -12 |         -12 |  -0.075758 |     -0.075758 |   -0.075758 |                   3   |                         3 |                 6       |                -0.100462 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.94591  |                   1.38629 |
| ABI1:EPS8L2   |        -12 |           -12 |         -12 |  -0.075758 |     -0.075758 |   -0.075758 |                   3   |                         3 |                 6       |                -0.080112 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.94591  |                   1.38629 |
| ABI1:EPS8L3   |        -12 |           -12 |         -12 |  -0.075758 |     -0.075758 |   -0.075758 |                   3   |                         3 |                 6       |                -0.159301 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.94591  |                   1.38629 |
| ABI1:NCKAP1   |         -3 |            -3 |          -3 |   0.418939 |      0.418939 |    0.418939 |                   5   |                         5 |                 2.6     |                -0.285093 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.28093  |                   1.79176 |
| ABI1:SOS1     |        -12 |           -12 |         -12 |  -0.075758 |     -0.075758 |   -0.075758 |                   3   |                         3 |                 6       |                -0.174911 |                     11 |                      4 |                         0 |                        0 |                   1.60944  |                   2.48491  |                    1.94591  |                   1.38629 |
| ABI1:WASF2    |         -3 |            -3 |          -3 |   0.418939 |      0.418939 |    0.418939 |                   5   |                         5 |                 2.6     |                -0.148504 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.28093  |                   1.79176 |
| ABI3:CYFIP1   |          1 |             1 |           1 |   0.25     |      0.25     |    0.25     |                   3   |                         3 |                 1.66667 |                -0.118142 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.980829 |                   1.38629 |
| ABI3:WASF2    |          1 |             1 |           1 |   0.25     |      0.25     |    0.25     |                   3   |                         3 |                 1.66667 |                -0.089081 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.980829 |                   1.38629 |
| ABL1:BCAR1    |        -19 |           -19 |         -19 |  -0.708734 |     -0.708734 |   -0.708734 |                   3   |                         3 |                 8.33333 |                -0.109185 |                     11 |                      1 |                         0 |                        0 |                   0.693147 |                   2.48491  |                    2.23359  |                   1.38629 |
| ABL1:BCR      |        -36 |           -22 |         -25 |  -0.411966 |     -0.25     |   -0.284587 |                   3.4 |                         4 |                 9.6     |                 0.009834 |                     11 |                      5 |                         0 |                        0 |                   1.79176  |                   2.48491  |                    2.36085  |                   1.48161 |
| ABL1:CBL      |        -28 |           -28 |         -28 |  -0.237097 |     -0.237097 |   -0.237097 |                   3   |                         3 |                11.3333  |                -0.000831 |                     18 |                      1 |                         0 |                        0 |                   0.693147 |                   2.94444  |                    2.51231  |                   1.38629 |
| ABL1:CTTN     |        -10 |           -10 |         -10 |  -0.038889 |     -0.038889 |   -0.038889 |                   3   |                         3 |                 5.33333 |                -0.102775 |                     11 |                      1 |                         0 |                        1 |                   0.693147 |                   2.48491  |                    1.84583  |                   1.38629 |
| ABL1:GRB2     |        -36 |           -36 |         -36 |  -0.25     |     -0.25     |   -0.25     |                   3   |                         3 |                14       |                -0.522769 |                     26 |                      1 |                         0 |                        0 |                   0.693147 |                   3.29584  |                    2.70805  |                   1.38629 |
| ABL1:MAD2L1   |        -11 |           -11 |         -11 |  -0.4      |     -0.4      |   -0.4      |                   3   |                         3 |                 5.66667 |                -0.696575 |                     11 |                      1 |                         0 |                        0 |                   0.693147 |                   2.48491  |                    1.89712  |                   1.38629 |
| ABL1:MAP2K1   |        -22 |           -22 |         -22 |  -0.411966 |     -0.411966 |   -0.411966 |                   4   |                         4 |                 7.5     |                -0.095721 |                     11 |                      2 |                         0 |                        0 |                   1.09861  |                   2.48491  |                    2.14007  |                   1.60944 |


*... [Truncated 10974 standard row items inline] ...*

**Last 40 Structural Rows:**

| pair_key       |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:---------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| WASHC1:WASHC4  |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -1.70211  |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.20683  |                   1.94591 |
| WASHC1:WASHC5  |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -1.7544   |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.20683  |                   1.94591 |
| WASHC2C:WASHC3 |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.431264 |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.20683  |                   1.94591 |
| WASHC2C:WASHC4 |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.34752  |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.20683  |                   1.94591 |
| WASHC2C:WASHC5 |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.399805 |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.20683  |                   1.94591 |
| WASHC3:WASHC4  |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.216979 |                      2 |                      2 |                         0 |                        0 |                   1.09861  |                   1.09861  |                    1.20683  |                   1.94591 |
| WASHC3:WASHC5  |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.269264 |                      2 |                      2 |                         0 |                        0 |                   1.09861  |                   1.09861  |                    1.20683  |                   1.94591 |
| WASHC4:WASHC5  |         -2 |          -2   |     -2      |   0.513889 |      0.604167 |    0.604167 |               6       |                         7 |                 2.34286 |                -0.18552  |                      2 |                      2 |                         0 |                        0 |                   1.09861  |                   1.09861  |                    1.20683  |                   1.94591 |
| WDR19:WDR35    |         -8 |          -8   |     -8      |   1        |      1        |    1        |               6       |                         5 |                 3.37143 |                -0.006161 |                      4 |                      2 |                         0 |                        0 |                   1.09861  |                   1.60944  |                    1.47509  |                   1.94591 |
| WDR20:WDR48    |          0 |           0   |      0      |   0.25     |      0.25     |    0.25     |               3       |                         3 |                 2       |                -0.242904 |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.09861  |                   1.38629 |
| WDR24:WDR59    |        -19 |         -17   |    -17.4    |   0.135294 |      0.319118 |    0.322815 |               6.6     |                         6 |                 4.69667 |                -0.468569 |                      5 |                      5 |                         0 |                        0 |                   1.79176  |                   1.79176  |                    1.73988  |                   2.02815 |
| WDR26:YPEL5    |        -17 |         -16   |    -16      |   0.705322 |      0.705322 |    0.705322 |              10       |                        10 |                 3.6     |                -0.680058 |                      4 |                      2 |                         0 |                        0 |                   1.09861  |                   1.60944  |                    1.52606  |                   2.3979  |
| WDR5:WDR82     |        -78 |         -61   |    -66      |  -0.100218 |      0.023538 |   -0.008503 |               7.33333 |                         6 |                11.2667  |                -1.59439  |                     21 |                      3 |                         0 |                        0 |                   1.38629  |                   3.09104  |                    2.50689  |                   2.12026 |
| WDR5:YEATS2    |        -20 |         -20   |    -20      |   0.361174 |      0.361174 |    0.361174 |              10       |                        10 |                 4       |                -0.866777 |                     21 |                      1 |                         0 |                        0 |                   0.693147 |                   3.09104  |                    1.60944  |                   2.3979  |
| WDR5:ZNF335    |        -55 |         -55   |    -55      |  -0.489107 |     -0.489107 |   -0.489107 |               4       |                         4 |                15.75    |                -0.887964 |                     21 |                      1 |                         0 |                        0 |                   0.693147 |                   3.09104  |                    2.8184   |                   1.60944 |
| WDR5:ZZZ3      |        -20 |         -20   |    -20      |   0.361174 |      0.361174 |    0.361174 |              10       |                        10 |                 4       |                -0.731379 |                     21 |                      1 |                         0 |                        0 |                   0.693147 |                   3.09104  |                    1.60944  |                   2.3979  |
| WIPF1:ZAP70    |         -6 |          -6   |     -6      |  -0.194444 |     -0.194444 |   -0.194444 |               4       |                         4 |                 3.5     |                 0.006787 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.50408  |                   1.60944 |
| WRN:XRCC5      |        -69 |         -61   |    -61      |  -0.648229 |     -0.615428 |   -0.615428 |               3.5     |                         4 |                19.4583  |                -0.544675 |                     27 |                      2 |                         0 |                        0 |                   1.09861  |                   3.33221  |                    3.01839  |                   1.50408 |
| WRN:XRCC6      |        -69 |         -61   |    -61      |  -0.648229 |     -0.615428 |   -0.615428 |               3.5     |                         4 |                19.4583  |                -1.07254  |                     29 |                      2 |                         0 |                        0 |                   1.09861  |                   3.4012   |                    3.01839  |                   1.50408 |
| WTAP:ZC3H13    |          3 |           3   |      3      |   1        |      1        |    1        |               6       |                         6 |                 1.5     |                -0.499764 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.916291 |                   1.94591 |
| XAB2:ZNF830    |         -7 |          -4.5 |     -4.5    |   0.5875   |      0.79375  |    0.79375  |               5.5     |                         6 |                 2.78333 |                -1.67928  |                      3 |                      2 |                         0 |                        0 |                   1.09861  |                   1.38629  |                    1.33061  |                   1.8718  |
| XPO5:ZNF346    |        -13 |         -13   |    -13      |   0.151429 |      0.151429 |    0.151429 |               4       |                         4 |                 5.25    |                -0.384975 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    1.83258  |                   1.60944 |
| XRCC2:XRCC3    |         -6 |          -6   |     -6      |   0.378968 |      0.378968 |    0.378968 |               5       |                         5 |                 3.2     |                -0.543392 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.43508  |                   1.79176 |
| XRCC4:XRCC5    |        -97 |         -84   |    -84      |  -0.463637 |     -0.175828 |   -0.175828 |               7.5     |                         7 |                13.3661  |                -0.587656 |                     27 |                      2 |                         0 |                        0 |                   1.09861  |                   3.33221  |                    2.66487  |                   2.14007 |
| XRCC4:XRCC6    |        -97 |         -84   |    -84      |  -0.463637 |     -0.175828 |   -0.175828 |               7.5     |                         7 |                13.3661  |                -1.11552  |                     29 |                      2 |                         0 |                        0 |                   1.09861  |                   3.4012   |                    2.66487  |                   2.14007 |
| XRCC5:XRCC6    |       -108 |         -68   |    -73.6296 |  -0.859184 |     -0.422368 |   -0.360829 |               5.48148 |                         3 |                16.9846  |                -1.43707  |                     29 |                     27 |                         0 |                        0 |                   3.33221  |                   3.4012   |                    2.88952  |                   1.86895 |
| XRCC5:YY1      |        -56 |         -56   |    -56      |  -0.773103 |     -0.773103 |   -0.773103 |               3       |                         3 |                20.6667  |                -0.837504 |                     27 |                      1 |                         0 |                        0 |                   0.693147 |                   3.33221  |                    3.07578  |                   1.38629 |
| XRCC6:YY1      |        -56 |         -56   |    -56      |  -0.773103 |     -0.773103 |   -0.773103 |               3       |                         3 |                20.6667  |                -1.36537  |                     29 |                      1 |                         0 |                        0 |                   0.693147 |                   3.4012   |                    3.07578  |                   1.38629 |
| XRN1:XRN2      |        -12 |         -12   |    -12      |   0.391646 |      0.391646 |    0.391646 |              10       |                        10 |                 3.2     |                -1.01067  |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    1.43508  |                   2.3979  |
| YAP1:YES1      |        -32 |         -32   |    -32      |  -0.317927 |     -0.317927 |   -0.317927 |               4       |                         4 |                10       |                -0.162911 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    2.3979   |                   1.60944 |
| YEATS2:ZZZ3    |        -20 |         -20   |    -20      |   0.361174 |      0.361174 |    0.361174 |              10       |                        10 |                 4       |                -0.439118 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    1.60944  |                   2.3979  |
| YEATS4:ZNHIT1  |        -48 |         -48   |    -48      |   0.225026 |      0.225026 |    0.225026 |              10       |                        10 |                 6.8     |                -0.600381 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.05412  |                   2.3979  |
| YWHAE:YWHAH    |        -32 |         -32   |    -32      |   0.056595 |      0.056595 |    0.056595 |               5       |                         5 |                 8.4     |                -0.201064 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    2.24071  |                   1.79176 |
| YWHAE:YWHAZ    |        -32 |         -32   |    -32      |   0.056595 |      0.056595 |    0.056595 |               5       |                         5 |                 8.4     |                -0.562597 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    2.24071  |                   1.79176 |
| YWHAH:YWHAZ    |        -32 |         -32   |    -32      |   0.056595 |      0.056595 |    0.056595 |               5       |                         5 |                 8.4     |                -0.346143 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                   1.38629  |                    2.24071  |                   1.79176 |
| ZMYM2:ZNF217   |       -119 |        -119   |   -119      |   0.225009 |      0.225009 |    0.225009 |              10       |                        10 |                13.9     |                -0.273796 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.70136  |                   2.3979  |
| ZMYM2:ZNF516   |       -119 |        -119   |   -119      |   0.225009 |      0.225009 |    0.225009 |              10       |                        10 |                13.9     |                 0.01478  |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    2.70136  |                   2.3979  |
| ZNF217:ZNF516  |       -119 |        -119   |   -119      |   0.225009 |      0.225009 |    0.225009 |              10       |                        10 |                13.9     |                -0.179843 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.70136  |                   2.3979  |
| ZW10:ZWILCH    |         -4 |          -3   |     -3      |   0.214286 |      0.333333 |    0.333333 |               3.5     |                         3 |                 2.83333 |                -0.27625  |                      5 |                      2 |                         0 |                        0 |                   1.09861  |                   1.79176  |                    1.34373  |                   1.50408 |
| ZW10:ZWINT     |         -5 |          -5   |     -5      |  -0.47619  |     -0.47619  |   -0.47619  |               3       |                         3 |                 3.66667 |                -0.43499  |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    1.54045  |                   1.38629 |


---

## File: degree_matched_permutation_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/degree_matched_permutation_summary.parquet`
- **Matrix Dimensions:** 6 rows × 7 columns

### 1. Data Schema & Quality Audit

| Column Name      | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------|:--------|-----------------:|-------------:|:---------|
| metric           | object  |                6 |            0 | 0.00%    |
| observed_count   | int64   |                6 |            0 | 0.00%    |
| observed_value   | float64 |                6 |            0 | 0.00%    |
| null_mean        | float64 |                6 |            0 | 0.00%    |
| empirical_p_less | float64 |                6 |            0 | 0.00%    |
| topology         | object  |                6 |            0 | 0.00%    |
| case_type        | object  |                6 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                  |   count | unique   | top                     | freq   | mean        | std         | min       | 25%        | 50%         | 75%         | max          |
|:-----------------|--------:|:---------|:------------------------|:-------|:------------|:------------|:----------|:-----------|:------------|:------------|:-------------|
| metric           |       6 | 1        | min_hlrc                | 6      | —           | —           | —         | —          | —           | —           | —            |
| observed_count   |       6 | —        | —                       | —      | 5099.000000 | 8859.036720 | 53.000000 | 264.750000 | 1230.500000 | 4345.000000 | 22754.000000 |
| observed_value   |       6 | —        | —                       | —      | -0.239328   | 0.300172    | -0.677206 | -0.442721  | -0.151615   | -0.043386   | 0.091531     |
| null_mean        |       6 | —        | —                       | —      | -0.156625   | 0.218125    | -0.462262 | -0.312310  | -0.111337   | -0.010177   | 0.100945     |
| empirical_p_less |       6 | —        | —                       | —      | 0.046333    | 0.113493    | 0.000000  | 0.000000   | 0.000000    | 0.000000    | 0.278000     |
| topology         |       6 | 3        | CORUM                   | 2      | —           | —           | —         | —          | —           | —           | —            |
| case_type        |       6 | 2        | is_systematic_candidate | 3      | —           | —           | —         | —          | —           | —           | —            |

### 3. Categorical Distribution Breakdown

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CORUM            |                2 | 33.33%                  |
| STRING           |                2 | 33.33%                  |
| TRRUST           |                2 | 33.33%                  |

**Column Grouping: `case_type`**

| Value Category          |   Absolute Count | Percentage Proportion   |
|:------------------------|-----------------:|:------------------------|
| is_systematic_candidate |                3 | 50.0%                   |
| is_validated_candidate  |                3 | 50.0%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (6 rows total):

| metric   |   observed_count |   observed_value |   null_mean |   empirical_p_less | topology   | case_type               |
|:---------|-----------------:|-----------------:|------------:|-------------------:|:-----------|:------------------------|
| min_hlrc |             1801 |        -0.114222 |   -0.057745 |              0     | CORUM      | is_systematic_candidate |
| min_hlrc |             5193 |        -0.527293 |   -0.361437 |              0     | STRING     | is_systematic_candidate |
| min_hlrc |            22754 |         0.091531 |    0.100945 |              0     | TRRUST     | is_systematic_candidate |
| min_hlrc |               53 |        -0.189007 |   -0.164928 |              0.278 | CORUM      | is_validated_candidate  |
| min_hlrc |              133 |        -0.677206 |   -0.462262 |              0     | STRING     | is_validated_candidate  |
| min_hlrc |              660 |        -0.019774 |    0.005678 |              0     | TRRUST     | is_validated_candidate  |


---

## File: depmap_25q3_continuous_meta_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/depmap_25q3_continuous_meta_summary.parquet`
- **Matrix Dimensions:** 1 rows × 13 columns

### 1. Data Schema & Quality Audit

| Column Name     | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------|:--------|-----------------:|-------------:|:---------|
| context         | object  |                1 |            0 | 0.00%    |
| endpoint_type   | object  |                1 |            0 | 0.00%    |
| effect_col      | object  |                1 |            0 | 0.00%    |
| se_col          | object  |                1 |            0 | 0.00%    |
| n_rows          | int64   |                1 |            0 | 0.00%    |
| n_unique_groups | int64   |                1 |            0 | 0.00%    |
| meta_mu         | float64 |                1 |            0 | 0.00%    |
| meta_se         | float64 |                1 |            0 | 0.00%    |
| meta_ci_low     | float64 |                1 |            0 | 0.00%    |
| meta_ci_high    | float64 |                1 |            0 | 0.00%    |
| meta_p          | float64 |                1 |            0 | 0.00%    |
| meta_i2         | float64 |                1 |            0 | 0.00%    |
| meta_tau2       | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                 |   count | unique   | top                       | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:----------------|--------:|:---------|:--------------------------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| context         |       1 | 1        | DepMap 25Q3               | 1      | —         | —     | —         | —         | —         | —         | —         |
| endpoint_type   |       1 | 1        | continuous                | 1      | —         | —     | —         | —         | —         | —         | —         |
| effect_col      |       1 | 1        | external_delta_dependency | 1      | —         | —     | —         | —         | —         | —         | —         |
| se_col          |       1 | 1        | external_se               | 1      | —         | —     | —         | —         | —         | —         | —         |
| n_rows          |       1 | —        | —                         | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| n_unique_groups |       1 | —        | —                         | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| meta_mu         |       1 | —        | —                         | —      | -0.282462 | —     | -0.282462 | -0.282462 | -0.282462 | -0.282462 | -0.282462 |
| meta_se         |       1 | —        | —                         | —      | 0.058935  | —     | 0.058935  | 0.058935  | 0.058935  | 0.058935  | 0.058935  |
| meta_ci_low     |       1 | —        | —                         | —      | -0.397975 | —     | -0.397975 | -0.397975 | -0.397975 | -0.397975 | -0.397975 |
| meta_ci_high    |       1 | —        | —                         | —      | -0.166949 | —     | -0.166949 | -0.166949 | -0.166949 | -0.166949 | -0.166949 |
| meta_p          |       1 | —        | —                         | —      | 0.000002  | —     | 0.000002  | 0.000002  | 0.000002  | 0.000002  | 0.000002  |
| meta_i2         |       1 | —        | —                         | —      | 0.942031  | —     | 0.942031  | 0.942031  | 0.942031  | 0.942031  | 0.942031  |
| meta_tau2       |       1 | —        | —                         | —      | 0.033838  | —     | 0.033838  | 0.033838  | 0.033838  | 0.033838  | 0.033838  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **1** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context     | endpoint_type   | effect_col                | se_col      |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|:--------------------------|:------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| DepMap 25Q3 | continuous      | external_delta_dependency | external_se |       11 |                11 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 |    2e-06 |  0.942031 |    0.033838 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| context     | endpoint_type   | effect_col                | se_col      |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|:--------------------------|:------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| DepMap 25Q3 | continuous      | external_delta_dependency | external_se |       11 |                11 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 |    2e-06 |  0.942031 |    0.033838 |


---

## File: depmap_25q3_leave_one_out.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/depmap_25q3_leave_one_out.parquet`
- **Matrix Dimensions:** 11 rows × 10 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| context       | object  |               11 |            0 | 0.00%    |
| omitted_group | object  |               11 |            0 | 0.00%    |
| n_remaining   | int64   |               11 |            0 | 0.00%    |
| meta_mu       | float64 |               11 |            0 | 0.00%    |
| meta_se       | float64 |               11 |            0 | 0.00%    |
| meta_ci_low   | float64 |               11 |            0 | 0.00%    |
| meta_ci_high  | float64 |               11 |            0 | 0.00%    |
| meta_p        | float64 |               11 |            0 | 0.00%    |
| meta_i2       | float64 |               11 |            0 | 0.00%    |
| meta_tau2     | float64 |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|               |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:--------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| context       |      11 | 1        | DepMap 25Q3 | 11     | —         | —        | —         | —         | —         | —         | —         |
| omitted_group |      11 | 11       | AP3B2:AP3M2 | 1      | —         | —        | —         | —         | —         | —         | —         |
| n_remaining   |      11 | —        | —           | —      | 10.000000 | 0.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 |
| meta_mu       |      11 | —        | —           | —      | -0.282567 | 0.023552 | -0.308329 | -0.301932 | -0.277630 | -0.273071 | -0.229281 |
| meta_se       |      11 | —        | —           | —      | 0.062187  | 0.004846 | 0.049582  | 0.061666  | 0.062424  | 0.064131  | 0.068337  |
| meta_ci_low   |      11 | —        | —           | —      | -0.404453 | 0.032179 | -0.437153 | -0.431562 | -0.400782 | -0.394631 | -0.326462 |
| meta_ci_high  |      11 | —        | —           | —      | -0.160680 | 0.015948 | -0.185395 | -0.172291 | -0.154477 | -0.151510 | -0.132100 |
| meta_p        |      11 | —        | —           | —      | 0.000007  | 0.000004 | 0.000001  | 0.000003  | 0.000009  | 0.000010  | 0.000012  |
| meta_i2       |      11 | —        | —           | —      | 0.940309  | 0.010361 | 0.913606  | 0.938394  | 0.945412  | 0.946063  | 0.947716  |
| meta_tau2     |      11 | —        | —           | —      | 0.034513  | 0.005450 | 0.020645  | 0.034060  | 0.034582  | 0.036585  | 0.041792  |

### 3. Categorical Distribution Breakdown

**Column Grouping: `omitted_group`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **11** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context     | omitted_group   |   n_remaining |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|--------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| DepMap 25Q3 | CD151:ITGA6     |            10 | -0.308329 |  0.062721 |     -0.431263 |      -0.185395 |    1e-06 |  0.946051 |    0.03496  |
| DepMap 25Q3 | DCP2:XRN1       |            10 | -0.295582 |  0.06145  |     -0.416025 |      -0.175139 |    2e-06 |  0.947716 |    0.034443 |
| DepMap 25Q3 | AP3B2:AP3M2     |            10 | -0.306615 |  0.065429 |     -0.434856 |      -0.178374 |    3e-06 |  0.944755 |    0.038094 |
| DepMap 25Q3 | APC:CTNNB1      |            10 | -0.229281 |  0.049582 |     -0.326462 |      -0.1321   |    4e-06 |  0.913606 |    0.020645 |
| DepMap 25Q3 | IFT122:WDR35    |            10 | -0.300652 |  0.066944 |     -0.431861 |      -0.169442 |    7e-06 |  0.946986 |    0.040072 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| context     | omitted_group   |   n_remaining |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|--------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| DepMap 25Q3 | AP3B2:AP3M2     |            10 | -0.306615 |  0.065429 |     -0.434856 |      -0.178374 |  3e-06   |  0.944755 |    0.038094 |
| DepMap 25Q3 | APC:CTNNB1      |            10 | -0.229281 |  0.049582 |     -0.326462 |      -0.1321   |  4e-06   |  0.913606 |    0.020645 |
| DepMap 25Q3 | BRAF:MAP2K1     |            10 | -0.272431 |  0.06216  |     -0.394265 |      -0.150596 |  1.2e-05 |  0.937498 |    0.033952 |
| DepMap 25Q3 | CD151:ITGA6     |            10 | -0.308329 |  0.062721 |     -0.431263 |      -0.185395 |  1e-06   |  0.946051 |    0.03496  |
| DepMap 25Q3 | CREBBP:EP300    |            10 | -0.27763  |  0.062833 |     -0.400782 |      -0.154477 |  1e-05   |  0.946051 |    0.035077 |
| DepMap 25Q3 | CTNNB1:TCF7L2   |            10 | -0.273711 |  0.061881 |     -0.394998 |      -0.152423 |  1e-05   |  0.946076 |    0.034169 |
| DepMap 25Q3 | DCP2:XRN1       |            10 | -0.295582 |  0.06145  |     -0.416025 |      -0.175139 |  2e-06   |  0.947716 |    0.034443 |
| DepMap 25Q3 | IFT122:WDR35    |            10 | -0.300652 |  0.066944 |     -0.431861 |      -0.169442 |  7e-06   |  0.946986 |    0.040072 |
| DepMap 25Q3 | IL2:IL2RG       |            10 | -0.303213 |  0.068337 |     -0.437153 |      -0.169273 |  9e-06   |  0.929961 |    0.041792 |
| DepMap 25Q3 | NRAS:SHOC2      |            10 | -0.265857 |  0.060295 |     -0.384035 |      -0.147678 |  1e-05   |  0.939291 |    0.031859 |
| DepMap 25Q3 | SMARCA2:SMARCA4 |            10 | -0.274936 |  0.062424 |     -0.397288 |      -0.152585 |  1.1e-05 |  0.945412 |    0.034582 |


---

## File: graph_metric_benchmark_best.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/graph_metric_benchmark_best.parquet`
- **Matrix Dimensions:** 18 rows × 9 columns

### 1. Data Schema & Quality Audit

| Column Name            | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------------|:--------|-----------------:|-------------:|:---------|
| cohort                 | object  |               18 |            0 | 0.00%    |
| topology               | object  |               18 |            0 | 0.00%    |
| endpoint_type          | object  |               18 |            0 | 0.00%    |
| label_name             | object  |               18 |            0 | 0.00%    |
| best_metric            | object  |               18 |            0 | 0.00%    |
| best_average_precision | float64 |               11 |            7 | 38.89%   |
| best_roc_auc           | float64 |                9 |            9 | 50.00%   |
| best_spearman_rho      | float64 |               16 |            2 | 11.11%   |
| best_pearson_r         | float64 |                7 |           11 | 61.11%   |

### 2. Full Descriptive Summary Statistics

|                        |   count | unique   | top                       | freq   | mean     | std      | min      | 25%      | 50%      | 75%      | max      |
|:-----------------------|--------:|:---------|:--------------------------|:-------|:---------|:---------|:---------|:---------|:---------|:---------|:---------|
| cohort                 |      18 | 7        | internal_heldout          | 6      | —        | —        | —        | —        | —        | —        | —        |
| topology               |      18 | 3        | corum                     | 8      | —        | —        | —        | —        | —        | —        | —        |
| endpoint_type          |      18 | 2        | binary                    | 11     | —        | —        | —        | —        | —        | —        | —        |
| label_name             |      18 | 5        | external_delta_dependency | 4      | —        | —        | —        | —        | —        | —        | —        |
| best_metric            |      18 | 5        | hlrc                      | 6      | —        | —        | —        | —        | —        | —        | —        |
| best_average_precision |      11 | —        | —                         | —      | 0.673928 | 0.410991 | 0.036061 | 0.408380 | 0.906041 | 0.945455 | 1.000000 |
| best_roc_auc           |       9 | —        | —                         | —      | 0.648751 | 0.111649 | 0.525762 | 0.566667 | 0.600000 | 0.722222 | 0.833333 |
| best_spearman_rho      |      16 | —        | —                         | —      | 0.234322 | 0.204454 | 0.004664 | 0.027189 | 0.198406 | 0.455553 | 0.527273 |
| best_pearson_r         |       7 | —        | —                         | —      | 0.275504 | 0.311966 | 0.002094 | 0.024264 | 0.071510 | 0.560841 | 0.684711 |

### 3. Categorical Distribution Breakdown

**Column Grouping: `cohort`**

| Value Category                         |   Absolute Count | Percentage Proportion   |
|:---------------------------------------|-----------------:|:------------------------|
| internal_heldout                       |                6 | 33.33%                  |
| depmap25q3_neg_delta_dependency        |                2 | 11.11%                  |
| depmap25q3_passes_external_nominal     |                2 | 11.11%                  |
| depmap25q3_same_direction_as_discovery |                2 | 11.11%                  |
| sanger_neg_delta_dependency            |                2 | 11.11%                  |
| sanger_passes_external_nominal         |                2 | 11.11%                  |
| sanger_same_direction_as_discovery     |                2 | 11.11%                  |

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| corum            |                8 | 44.44%                  |
| string           |                8 | 44.44%                  |
| trrust           |                2 | 11.11%                  |

**Column Grouping: `endpoint_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| binary           |               11 | 61.11%                  |
| continuous       |                7 | 38.89%                  |

**Column Grouping: `label_name`**

| Value Category              |   Absolute Count | Percentage Proportion   |
|:----------------------------|-----------------:|:------------------------|
| external_delta_dependency   |                4 | 22.22%                  |
| passes_external_nominal     |                4 | 22.22%                  |
| same_direction_as_discovery |                4 | 22.22%                  |
| passes_validation_nominal   |                3 | 16.67%                  |
| delta_dependency            |                3 | 16.67%                  |

**Column Grouping: `best_metric`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| hlrc             |                6 | 33.33%                  |
| pagerank         |                5 | 27.78%                  |
| hfrc             |                3 | 16.67%                  |
| betweenness      |                2 | 11.11%                  |
| jaccard          |                2 | 11.11%                  |

### 4. Significant Signals & Key Highlights

- 📈 **Peak Performance Asset (`best_average_precision`):** Maximal value observed is `1.00000`.
- 📈 **Peak Performance Asset (`best_roc_auc`):** Maximal value observed is `0.83333`.
- 📈 **Peak Performance Asset (`best_spearman_rho`):** Maximal value observed is `0.52727`.
- 📈 **Peak Performance Asset (`best_pearson_r`):** Maximal value observed is `0.68471`.

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (18 rows total):

| cohort                                 | topology   | endpoint_type   | label_name                  | best_metric   |   best_average_precision |   best_roc_auc |   best_spearman_rho |   best_pearson_r |
|:---------------------------------------|:-----------|:----------------|:----------------------------|:--------------|-------------------------:|---------------:|--------------------:|-----------------:|
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | betweenness   |               nan        |     nan        |            0.478361 |         0.684711 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | pagerank      |               nan        |     nan        |            0.527273 |         0.633301 |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | pagerank      |                 0.938131 |       0.791667 |            0.451848 |       nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | hfrc          |                 0.947222 |       0.833333 |            0.516398 |       nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | hlrc          |                 1        |     nan        |          nan        |       nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | hlrc          |                 1        |     nan        |          nan        |       nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | hlrc          |                 0.036061 |       0.525762 |            0.015875 |       nan        |
| internal_heldout                       | corum      | continuous      | delta_dependency            | jaccard       |               nan        |     nan        |            0.004664 |         0.007805 |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | betweenness   |                 0.049378 |       0.537525 |            0.022329 |       nan        |
| internal_heldout                       | string     | continuous      | delta_dependency            | hlrc          |               nan        |     nan        |            0.02881  |         0.040723 |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | pagerank      |                 0.049926 |       0.594916 |            0.058503 |       nan        |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | pagerank      |               nan        |     nan        |            0.017998 |         0.002094 |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | hfrc          |               nan        |     nan        |            0.35     |         0.07151  |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | pagerank      |               nan        |     nan        |            0.466667 |         0.488381 |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | hfrc          |                 0.775926 |       0.6      |            0.173205 |       nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | hlrc          |                 0.766835 |       0.566667 |            0.11547  |       nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | hlrc          |                 0.943687 |       0.722222 |            0.298142 |       nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | jaccard       |                 0.906041 |       0.666667 |            0.223607 |       nan        |


---

## File: graph_metric_benchmark_pairs.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/graph_metric_benchmark_pairs.parquet`
- **Matrix Dimensions:** 350904 rows × 10 columns

### 1. Data Schema & Quality Audit

| Column Name           | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------------|:--------|-----------------:|-------------:|:---------|
| pair_key              | object  |           350904 |            0 | 0.00%    |
| min_hlrc              | float64 |           350904 |            0 | 0.00%    |
| min_hfrc              | float64 |           350904 |            0 | 0.00%    |
| pair_degree_mean      | float64 |           350904 |            0 | 0.00%    |
| pair_pagerank_mean    | float64 |           350904 |            0 | 0.00%    |
| pair_betweenness_mean | float64 |           350904 |            0 | 0.00%    |
| pair_jaccard          | float64 |           350904 |            0 | 0.00%    |
| topology              | object  |           350904 |            0 | 0.00%    |
| hlrc_score            | float64 |           350904 |            0 | 0.00%    |
| hfrc_score            | float64 |           350904 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                       |   count | unique   | top       | freq   | mean         | std         | min          | 25%          | 50%          | 75%         | max         |
|:----------------------|--------:|:---------|:----------|:-------|:-------------|:------------|:-------------|:-------------|:-------------|:------------|:------------|
| pair_key              |  350904 | 341995   | DHFR:TYMS | 3      | —            | —           | —            | —            | —            | —           | —           |
| min_hlrc              |  350904 | —        | —         | —      | 0.045493     | 0.373271    | -0.987050    | -0.183603    | 0.083392     | 0.448826    | 1.000000    |
| min_hfrc              |  350904 | —        | —         | —      | -1505.492915 | 1030.072215 | -5877.000000 | -2318.000000 | -1613.000000 | -533.000000 | 10.000000   |
| pair_degree_mean      |  350904 | —        | —         | —      | 384.877935   | 263.456882  | 1.000000     | 105.000000   | 439.000000   | 583.500000  | 1572.500000 |
| pair_pagerank_mean    |  350904 | —        | —         | —      | 0.000723     | 0.000523    | 0.000028     | 0.000290     | 0.000646     | 0.000977    | 0.005309    |
| pair_betweenness_mean |  350904 | —        | —         | —      | 0.001660     | 0.003326    | 0.000000     | 0.000186     | 0.000589     | 0.001615    | 0.058377    |
| pair_jaccard          |  350904 | —        | —         | —      | 0.458511     | 0.289341    | 0.000000     | 0.194729     | 0.446139     | 0.697248    | 0.997245    |
| topology              |  350904 | 3        | trrust    | 260576 | —            | —           | —            | —            | —            | —           | —           |
| hlrc_score            |  350904 | —        | —         | —      | -0.045493    | 0.373271    | -1.000000    | -0.448826    | -0.083392    | 0.183603    | 0.987050    |
| hfrc_score            |  350904 | —        | —         | —      | 1505.492915  | 1030.072215 | -10.000000   | 533.000000   | 1613.000000  | 2318.000000 | 5877.000000 |

### 3. Categorical Distribution Breakdown

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| trrust           |           260576 | 74.26%                  |
| string           |            79274 | 22.59%                  |
| corum            |            11054 | 3.15%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| pair_key      |   min_hlrc |   min_hfrc |   pair_degree_mean |   pair_pagerank_mean |   pair_betweenness_mean |   pair_jaccard | topology   |   hlrc_score |   hfrc_score |
|:--------------|-----------:|-----------:|-------------------:|---------------------:|------------------------:|---------------:|:-----------|-------------:|-------------:|
| AATF:NGDN     |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| AATF:NOL10    |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| ABCA12:NR1H2  |   0.4375   |          0 |                2   |             0.000164 |                0        |       0.333333 | corum      |    -0.4375   |           -0 |
| ABCA1:ABCA12  |   0.4375   |          0 |                5   |             0.000307 |                0.000661 |       0.111111 | corum      |    -0.4375   |           -0 |
| ABCA1:COPS2   |  -0.596591 |         -6 |               10   |             0.000445 |                0.001034 |       0.052632 | corum      |     0.596591 |            6 |
| ABCA1:COPS5   |  -0.596591 |         -6 |                9.5 |             0.000428 |                0.001208 |       0.055556 | corum      |     0.596591 |            6 |
| ABCA1:FLOT1   |  -0.2375   |         -3 |                6   |             0.000329 |                0.000907 |       0.090909 | corum      |     0.2375   |            3 |
| ABCA1:NR1H2   |   0.4375   |          0 |                5   |             0.000307 |                0.000661 |       0.111111 | corum      |    -0.4375   |           -0 |
| ABCA1:SNTB2   |   0.4375   |          0 |                5   |             0.000307 |                0.000661 |       0.111111 | corum      |    -0.4375   |           -0 |
| ABCA1:STX12   |  -0.2375   |         -3 |                6.5 |             0.000373 |                0.000958 |       0.083333 | corum      |     0.2375   |            3 |
| ABCA1:UGP2    |   0.4375   |          0 |                5   |             0.000307 |                0.000661 |       0.111111 | corum      |    -0.4375   |           -0 |
| ABCB1:ANXA2   |  -0.293162 |        -23 |                5   |             0.000269 |                0.000396 |       0.25     | corum      |     0.293162 |           23 |
| ABCB1:PPP2R3C |   0.55     |          2 |                3.5 |             0.000224 |                0.000237 |       0.166667 | corum      |    -0.55     |           -2 |
| ABCB1:RACK1   |  -0.293162 |        -23 |               11.5 |             0.000477 |                0.008978 |       0.095238 | corum      |     0.293162 |           23 |
| ABCB1:SRC     |  -0.293162 |        -23 |               22   |             0.000812 |                0.032439 |       0.047619 | corum      |     0.293162 |           23 |
| ABCB1:TFPI2   |   0.55     |          2 |                3.5 |             0.000224 |                0.000237 |       0.166667 | corum      |    -0.55     |           -2 |
| ABCC9:KCNJ11  |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| ABCC9:LDHA    |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| ABCE1:HBS1L   |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| ABCE1:PELO    |   1        |          3 |                2   |             0.000304 |                0        |       0.333333 | corum      |    -1        |           -3 |
| ABI1:ABL1     |  -0.708734 |        -19 |               13   |             0.00064  |                0.002932 |       0.04     | corum      |     0.708734 |           19 |
| ABI1:BCAR1    |  -0.708734 |        -19 |               14   |             0.000603 |                0.00624  |       0.076923 | corum      |     0.708734 |           19 |
| ABI1:BRK1     |   0.418939 |         -3 |                7.5 |             0.000386 |                0.00065  |       0.25     | corum      |    -0.418939 |            3 |
| ABI1:CYFIP1   |   0.418939 |         -3 |                8   |             0.000438 |                0.000709 |       0.230769 | corum      |    -0.418939 |            3 |
| ABI1:EPS8     |  -0.075758 |        -12 |                6.5 |             0.000331 |                0.00065  |       0.083333 | corum      |     0.075758 |           12 |
| ABI1:EPS8L1   |  -0.075758 |        -12 |                6.5 |             0.000331 |                0.00065  |       0.083333 | corum      |     0.075758 |           12 |
| ABI1:EPS8L2   |  -0.075758 |        -12 |                6.5 |             0.000331 |                0.00065  |       0.083333 | corum      |     0.075758 |           12 |
| ABI1:EPS8L3   |  -0.075758 |        -12 |                6.5 |             0.000331 |                0.00065  |       0.083333 | corum      |     0.075758 |           12 |
| ABI1:NCKAP1   |   0.418939 |         -3 |                8.5 |             0.000432 |                0.000742 |       0.214286 | corum      |    -0.418939 |            3 |
| ABI1:SOS1     |  -0.075758 |        -12 |               14.5 |             0.000731 |                0.00152  |       0.208333 | corum      |     0.075758 |           12 |
| ABI1:WASF2    |   0.418939 |         -3 |                8   |             0.000438 |                0.000709 |       0.230769 | corum      |    -0.418939 |            3 |
| ABI3:CYFIP1   |   0.25     |          1 |                3.5 |             0.000227 |                5.9e-05  |       0.166667 | corum      |    -0.25     |           -1 |
| ABI3:WASF2    |   0.25     |          1 |                3.5 |             0.000227 |                5.9e-05  |       0.166667 | corum      |    -0.25     |           -1 |
| ABL1:BCAR1    |  -0.708734 |        -19 |               16   |             0.000685 |                0.007872 |       0.103448 | corum      |     0.708734 |           19 |
| ABL1:BCR      |  -0.411966 |        -36 |               10.5 |             0.00053  |                0.002349 |       0.3125   | corum      |     0.411966 |           36 |
| ABL1:CBL      |  -0.237097 |        -28 |               23   |             0.001047 |                0.004339 |       0.095238 | corum      |     0.237097 |           28 |
| ABL1:CTTN     |  -0.038889 |        -10 |               12   |             0.000538 |                0.002862 |       0.043478 | corum      |     0.038889 |           10 |
| ABL1:GRB2     |  -0.25     |        -36 |               25   |             0.001261 |                0.00499  |       0.086957 | corum      |     0.25     |           36 |
| ABL1:MAD2L1   |  -0.4      |        -11 |               10   |             0.000481 |                0.002462 |       0.052632 | corum      |     0.4      |           11 |
| ABL1:MAP2K1   |  -0.411966 |        -22 |               16.5 |             0.000797 |                0.004015 |       0.064516 | corum      |     0.411966 |           22 |


*... [Truncated 350824 standard row items inline] ...*

**Last 40 Structural Rows:**

| pair_key     |   min_hlrc |   min_hfrc |   pair_degree_mean |   pair_pagerank_mean |   pair_betweenness_mean |   pair_jaccard | topology   |   hlrc_score |   hfrc_score |
|:-------------|-----------:|-----------:|-------------------:|---------------------:|------------------------:|---------------:|:-----------|-------------:|-------------:|
| WDFY4:ZNF175 |  -0.042965 |       -637 |               94.5 |             0.000185 |                3.6e-05  |       0.89     | trrust     |     0.042965 |          637 |
| WEE1:WNT7B   |   0.079064 |       -721 |               98   |             0.000203 |                1.7e-05  |       0.849057 | trrust     |    -0.079064 |          721 |
| WEE1:XIAP    |   0.079064 |       -721 |              427   |             0.000741 |                0.000677 |       0.12963  | trrust     |    -0.079064 |          721 |
| WFS1:XBP1    |  -0.226624 |       -211 |               67.5 |             0.000189 |                8.4e-05  |       0.144068 | trrust     |     0.226624 |          211 |
| WFS1:ZHX2    |  -0.226624 |       -211 |               23   |             0.000109 |                1.7e-05  |       0.586207 | trrust     |     0.226624 |          211 |
| WIF1:WRN     |   0.448826 |      -2318 |              571   |             0.000726 |                0.00033  |       0.686854 | trrust     |    -0.448826 |         2318 |
| WIF1:WT1     |   0.448826 |      -2318 |              672   |             0.001106 |                0.001757 |       0.52901  | trrust     |    -0.448826 |         2318 |
| WIF1:XIAP    |   0.448826 |      -2318 |              607.5 |             0.000885 |                0.000659 |       0.62     | trrust     |    -0.448826 |         2318 |
| WIF1:XPC     |   0.448826 |      -2318 |              602.5 |             0.000822 |                0.001169 |       0.628378 | trrust     |    -0.448826 |         2318 |
| WIF1:YY1     |   0.448826 |      -2318 |              626.5 |             0.000987 |                0.000877 |       0.590102 | trrust     |    -0.448826 |         2318 |
| WNT11:ZEB1   |  -0.123905 |       -149 |              116.5 |             0.000286 |                0.000573 |       0.114833 | trrust     |     0.123905 |          149 |
| WNT2:WNT5A   |   0.089682 |        -48 |               19.5 |             0.000134 |                4.4e-05  |       0.344828 | trrust     |    -0.089682 |           48 |
| WNT7B:XIAP   |   0.079064 |       -721 |              420   |             0.000723 |                0.000659 |       0.12     | trrust     |    -0.079064 |          721 |
| WRN:WT1      |   0.448826 |      -2318 |              777   |             0.001325 |                0.002087 |       0.511673 | trrust     |    -0.448826 |         2318 |
| WRN:XIAP     |   0.448826 |      -2318 |              712.5 |             0.001104 |                0.000989 |       0.543879 | trrust     |    -0.448826 |         2318 |
| WRN:XPC      |  -0.167924 |      -2318 |              707.5 |             0.001041 |                0.001499 |       0.770964 | trrust     |     0.167924 |         2318 |
| WRN:XPO1     |  -0.011415 |      -1343 |              455.5 |             0.00066  |                0.000367 |       0.345643 | trrust     |     0.011415 |         1343 |
| WRN:YY1      |   0.448826 |      -2318 |              731.5 |             0.001206 |                0.001207 |       0.546512 | trrust     |    -0.448826 |         2318 |
| WT1:WTAP     |  -0.179362 |       -739 |              466.5 |             0.000917 |                0.001757 |       0.061433 | trrust     |     0.179362 |          739 |
| WT1:XIAP     |   0.211056 |      -2318 |              813.5 |             0.001484 |                0.002416 |       0.740107 | trrust     |    -0.211056 |         2318 |
| WT1:XPC      |   0.448826 |      -2318 |              808.5 |             0.001422 |                0.002926 |       0.511215 | trrust     |    -0.448826 |         2318 |
| WT1:YY1      |  -0.417897 |      -2318 |              832.5 |             0.001586 |                0.002635 |       0.769394 | trrust     |     0.417897 |         2318 |
| WT1:ZEB1     |  -0.417897 |       -926 |              543   |             0.001089 |                0.00233  |       0.133612 | trrust     |     0.417897 |          926 |
| WT1:ZNF268   |  -0.008815 |       -174 |              465   |             0.000922 |                0.001757 |       0.05802  | trrust     |     0.008815 |          174 |
| WWOX:XRCC1   |   0.132382 |       -995 |              132   |             0.000243 |                0.000403 |       0.955556 | trrust     |    -0.132382 |          995 |
| WWOX:ZNF350  |   0.132382 |       -995 |              132   |             0.000232 |                2.2e-05  |       0.955556 | trrust     |    -0.132382 |          995 |
| XBP1:ZHX2    |  -0.226624 |       -211 |               72.5 |             0.000211 |                0.000101 |       0.132812 | trrust     |     0.226624 |          211 |
| XIAP:XPC     |   0.448826 |      -2318 |              744   |             0.0012   |                0.001828 |       0.535604 | trrust     |    -0.448826 |         2318 |
| XIAP:YY1     |   0.211056 |      -2318 |              768   |             0.001365 |                0.001537 |       0.804935 | trrust     |    -0.211056 |         2318 |
| XPC:XPO1     |   0.083392 |      -1343 |              487   |             0.000756 |                0.001206 |       0.234474 | trrust     |    -0.083392 |         1343 |
| XPC:YY1      |   0.448826 |      -2318 |              763   |             0.001302 |                0.002047 |       0.530592 | trrust     |    -0.448826 |         2318 |
| XPC:ZNF217   |  -0.067713 |       -632 |              410   |             0.000648 |                0.001169 |       0.108108 | trrust     |     0.067713 |          632 |
| XPC:ZNF750   |  -0.337597 |       -234 |              394   |             0.000636 |                0.001181 |       0.046481 | trrust     |     0.337597 |          234 |
| XRCC1:ZNF350 |   0.132382 |       -995 |              134   |             0.00025  |                0.000426 |       0.928058 | trrust     |    -0.132382 |          995 |
| YWHAQ:ZEB1   |  -0.134149 |      -1034 |              149   |             0.000328 |                0.000576 |       0.360731 | trrust     |     0.134149 |         1034 |
| YWHAQ:ZFHX3  |  -0.134149 |      -1034 |               84   |             0.000169 |                3e-06    |       0.787234 | trrust     |     0.134149 |         1034 |
| YY1:ZEB1     |  -0.417897 |       -926 |              497.5 |             0.00097  |                0.00145  |       0.142365 | trrust     |     0.417897 |          926 |
| YY1:ZNF175   |  -0.042965 |       -637 |              443   |             0.000833 |                0.000913 |       0.113065 | trrust     |     0.042965 |          637 |
| ZEB1:ZEB2    |  -0.087607 |         -6 |              108.5 |             0.000289 |                0.000577 |       0.028436 | trrust     |     0.087607 |            6 |
| ZEB1:ZFHX3   |  -0.134149 |      -1034 |              143   |             0.000314 |                0.000573 |       0.349057 | trrust     |     0.134149 |         1034 |


---

## File: graph_metric_benchmark_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/graph_metric_benchmark_summary.parquet`
- **Matrix Dimensions:** 108 rows × 23 columns

### 1. Data Schema & Quality Audit

| Column Name             | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:------------------------|:--------|-----------------:|-------------:|:---------|
| cohort                  | object  |              108 |            0 | 0.00%    |
| topology                | object  |              108 |            0 | 0.00%    |
| endpoint_type           | object  |              108 |            0 | 0.00%    |
| label_name              | object  |              108 |            0 | 0.00%    |
| metric_name             | object  |              108 |            0 | 0.00%    |
| score_column            | object  |              108 |            0 | 0.00%    |
| n_total                 | int64   |              108 |            0 | 0.00%    |
| n_positive              | float64 |               66 |           42 | 38.89%   |
| n_negative              | float64 |               66 |           42 | 38.89%   |
| positive_rate           | float64 |               66 |           42 | 38.89%   |
| roc_auc                 | float64 |               54 |           54 | 50.00%   |
| average_precision       | float64 |               66 |           42 | 38.89%   |
| spearman_rho            | float64 |               96 |           12 | 11.11%   |
| spearman_p              | float64 |               96 |           12 | 11.11%   |
| mannwhitney_p           | float64 |               54 |           54 | 50.00%   |
| top_3_positive_rate     | float64 |               66 |           42 | 38.89%   |
| top_5_positive_rate     | float64 |               66 |           42 | 38.89%   |
| top_10pct_positive_rate | float64 |               66 |           42 | 38.89%   |
| median_score_positive   | float64 |               66 |           42 | 38.89%   |
| median_score_negative   | float64 |               54 |           54 | 50.00%   |
| frame_type              | object  |              108 |            0 | 0.00%    |
| pearson_r               | float64 |               42 |           66 | 61.11%   |
| pearson_p               | float64 |               42 |           66 | 61.11%   |

### 2. Full Descriptive Summary Statistics

|                         |   count | unique   | top                         | freq   | mean         | std          | min       | 25%       | 50%       | 75%         | max          |
|:------------------------|--------:|:---------|:----------------------------|:-------|:-------------|:-------------|:----------|:----------|:----------|:------------|:-------------|
| cohort                  |     108 | 7        | internal_heldout            | 36     | —            | —            | —         | —         | —         | —           | —            |
| topology                |     108 | 3        | corum                       | 48     | —            | —            | —         | —         | —         | —           | —            |
| endpoint_type           |     108 | 2        | binary                      | 66     | —            | —            | —         | —         | —         | —           | —            |
| label_name              |     108 | 5        | same_direction_as_discovery | 24     | —            | —            | —         | —         | —         | —           | —            |
| metric_name             |     108 | 6        | hlrc                        | 18     | —            | —            | —         | —         | —         | —           | —            |
| score_column            |     108 | 6        | hlrc_score                  | 18     | —            | —            | —         | —         | —         | —           | —            |
| n_total                 |     108 | —        | —                           | —      | 10702.666667 | 22618.003105 | 9.000000  | 11.000000 | 11.000000 | 6236.000000 | 72411.000000 |
| n_positive              |      66 | —        | —                           | —      | 288.909091   | 681.283601   | 6.000000  | 8.000000  | 9.000000  | 204.000000  | 2370.000000  |
| n_negative              |      66 | —        | —                           | —      | 8470.000000  | 20255.143643 | 0.000000  | 2.000000  | 3.000000  | 6032.000000 | 70041.000000 |
| positive_rate           |      66 | —        | —                           | —      | 0.570699     | 0.361040     | 0.030432  | 0.032730  | 0.727273  | 0.818182    | 1.000000     |
| roc_auc                 |      54 | —        | —                           | —      | 0.553834     | 0.121101     | 0.277778  | 0.486695  | 0.541531  | 0.625000    | 0.833333     |
| average_precision       |      66 | —        | —                           | —      | 0.641491     | 0.383568     | 0.029413  | 0.049515  | 0.817408  | 0.909634    | 1.000000     |
| spearman_rho            |      96 | —        | —                           | —      | 0.116854     | 0.213307     | -0.501140 | -0.008937 | 0.028393  | 0.291042    | 0.527273     |
| spearman_p              |      96 | —        | —                           | —      | 0.377538     | 0.296826     | 0.000000  | 0.113227  | 0.346024  | 0.586760    | 1.000000     |
| mannwhitney_p           |      54 | —        | —                           | —      | 0.394823     | 0.299667     | 0.000000  | 0.187879  | 0.323160  | 0.677634    | 1.000000     |
| top_3_positive_rate     |      66 | —        | —                           | —      | 0.636364     | 0.408153     | 0.000000  | 0.333333  | 0.666667  | 1.000000    | 1.000000     |
| top_5_positive_rate     |      66 | —        | —                           | —      | 0.609091     | 0.384998     | 0.000000  | 0.200000  | 0.800000  | 1.000000    | 1.000000     |
| top_10pct_positive_rate |      66 | —        | —                           | —      | 0.685168     | 0.426067     | 0.016026  | 0.070733  | 1.000000  | 1.000000    | 1.000000     |
| median_score_positive   |      66 | —        | —                           | —      | 70.028401    | 293.374521   | 0.000178  | 0.001456  | 0.240053  | 19.812500   | 2263.000000  |
| median_score_negative   |      54 | —        | —                           | —      | 80.029475    | 331.400729   | -0.391646 | 0.000744  | 0.200000  | 17.250000   | 2314.000000  |
| frame_type              |     108 | 1        | summary                     | 108    | —            | —            | —         | —         | —         | —           | —            |
| pearson_r               |      42 | —        | —                           | —      | 0.163247     | 0.311751     | -0.535715 | -0.005893 | 0.032056  | 0.454989    | 0.697062     |
| pearson_p               |      42 | —        | —                           | —      | 0.318413     | 0.269305     | 0.000000  | 0.091505  | 0.267044  | 0.488543    | 0.927773     |

### 3. Categorical Distribution Breakdown

**Column Grouping: `cohort`**

| Value Category                         |   Absolute Count | Percentage Proportion   |
|:---------------------------------------|-----------------:|:------------------------|
| internal_heldout                       |               36 | 33.33%                  |
| sanger_same_direction_as_discovery     |               12 | 11.11%                  |
| sanger_passes_external_nominal         |               12 | 11.11%                  |
| sanger_neg_delta_dependency            |               12 | 11.11%                  |
| depmap25q3_same_direction_as_discovery |               12 | 11.11%                  |
| depmap25q3_passes_external_nominal     |               12 | 11.11%                  |
| depmap25q3_neg_delta_dependency        |               12 | 11.11%                  |

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| corum            |               48 | 44.44%                  |
| string           |               48 | 44.44%                  |
| trrust           |               12 | 11.11%                  |

**Column Grouping: `endpoint_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| binary           |               66 | 61.11%                  |
| continuous       |               42 | 38.89%                  |

**Column Grouping: `label_name`**

| Value Category              |   Absolute Count | Percentage Proportion   |
|:----------------------------|-----------------:|:------------------------|
| same_direction_as_discovery |               24 | 22.22%                  |
| passes_external_nominal     |               24 | 22.22%                  |
| external_delta_dependency   |               24 | 22.22%                  |
| passes_validation_nominal   |               18 | 16.67%                  |
| delta_dependency            |               18 | 16.67%                  |

**Column Grouping: `metric_name`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| hlrc             |               18 | 16.67%                  |
| hfrc             |               18 | 16.67%                  |
| pagerank         |               18 | 16.67%                  |
| betweenness      |               18 | 16.67%                  |
| jaccard          |               18 | 16.67%                  |
| degree           |               18 | 16.67%                  |

**Column Grouping: `score_column`**

| Value Category        |   Absolute Count | Percentage Proportion   |
|:----------------------|-----------------:|:------------------------|
| hlrc_score            |               18 | 16.67%                  |
| hfrc_score            |               18 | 16.67%                  |
| pair_pagerank_mean    |               18 | 16.67%                  |
| pair_betweenness_mean |               18 | 16.67%                  |
| pair_jaccard          |               18 | 16.67%                  |
| pair_degree_mean      |               18 | 16.67%                  |

### 4. Significant Signals & Key Highlights

- 📊 **Concordance Metric Profile (`positive_rate`):** Mean=0.57070, Max=1.00000, Min=0.03043
- 📊 **Concordance Metric Profile (`top_3_positive_rate`):** Mean=0.63636, Max=1.00000, Min=0.00000
- 📊 **Concordance Metric Profile (`top_5_positive_rate`):** Mean=0.60909, Max=1.00000, Min=0.00000
- 📊 **Concordance Metric Profile (`top_10pct_positive_rate`):** Mean=0.68517, Max=1.00000, Min=0.01603
- 📈 **Peak Performance Asset (`roc_auc`):** Maximal value observed is `0.83333`.
- 📈 **Peak Performance Asset (`average_precision`):** Maximal value observed is `1.00000`.
- 📈 **Peak Performance Asset (`spearman_rho`):** Maximal value observed is `0.52727`.
- 📈 **Peak Performance Asset (`spearman_p`):** Maximal value observed is `1.00000`.
- 📈 **Peak Performance Asset (`pearson_r`):** Maximal value observed is `0.69706`.

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (108 rows total):

| cohort                                 | topology   | endpoint_type   | label_name                  | metric_name   | score_column          |   n_total |   n_positive |   n_negative |   positive_rate |    roc_auc |   average_precision |   spearman_rho |   spearman_p |   mannwhitney_p |   top_3_positive_rate |   top_5_positive_rate |   top_10pct_positive_rate |   median_score_positive |   median_score_negative | frame_type   |   pearson_r |   pearson_p |
|:---------------------------------------|:-----------|:----------------|:----------------------------|:--------------|:----------------------|----------:|-------------:|-------------:|----------------:|-----------:|--------------------:|---------------:|-------------:|----------------:|----------------------:|----------------------:|--------------------------:|------------------------:|------------------------:|:-------------|------------:|------------:|
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | hlrc          | hlrc_score            |      6236 |          204 |         6032 |        0.032713 |   0.525762 |            0.036061 |       0.015875 |     0.210046 |        0.105014 |              0        |                   0   |                  0.040064 |                0.066159 |                0.040577 | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | hfrc          | hfrc_score            |      6236 |          204 |         6032 |        0.032713 |   0.480237 |            0.029413 |      -0.01218  |     0.336229 |        0.83191  |              0        |                   0   |                  0.016026 |               27.5      |               28        | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | pagerank      | pair_pagerank_mean    |      6236 |          204 |         6032 |        0.032713 |   0.488591 |            0.030545 |      -0.007031 |     0.578832 |        0.710611 |              0        |                   0   |                  0.017628 |                0.000478 |                0.000471 | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | betweenness   | pair_betweenness_mean |      6236 |          204 |         6032 |        0.032713 |   0.513138 |            0.033984 |       0.008101 |     0.522429 |        0.261199 |              0        |                   0   |                  0.025641 |                0.001759 |                0.001537 | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | jaccard       | pair_jaccard          |      6236 |          204 |         6032 |        0.032713 |   0.486062 |            0.031407 |      -0.008589 |     0.497668 |        0.751194 |              0        |                   0   |                  0.027244 |                0.191901 |                0.2      | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | binary          | passes_validation_nominal   | degree        | pair_degree_mean      |      6236 |          204 |         6032 |        0.032713 |   0.48973  |            0.031604 |      -0.006329 |     0.61727  |        0.691391 |              0        |                   0   |                  0.028846 |               12.75     |               13.5      | summary      |  nan        |  nan        |
| internal_heldout                       | corum      | continuous      | delta_dependency            | hlrc          | hlrc_score            |      6236 |          nan |          nan |      nan        | nan        |          nan        |      -0.008837 |     0.485349 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.007038 |    0.578443 |
| internal_heldout                       | corum      | continuous      | delta_dependency            | hfrc          | hfrc_score            |      6236 |          nan |          nan |      nan        | nan        |          nan        |      -0.030806 |     0.014984 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.037693 |    0.002911 |
| internal_heldout                       | corum      | continuous      | delta_dependency            | pagerank      | pair_pagerank_mean    |      6236 |          nan |          nan |      nan        | nan        |          nan        |      -0.032431 |     0.010431 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.016644 |    0.188793 |
| internal_heldout                       | corum      | continuous      | delta_dependency            | betweenness   | pair_betweenness_mean |      6236 |          nan |          nan |      nan        | nan        |          nan        |       0.000504 |     0.968237 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.02862  |    0.023814 |
| internal_heldout                       | corum      | continuous      | delta_dependency            | jaccard       | pair_jaccard          |      6236 |          nan |          nan |      nan        | nan        |          nan        |       0.004664 |     0.712702 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.007805 |    0.537747 |
| internal_heldout                       | corum      | continuous      | delta_dependency            | degree        | pair_degree_mean      |      6236 |          nan |          nan |      nan        | nan        |          nan        |      -0.024538 |     0.052665 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.002242 |    0.859476 |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | hlrc          | hlrc_score            |        11 |            9 |            2 |        0.818182 |   0.722222 |            0.943687 |       0.298142 |     0.373199 |        0.218182 |              1        |                   1   |                  1        |                0.314723 |               -0.252196 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | hfrc          | hfrc_score            |        11 |            9 |            2 |        0.818182 |   0.5      |            0.886588 |       0        |     1        |        0.545455 |              1        |                   0.8 |                  1        |               20        |               20        | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | pagerank      | pair_pagerank_mean    |        11 |            9 |            2 |        0.818182 |   0.5      |            0.832135 |       0        |     1        |        0.545455 |              0.666667 |                   0.8 |                  0.5      |                0.000525 |                0.000756 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | betweenness   | pair_betweenness_mean |        11 |            9 |            2 |        0.818182 |   0.333333 |            0.825381 |      -0.224117 |     0.507655 |        0.795836 |              0.666667 |                   0.8 |                  1        |                0.00074  |                0.011184 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | jaccard       | pair_jaccard          |        11 |            9 |            2 |        0.818182 |   0.555556 |            0.843871 |       0.074706 |     0.827198 |        0.452986 |              0.666667 |                   0.8 |                  0.5      |                0.2      |                0.29533  | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | corum      | binary          | same_direction_as_discovery | degree        | pair_degree_mean      |        11 |            9 |            2 |        0.818182 |   0.388889 |            0.853608 |      -0.149411 |     0.661049 |        0.722606 |              1        |                   0.8 |                  1        |               10.5      |               18.75     | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | hlrc          | hlrc_score            |        11 |            6 |            5 |        0.545455 |   0.6      |            0.73952  |       0.173205 |     0.610542 |        0.331169 |              0.666667 |                   0.6 |                  1        |                0.162169 |               -0.112745 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | hfrc          | hfrc_score            |        11 |            6 |            5 |        0.545455 |   0.6      |            0.775926 |       0.173205 |     0.610542 |        0.331169 |              1        |                   0.6 |                  1        |               36        |               20        | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | pagerank      | pair_pagerank_mean    |        11 |            6 |            5 |        0.545455 |   0.566667 |            0.697391 |       0.11547  |     0.735302 |        0.396104 |              0.666667 |                   0.6 |                  0.5      |                0.000811 |                0.000519 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | betweenness   | pair_betweenness_mean |        11 |            6 |            5 |        0.545455 |   0.466667 |            0.714226 |      -0.057867 |     0.865799 |        0.608144 |              0.666667 |                   0.6 |                  1        |                0.002326 |                0.000781 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | jaccard       | pair_jaccard          |        11 |            6 |            5 |        0.545455 |   0.55     |            0.649405 |       0.0868   |     0.799678 |        0.427403 |              0.333333 |                   0.6 |                  0.5      |                0.237681 |                0.2      | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | corum      | binary          | passes_external_nominal     | degree        | pair_degree_mean      |        11 |            6 |            5 |        0.545455 |   0.5      |            0.757576 |       0        |     1        |        0.53645  |              1        |                   0.6 |                  1        |               18        |               11        | summary      |  nan        |  nan        |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | hlrc          | hlrc_score            |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.266667 |     0.487922 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.306865 |    0.42186  |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | hfrc          | hfrc_score            |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.35     |     0.35582  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.07151  |    0.854941 |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | pagerank      | pair_pagerank_mean    |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.333333 |     0.380713 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.445816 |    0.229086 |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | betweenness   | pair_betweenness_mean |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.343099 |     0.366029 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.572369 |    0.107274 |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | jaccard       | pair_jaccard          |         9 |          nan |          nan |      nan        | nan        |          nan        |      -0.24268  |     0.529241 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.508329 |    0.16232  |
| sanger_neg_delta_dependency            | corum      | continuous      | external_delta_dependency   | degree        | pair_degree_mean      |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.142261 |     0.715032 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.258989 |    0.501001 |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | hlrc          | hlrc_score            |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.009615 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | hfrc          | hfrc_score            |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |               20        |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | pagerank      | pair_pagerank_mean    |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.000525 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | betweenness   | pair_betweenness_mean |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.000781 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | jaccard       | pair_jaccard          |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.2      |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | corum      | binary          | same_direction_as_discovery | degree        | pair_degree_mean      |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |               11        |              nan        | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | hlrc          | hlrc_score            |        11 |            8 |            3 |        0.727273 |   0.666667 |            0.855344 |       0.258199 |     0.443332 |        0.248485 |              0.666667 |                   0.8 |                  1        |                0.162169 |               -0.391646 | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | hfrc          | hfrc_score            |        11 |            8 |            3 |        0.727273 |   0.666667 |            0.870139 |       0.258199 |     0.443332 |        0.248485 |              1        |                   0.8 |                  1        |               24        |               12        | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | pagerank      | pair_pagerank_mean    |        11 |            8 |            3 |        0.727273 |   0.791667 |            0.938131 |       0.451848 |     0.162954 |        0.09697  |              1        |                   1   |                  1        |                0.000849 |                0.000345 | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | betweenness   | pair_betweenness_mean |        11 |            8 |            3 |        0.727273 |   0.625    |            0.890152 |       0.194091 |     0.567423 |        0.30451  |              1        |                   1   |                  1        |                0.003104 |                0.00074  | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | jaccard       | pair_jaccard          |        11 |            8 |            3 |        0.727273 |   0.333333 |            0.713231 |      -0.258788 |     0.442256 |        0.821384 |              0.333333 |                   0.6 |                  0.5      |                0.2      |                0.5      | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | corum      | binary          | passes_external_nominal     | degree        | pair_degree_mean      |        11 |            8 |            3 |        0.727273 |   0.625    |            0.890909 |       0.194091 |     0.567423 |        0.30451  |              1        |                   1   |                  1        |               19.25     |               10.5      | summary      |  nan        |  nan        |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | hlrc          | hlrc_score            |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.372727 |     0.258926 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.524326 |    0.097776 |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | hfrc          | hfrc_score            |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.354545 |     0.284693 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.290607 |    0.385974 |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | pagerank      | pair_pagerank_mean    |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.445455 |     0.169733 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.697062 |    0.017128 |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | betweenness   | pair_betweenness_mean |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.478361 |     0.136651 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.684711 |    0.020098 |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | jaccard       | pair_jaccard          |        11 |          nan |          nan |      nan        | nan        |          nan        |      -0.50114  |     0.116339 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.535715 |    0.089415 |
| depmap25q3_neg_delta_dependency        | corum      | continuous      | external_delta_dependency   | degree        | pair_degree_mean      |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.277905 |     0.407993 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.518501 |    0.102243 |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | hlrc          | hlrc_score            |     17613 |          536 |        17077 |        0.030432 |   0.538328 |            0.035213 |       0.022807 |     0.00247  |        0.001236 |              0        |                   0   |                  0.04143  |                0.678009 |                0.607843 | summary      |  nan        |  nan        |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | hfrc          | hfrc_score            |     17613 |          536 |        17077 |        0.030432 |   0.513859 |            0.032079 |       0.008247 |     0.273781 |        0.136885 |              0        |                   0   |                  0.030647 |              359        |              360        | summary      |  nan        |  nan        |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | pagerank      | pair_pagerank_mean    |     17613 |          536 |        17077 |        0.030432 |   0.533183 |            0.041715 |       0.019745 |     0.008779 |        0.004391 |              0        |                   0   |                  0.053348 |                0.000219 |                0.000215 | summary      |  nan        |  nan        |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | betweenness   | pair_betweenness_mean |     17613 |          536 |        17077 |        0.030432 |   0.537525 |            0.049378 |       0.022329 |     0.003041 |        0.001522 |              0        |                   0   |                  0.052781 |                0.000966 |                0.000836 | summary      |  nan        |  nan        |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | jaccard       | pair_jaccard          |     17613 |          536 |        17077 |        0.030432 |   0.475613 |            0.029657 |      -0.014514 |     0.054078 |        0.97296  |              0        |                   0   |                  0.031782 |                0.11279  |                0.139073 | summary      |  nan        |  nan        |
| internal_heldout                       | string     | binary          | passes_validation_nominal   | degree        | pair_degree_mean      |     17613 |          536 |        17077 |        0.030432 |   0.533766 |            0.037557 |       0.020092 |     0.007662 |        0.003833 |              0        |                   0   |                  0.059024 |               43.75     |               41        | summary      |  nan        |  nan        |
| internal_heldout                       | string     | continuous      | delta_dependency            | hlrc          | hlrc_score            |     17613 |          nan |          nan |      nan        | nan        |          nan        |       0.02881  |     0.000131 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.040723 |    0        |
| internal_heldout                       | string     | continuous      | delta_dependency            | hfrc          | hfrc_score            |     17613 |          nan |          nan |      nan        | nan        |          nan        |      -0.012692 |     0.092111 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.005965 |    0.428576 |
| internal_heldout                       | string     | continuous      | delta_dependency            | pagerank      | pair_pagerank_mean    |     17613 |          nan |          nan |      nan        | nan        |          nan        |      -0.012391 |     0.10008  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.008335 |    0.268659 |
| internal_heldout                       | string     | continuous      | delta_dependency            | betweenness   | pair_betweenness_mean |     17613 |          nan |          nan |      nan        | nan        |          nan        |       0.00046  |     0.951311 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.002351 |    0.755001 |
| internal_heldout                       | string     | continuous      | delta_dependency            | jaccard       | pair_jaccard          |     17613 |          nan |          nan |      nan        | nan        |          nan        |      -0.010864 |     0.149359 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.005678 |    0.451169 |
| internal_heldout                       | string     | continuous      | delta_dependency            | degree        | pair_degree_mean      |     17613 |          nan |          nan |      nan        | nan        |          nan        |      -0.019636 |     0.009158 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.022454 |    0.002882 |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | hlrc          | hlrc_score            |        11 |            9 |            2 |        0.818182 |   0.444444 |            0.864366 |      -0.074536 |     0.827586 |        0.636364 |              1        |                   0.8 |                  1        |                0.703995 |                0.76602  | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | hfrc          | hfrc_score            |        11 |            9 |            2 |        0.818182 |   0.388889 |            0.811456 |      -0.149071 |     0.66178  |        0.709091 |              0.666667 |                   0.8 |                  0.5      |              172        |              577.5      | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | pagerank      | pair_pagerank_mean    |        11 |            9 |            2 |        0.818182 |   0.388889 |            0.836588 |      -0.149071 |     0.66178  |        0.709091 |              0.666667 |                   0.8 |                  1        |                0.000178 |                0.000427 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | betweenness   | pair_betweenness_mean |        11 |            9 |            2 |        0.818182 |   0.277778 |            0.808546 |      -0.298142 |     0.373199 |        0.836364 |              0.666667 |                   0.6 |                  1        |                0.000434 |                0.006504 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | jaccard       | pair_jaccard          |        11 |            9 |            2 |        0.818182 |   0.666667 |            0.906041 |       0.223607 |     0.508646 |        0.290909 |              1        |                   0.8 |                  1        |                0.242424 |                0.230355 | summary      |  nan        |  nan        |
| sanger_same_direction_as_discovery     | string     | binary          | same_direction_as_discovery | degree        | pair_degree_mean      |        11 |            9 |            2 |        0.818182 |   0.333333 |            0.823361 |      -0.223607 |     0.508646 |        0.781818 |              0.666667 |                   0.8 |                  1        |               20.5      |               58.5      | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | hlrc          | hlrc_score            |        11 |            6 |            5 |        0.545455 |   0.566667 |            0.766835 |       0.11547  |     0.735302 |        0.396104 |              1        |                   0.6 |                  1        |                0.697096 |                0.703995 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | hfrc          | hfrc_score            |        11 |            6 |            5 |        0.545455 |   0.6      |            0.706481 |       0.173205 |     0.610542 |        0.331169 |              0.666667 |                   0.6 |                  0.5      |              321.5      |              142        | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | pagerank      | pair_pagerank_mean    |        11 |            6 |            5 |        0.545455 |   0.633333 |            0.762037 |       0.23094  |     0.494466 |        0.268398 |              0.666667 |                   0.6 |                  1        |                0.000234 |                0.000165 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | betweenness   | pair_betweenness_mean |        11 |            6 |            5 |        0.545455 |   0.633333 |            0.762037 |       0.23094  |     0.494466 |        0.268398 |              0.666667 |                   0.6 |                  1        |                0.001456 |                0.000434 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | jaccard       | pair_jaccard          |        11 |            6 |            5 |        0.545455 |   0.666667 |            0.759722 |       0.288675 |     0.389283 |        0.214286 |              0.666667 |                   0.6 |                  1        |                0.287879 |                0.185185 | summary      |  nan        |  nan        |
| sanger_passes_external_nominal         | string     | binary          | passes_external_nominal     | degree        | pair_degree_mean      |        11 |            6 |            5 |        0.545455 |   0.533333 |            0.727814 |       0.057735 |     0.866102 |        0.465368 |              0.666667 |                   0.6 |                  1        |               46.25     |               21.5      | summary      |  nan        |  nan        |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | hlrc          | hlrc_score            |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.433333 |     0.243952 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.361157 |    0.339609 |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | hfrc          | hfrc_score            |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.466667 |     0.205386 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.035492 |    0.927773 |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | pagerank      | pair_pagerank_mean    |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.466667 |     0.205386 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.488381 |    0.182224 |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | betweenness   | pair_betweenness_mean |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.433333 |     0.243952 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.458047 |    0.215011 |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | jaccard       | pair_jaccard          |         9 |          nan |          nan |      nan        | nan        |          nan        |      -0.033333 |     0.932157 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.416001 |    0.265429 |
| sanger_neg_delta_dependency            | string     | continuous      | external_delta_dependency   | degree        | pair_degree_mean      |         9 |          nan |          nan |      nan        | nan        |          nan        |       0.366667 |     0.33174  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.373526 |    0.32207  |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | hlrc          | hlrc_score            |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.703995 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | hfrc          | hfrc_score            |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |              172        |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | pagerank      | pair_pagerank_mean    |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.000178 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | betweenness   | pair_betweenness_mean |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.000559 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | jaccard       | pair_jaccard          |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |                0.242424 |              nan        | summary      |  nan        |  nan        |
| depmap25q3_same_direction_as_discovery | string     | binary          | same_direction_as_discovery | degree        | pair_degree_mean      |        11 |           11 |            0 |        1        | nan        |            1        |     nan        |   nan        |      nan        |              1        |                   1   |                  1        |               21.5      |              nan        | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | hlrc          | hlrc_score            |        11 |            8 |            3 |        0.727273 |   0.708333 |            0.906881 |       0.322749 |     0.333021 |        0.187879 |              1        |                   1   |                  1        |                0.787106 |                0.684376 | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | hfrc          | hfrc_score            |        11 |            8 |            3 |        0.727273 |   0.833333 |            0.947222 |       0.516398 |     0.103888 |        0.066667 |              1        |                   1   |                  1        |              326        |               92        | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | pagerank      | pair_pagerank_mean    |        11 |            8 |            3 |        0.727273 |   0.833333 |            0.947222 |       0.516398 |     0.103888 |        0.066667 |              1        |                   1   |                  1        |                0.00024  |                0.00016  | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | betweenness   | pair_betweenness_mean |        11 |            8 |            3 |        0.727273 |   0.708333 |            0.895139 |       0.322749 |     0.333021 |        0.187879 |              1        |                   0.8 |                  1        |                0.001456 |                0.000434 | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | jaccard       | pair_jaccard          |        11 |            8 |            3 |        0.727273 |   0.625    |            0.861048 |       0.193649 |     0.568322 |        0.315152 |              1        |                   0.8 |                  1        |                0.287879 |                0.185185 | summary      |  nan        |  nan        |
| depmap25q3_passes_external_nominal     | string     | binary          | passes_external_nominal     | degree        | pair_degree_mean      |        11 |            8 |            3 |        0.727273 |   0.708333 |            0.910552 |       0.322749 |     0.333021 |        0.187879 |              1        |                   1   |                  1        |               48        |               18.5      | summary      |  nan        |  nan        |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | hlrc          | hlrc_score            |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.481818 |     0.133434 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.51956  |    0.101421 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | hfrc          | hfrc_score            |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.490909 |     0.125204 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.157101 |    0.644574 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | pagerank      | pair_pagerank_mean    |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.527273 |     0.095565 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.633301 |    0.036459 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | betweenness   | pair_betweenness_mean |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.327273 |     0.325895 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.572567 |    0.065636 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | jaccard       | pair_jaccard          |        11 |          nan |          nan |      nan        | nan        |          nan        |      -0.154545 |     0.650034 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.199552 |    0.556351 |
| depmap25q3_neg_delta_dependency        | string     | continuous      | external_delta_dependency   | degree        | pair_degree_mean      |        11 |          nan |          nan |      nan        | nan        |          nan        |       0.418182 |     0.20057  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.567469 |    0.068636 |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | hlrc          | hlrc_score            |     72411 |         2370 |        70041 |        0.03273  |   0.544734 |            0.038195 |       0.027976 |     0        |        0        |              0        |                   0   |                  0.044325 |                0.00261  |               -0.083392 | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | hfrc          | hfrc_score            |     72411 |         2370 |        70041 |        0.03273  |   0.485493 |            0.031055 |      -0.009235 |     0.012955 |        0.993522 |              0.333333 |                   0.2 |                  0.032864 |             2263        |             2314        | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | pagerank      | pair_pagerank_mean    |     72411 |         2370 |        70041 |        0.03273  |   0.594916 |            0.049926 |       0.058503 |     0        |        0        |              0        |                   0.2 |                  0.07208  |                0.001158 |                0.000924 | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | betweenness   | pair_betweenness_mean |     72411 |         2370 |        70041 |        0.03273  |   0.587114 |            0.046248 |       0.053694 |     0        |        0        |              0        |                   0   |                  0.070284 |                0.002124 |                0.001121 | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | jaccard       | pair_jaccard          |     72411 |         2370 |        70041 |        0.03273  |   0.460625 |            0.029652 |      -0.024269 |     0        |        1        |              0.333333 |                   0.2 |                  0.02596  |                0.362719 |                0.416111 | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | binary          | passes_validation_nominal   | degree        | pair_degree_mean      |     72411 |         2370 |        70041 |        0.03273  |   0.576699 |            0.044153 |       0.047275 |     0        |        0        |              0        |                   0   |                  0.051091 |              622.5      |              558.5      | summary      |  nan        |  nan        |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | hlrc          | hlrc_score            |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.004648 |     0.211057 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.002924 |    0.431418 |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | hfrc          | hfrc_score            |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.005496 |     0.139147 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.0037   |    0.319411 |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | pagerank      | pair_pagerank_mean    |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.017998 |     1e-06    |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.002094 |    0.57315  |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | betweenness   | pair_betweenness_mean |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.014751 |     7.2e-05  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |   -0.007592 |    0.041062 |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | jaccard       | pair_jaccard          |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.000967 |     0.794627 |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.001037 |    0.780242 |
| internal_heldout                       | trrust     | continuous      | delta_dependency            | degree        | pair_degree_mean      |     72411 |          nan |          nan |      nan        | nan        |          nan        |       0.016047 |     1.6e-05  |      nan        |            nan        |                 nan   |                nan        |              nan        |              nan        | summary      |    0.003021 |    0.416273 |


---

## File: phase13_cross_topology_families.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_cross_topology_families.parquet`
- **Matrix Dimensions:** 11 rows × 11 columns

### 1. Data Schema & Quality Audit

| Column Name             | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:------------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key          | object  |               11 |            0 | 0.00%    |
| gene_a                  | object  |               11 |            0 | 0.00%    |
| gene_b                  | object  |               11 |            0 | 0.00%    |
| mutation_gene           | object  |               11 |            0 | 0.00%    |
| partner_gene            | object  |               11 |            0 | 0.00%    |
| corum_mutation_type     | object  |               11 |            0 | 0.00%    |
| string_mutation_type    | object  |               11 |            0 | 0.00%    |
| corum_delta_dependency  | float64 |               11 |            0 | 0.00%    |
| string_delta_dependency | float64 |               11 |            0 | 0.00%    |
| corum_min_hlrc          | float64 |               11 |            0 | 0.00%    |
| string_min_hlrc         | float64 |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                         |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:------------------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| undirected_key          |      11 | 11       | AP3B2:AP3M2 | 1      | —         | —        | —         | —         | —         | —         | —         |
| gene_a                  |      11 | 11       | AP3B2       | 1      | —         | —        | —         | —         | —         | —         | —         |
| gene_b                  |      11 | 11       | AP3M2       | 1      | —         | —        | —         | —         | —         | —         | —         |
| mutation_gene           |      11 | 11       | AP3B2       | 1      | —         | —        | —         | —         | —         | —         | —         |
| partner_gene            |      11 | 11       | AP3M2       | 1      | —         | —        | —         | —         | —         | —         | —         |
| corum_mutation_type     |      11 | 2        | damaging    | 8      | —         | —        | —         | —         | —         | —         | —         |
| string_mutation_type    |      11 | 2        | damaging    | 8      | —         | —        | —         | —         | —         | —         | —         |
| corum_delta_dependency  |      11 | —        | —           | —      | -0.330867 | 0.250404 | -0.927101 | -0.428322 | -0.370856 | -0.115480 | -0.067571 |
| string_delta_dependency |      11 | —        | —           | —      | -0.330867 | 0.250404 | -0.927101 | -0.428322 | -0.370856 | -0.115480 | -0.067571 |
| corum_min_hlrc          |      11 | —        | —           | —      | -0.031677 | 0.578861 | -0.817335 | -0.498723 | -0.009615 | 0.351379  | 1.000000  |
| string_min_hlrc         |      11 | —        | —           | —      | -0.567756 | 0.418496 | -0.936707 | -0.858169 | -0.703995 | -0.514974 | 0.274242  |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

**Column Grouping: `gene_a`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2            |                1 | 9.09%                   |
| APC              |                1 | 9.09%                   |
| BRAF             |                1 | 9.09%                   |
| CD151            |                1 | 9.09%                   |
| CREBBP           |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| DCP2             |                1 | 9.09%                   |
| IFT122           |                1 | 9.09%                   |
| IL2              |                1 | 9.09%                   |
| NRAS             |                1 | 9.09%                   |
| SMARCA2          |                1 | 9.09%                   |

**Column Grouping: `gene_b`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3M2            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| MAP2K1           |                1 | 9.09%                   |
| ITGA6            |                1 | 9.09%                   |
| EP300            |                1 | 9.09%                   |
| TCF7L2           |                1 | 9.09%                   |
| XRN1             |                1 | 9.09%                   |
| WDR35            |                1 | 9.09%                   |
| IL2RG            |                1 | 9.09%                   |
| SHOC2            |                1 | 9.09%                   |
| SMARCA4          |                1 | 9.09%                   |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2            |                1 | 9.09%                   |
| APC              |                1 | 9.09%                   |
| BRAF             |                1 | 9.09%                   |
| ITGA6            |                1 | 9.09%                   |
| EP300            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| DCP2             |                1 | 9.09%                   |
| IFT122           |                1 | 9.09%                   |
| IL2RG            |                1 | 9.09%                   |
| NRAS             |                1 | 9.09%                   |
| SMARCA4          |                1 | 9.09%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3M2            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| MAP2K1           |                1 | 9.09%                   |
| CD151            |                1 | 9.09%                   |
| CREBBP           |                1 | 9.09%                   |
| TCF7L2           |                1 | 9.09%                   |
| XRN1             |                1 | 9.09%                   |
| WDR35            |                1 | 9.09%                   |
| IL2              |                1 | 9.09%                   |
| SHOC2            |                1 | 9.09%                   |
| SMARCA2          |                1 | 9.09%                   |

**Column Grouping: `corum_mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                8 | 72.73%                  |
| hotspot          |                3 | 27.27%                  |

**Column Grouping: `string_mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                8 | 72.73%                  |
| hotspot          |                3 | 27.27%                  |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| undirected_key   | gene_a   | gene_b   | mutation_gene   | partner_gene   | corum_mutation_type   | string_mutation_type   |   corum_delta_dependency |   string_delta_dependency |   corum_min_hlrc |   string_min_hlrc |
|:-----------------|:---------|:---------|:----------------|:---------------|:----------------------|:-----------------------|-------------------------:|--------------------------:|-----------------:|------------------:|
| AP3B2:AP3M2      | AP3B2    | AP3M2    | AP3B2           | AP3M2          | damaging              | damaging               |                -0.067571 |                 -0.067571 |         0.623737 |          0.181667 |
| APC:CTNNB1       | APC      | CTNNB1   | APC             | CTNNB1         | damaging              | damaging               |                -0.927101 |                 -0.927101 |        -0.648562 |         -0.903316 |
| BRAF:MAP2K1      | BRAF     | MAP2K1   | BRAF            | MAP2K1         | hotspot               | hotspot                |                -0.390174 |                 -0.390174 |        -0.387723 |         -0.726548 |
| CD151:ITGA6      | CD151    | ITGA6    | ITGA6           | CD151          | damaging              | damaging               |                -0.093867 |                 -0.093867 |        -0.609722 |         -0.703995 |
| CREBBP:EP300     | CREBBP   | EP300    | EP300           | CREBBP         | damaging              | damaging               |                -0.370856 |                 -0.370856 |        -0.817335 |         -0.936707 |
| CTNNB1:TCF7L2    | CTNNB1   | TCF7L2   | CTNNB1          | TCF7L2         | hotspot               | hotspot                |                -0.46647  |                 -0.46647  |         0.112745 |         -0.847663 |
| DCP2:XRN1        | DCP2     | XRN1     | DCP2            | XRN1           | damaging              | damaging               |                -0.244932 |                 -0.244932 |         0.391646 |         -0.684376 |
| IFT122:WDR35     | IFT122   | WDR35    | IFT122          | WDR35          | damaging              | damaging               |                -0.115395 |                 -0.115395 |         1        |          0.274242 |
| IL2:IL2RG        | IL2      | IL2RG    | IL2RG           | IL2            | damaging              | damaging               |                -0.115564 |                 -0.115564 |         0.311111 |         -0.504431 |
| NRAS:SHOC2       | NRAS     | SHOC2    | NRAS            | SHOC2          | hotspot               | hotspot                |                -0.474233 |                 -0.474233 |        -0.009615 |         -0.525517 |
| SMARCA2:SMARCA4  | SMARCA2  | SMARCA4  | SMARCA4         | SMARCA2        | damaging              | damaging               |                -0.373378 |                 -0.373378 |        -0.314723 |         -0.868675 |


---

## File: phase13_degree_preserving_shuffle_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_degree_preserving_shuffle_summary.parquet`
- **Matrix Dimensions:** 2 rows × 6 columns

### 1. Data Schema & Quality Audit

| Column Name      | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------|:--------|-----------------:|-------------:|:---------|
| metric           | object  |                2 |            0 | 0.00%    |
| observed_count   | int64   |                2 |            0 | 0.00%    |
| observed_value   | float64 |                2 |            0 | 0.00%    |
| null_mean        | float64 |                2 |            0 | 0.00%    |
| empirical_p_less | float64 |                2 |            0 | 0.00%    |
| topology         | object  |                2 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                  |   count | unique   | top   | freq   | mean        | std         | min        | 25%        | 50%         | 75%         | max         |
|:-----------------|--------:|:---------|:------|:-------|:------------|:------------|:-----------|:-----------|:------------|:------------|:------------|
| metric           |       2 | 1        | hlrc  | 2      | —           | —           | —          | —          | —           | —           | —           |
| observed_count   |       2 | —        | —     | —      | 1117.000000 | 1377.444010 | 143.000000 | 630.000000 | 1117.000000 | 1604.000000 | 2091.000000 |
| observed_value   |       2 | —        | —     | —      | -0.415353   | 0.212914    | -0.565906  | -0.490630  | -0.415353   | -0.340077   | -0.264801   |
| null_mean        |       2 | —        | —     | —      | 0.368429    | 0.386298    | 0.095275   | 0.231852   | 0.368429    | 0.505006    | 0.641583    |
| empirical_p_less |       2 | —        | —     | —      | 0.000000    | 0.000000    | 0.000000   | 0.000000   | 0.000000    | 0.000000    | 0.000000    |
| topology         |       2 | 2        | CORUM | 1      | —           | —           | —          | —          | —           | —           | —           |

### 3. Categorical Distribution Breakdown

**Column Grouping: `topology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CORUM            |                1 | 50.0%                   |
| STRING           |                1 | 50.0%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (2 rows total):

| metric   |   observed_count |   observed_value |   null_mean |   empirical_p_less | topology   |
|:---------|-----------------:|-----------------:|------------:|-------------------:|:-----------|
| hlrc     |              143 |        -0.264801 |    0.095275 |                  0 | CORUM      |
| hlrc     |             2091 |        -0.565906 |    0.641583 |                  0 | STRING     |


---

## File: phase13_external_cmp_sanger_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_external_cmp_sanger_summary.parquet`
- **Matrix Dimensions:** 1 rows × 17 columns

### 1. Data Schema & Quality Audit

| Column Name             | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:------------------------|:--------|-----------------:|-------------:|:---------|
| context                 | object  |                1 |            0 | 0.00%    |
| n_total_families        | int64   |                1 |            0 | 0.00%    |
| n_testable_families     | int64   |                1 |            0 | 0.00%    |
| n_concordant_families   | int64   |                1 |            0 | 0.00%    |
| concordance_rate        | float64 |                1 |            0 | 0.00%    |
| concordance_ci_low      | float64 |                1 |            0 | 0.00%    |
| concordance_ci_high     | float64 |                1 |            0 | 0.00%    |
| n_nominally_significant | int64   |                1 |            0 | 0.00%    |
| meta_mu                 | float64 |                1 |            0 | 0.00%    |
| meta_se                 | float64 |                1 |            0 | 0.00%    |
| meta_ci_low             | float64 |                1 |            0 | 0.00%    |
| meta_ci_high            | float64 |                1 |            0 | 0.00%    |
| meta_p                  | float64 |                1 |            0 | 0.00%    |
| meta_i2                 | float64 |                1 |            0 | 0.00%    |
| bayes_p_negative        | float64 |                1 |            0 | 0.00%    |
| bayes_mu_mean           | float64 |                1 |            0 | 0.00%    |
| bayes_rhat_mu           | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                         |   count | unique   | top    | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:------------------------|--------:|:---------|:-------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| context                 |       1 | 1        | Sanger | 1      | —         | —     | —         | —         | —         | —         | —         |
| n_total_families        |       1 | —        | —      | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| n_testable_families     |       1 | —        | —      | —      | 10.000000 | —     | 10.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 |
| n_concordant_families   |       1 | —        | —      | —      | 9.000000  | —     | 9.000000  | 9.000000  | 9.000000  | 9.000000  | 9.000000  |
| concordance_rate        |       1 | —        | —      | —      | 0.900000  | —     | 0.900000  | 0.900000  | 0.900000  | 0.900000  | 0.900000  |
| concordance_ci_low      |       1 | —        | —      | —      | 0.595844  | —     | 0.595844  | 0.595844  | 0.595844  | 0.595844  | 0.595844  |
| concordance_ci_high     |       1 | —        | —      | —      | 0.982124  | —     | 0.982124  | 0.982124  | 0.982124  | 0.982124  | 0.982124  |
| n_nominally_significant |       1 | —        | —      | —      | 6.000000  | —     | 6.000000  | 6.000000  | 6.000000  | 6.000000  | 6.000000  |
| meta_mu                 |       1 | —        | —      | —      | -2.371364 | —     | -2.371364 | -2.371364 | -2.371364 | -2.371364 | -2.371364 |
| meta_se                 |       1 | —        | —      | —      | 0.639285  | —     | 0.639285  | 0.639285  | 0.639285  | 0.639285  | 0.639285  |
| meta_ci_low             |       1 | —        | —      | —      | -3.624362 | —     | -3.624362 | -3.624362 | -3.624362 | -3.624362 | -3.624362 |
| meta_ci_high            |       1 | —        | —      | —      | -1.118366 | —     | -1.118366 | -1.118366 | -1.118366 | -1.118366 | -1.118366 |
| meta_p                  |       1 | —        | —      | —      | 0.000208  | —     | 0.000208  | 0.000208  | 0.000208  | 0.000208  | 0.000208  |
| meta_i2                 |       1 | —        | —      | —      | 0.878410  | —     | 0.878410  | 0.878410  | 0.878410  | 0.878410  | 0.878410  |
| bayes_p_negative        |       1 | —        | —      | —      | 0.988800  | —     | 0.988800  | 0.988800  | 0.988800  | 0.988800  | 0.988800  |
| bayes_mu_mean           |       1 | —        | —      | —      | -2.514229 | —     | -2.514229 | -2.514229 | -2.514229 | -2.514229 | -2.514229 |
| bayes_rhat_mu           |       1 | —        | —      | —      | 0.999822  | —     | 0.999822  | 0.999822  | 0.999822  | 0.999822  | 0.999822  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **1** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context   |   n_total_families |   n_testable_families |   n_concordant_families |   concordance_rate |   concordance_ci_low |   concordance_ci_high |   n_nominally_significant |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   bayes_p_negative |   bayes_mu_mean |   bayes_rhat_mu |
|:----------|-------------------:|----------------------:|------------------------:|-------------------:|---------------------:|----------------------:|--------------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|-------------------:|----------------:|----------------:|
| Sanger    |                 11 |                    10 |                       9 |                0.9 |             0.595844 |              0.982124 |                         6 |  -2.37136 |  0.639285 |      -3.62436 |       -1.11837 | 0.000208 |   0.87841 |             0.9888 |        -2.51423 |        0.999822 |

- 📊 **Concordance Metric Profile (`concordance_rate`):** Mean=0.90000, Max=0.90000, Min=0.90000
- 📊 **Concordance Metric Profile (`concordance_ci_low`):** Mean=0.59584, Max=0.59584, Min=0.59584
- 📊 **Concordance Metric Profile (`concordance_ci_high`):** Mean=0.98212, Max=0.98212, Min=0.98212

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| context   |   n_total_families |   n_testable_families |   n_concordant_families |   concordance_rate |   concordance_ci_low |   concordance_ci_high |   n_nominally_significant |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   bayes_p_negative |   bayes_mu_mean |   bayes_rhat_mu |
|:----------|-------------------:|----------------------:|------------------------:|-------------------:|---------------------:|----------------------:|--------------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|-------------------:|----------------:|----------------:|
| Sanger    |                 11 |                    10 |                       9 |                0.9 |             0.595844 |              0.982124 |                         6 |  -2.37136 |  0.639285 |      -3.62436 |       -1.11837 | 0.000208 |   0.87841 |             0.9888 |        -2.51423 |        0.999822 |


---

## File: phase13_external_cmp_sanger_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_external_cmp_sanger_validation.parquet`
- **Matrix Dimensions:** 11 rows × 12 columns

### 1. Data Schema & Quality Audit

| Column Name                 | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key              | object  |               11 |            0 | 0.00%    |
| mutation_gene               | object  |               11 |            0 | 0.00%    |
| partner_gene                | object  |               11 |            0 | 0.00%    |
| mutation_type               | object  |               11 |            0 | 0.00%    |
| external_delta_dependency   | float64 |                9 |            2 | 18.18%   |
| external_p_value            | float64 |                9 |            2 | 18.18%   |
| external_num_mutant         | int64   |               11 |            0 | 0.00%    |
| external_num_wildtype       | int64   |               11 |            0 | 0.00%    |
| external_se                 | float64 |                9 |            2 | 18.18%   |
| same_direction_as_discovery | bool    |               11 |            0 | 0.00%    |
| passes_external_nominal     | bool    |               11 |            0 | 0.00%    |
| external_gene_available     | bool    |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                             |   count | unique   | top         | freq   | mean       | std       | min       | 25%        | 50%        | 75%        | max        |
|:----------------------------|--------:|:---------|:------------|:-------|:-----------|:----------|:----------|:-----------|:-----------|:-----------|:-----------|
| undirected_key              |      11 | 11       | AP3B2:AP3M2 | 1      | —          | —         | —         | —          | —          | —          | —          |
| mutation_gene               |      11 | 11       | AP3B2       | 1      | —          | —         | —         | —          | —          | —          | —          |
| partner_gene                |      11 | 11       | AP3M2       | 1      | —          | —         | —         | —          | —          | —          | —          |
| mutation_type               |      11 | 2        | damaging    | 8      | —          | —         | —         | —          | —          | —          | —          |
| external_delta_dependency   |       9 | —        | —           | —      | -2.794659  | 3.246963  | -9.320826 | -2.703582  | -1.577966  | -0.601137  | -0.182734  |
| external_p_value            |       9 | —        | —           | —      | 0.114875   | 0.164178  | 0.000000  | 0.001653   | 0.014770   | 0.284608   | 0.408136   |
| external_num_mutant         |      11 | —        | —           | —      | 15.363636  | 16.983950 | 0.000000  | 4.500000   | 11.000000  | 19.500000  | 59.000000  |
| external_num_wildtype       |      11 | —        | —           | —      | 276.454545 | 93.110003 | 0.000000  | 296.500000 | 307.000000 | 315.500000 | 319.000000 |
| external_se                 |       9 | —        | —           | —      | 0.932982   | 0.524553  | 0.331161  | 0.419397   | 0.922898   | 1.287535   | 1.880686   |
| same_direction_as_discovery |      11 | 2        | True        | 9      | —          | —         | —         | —          | —          | —          | —          |
| passes_external_nominal     |      11 | 2        | True        | 6      | —          | —         | —         | —          | —          | —          | —          |
| external_gene_available     |      11 | 2        | True        | 10     | —          | —         | —         | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2            |                1 | 9.09%                   |
| APC              |                1 | 9.09%                   |
| BRAF             |                1 | 9.09%                   |
| ITGA6            |                1 | 9.09%                   |
| EP300            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| DCP2             |                1 | 9.09%                   |
| IFT122           |                1 | 9.09%                   |
| IL2RG            |                1 | 9.09%                   |
| NRAS             |                1 | 9.09%                   |
| SMARCA4          |                1 | 9.09%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3M2            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| MAP2K1           |                1 | 9.09%                   |
| CD151            |                1 | 9.09%                   |
| CREBBP           |                1 | 9.09%                   |
| TCF7L2           |                1 | 9.09%                   |
| XRN1             |                1 | 9.09%                   |
| WDR35            |                1 | 9.09%                   |
| IL2              |                1 | 9.09%                   |
| SHOC2            |                1 | 9.09%                   |
| SMARCA2          |                1 | 9.09%                   |

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                8 | 72.73%                  |
| hotspot          |                3 | 27.27%                  |

**Column Grouping: `same_direction_as_discovery`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |                9 | 81.82%                  |
| False            |                2 | 18.18%                  |

**Column Grouping: `passes_external_nominal`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |                6 | 54.55%                  |
| False            |                5 | 45.45%                  |

**Column Grouping: `external_gene_available`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |               10 | 90.91%                  |
| False            |                1 | 9.09%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `external_p_value` contains **6** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                    -9.32083 |           0        |                    29 |                     292 |      1.28754  | True                          | True                      | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                    -2.70358 |           0.000596 |                    59 |                     262 |      0.798418 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                    -7.17211 |           0.001653 |                    11 |                     310 |      1.88069  | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                    -2.22019 |           0.012944 |                    20 |                     301 |      0.922898 | True                          | True                      | True                      |
| IL2:IL2RG        | IL2RG           | IL2            | damaging        |                    -1.57797 |           0.01477  |                     4 |                     317 |      0.419397 | True                          | True                      | True                      |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| AP3B2:AP3M2      | AP3B2           | AP3M2          | damaging        |                   -0.601137 |           0.284608 |                     5 |                     316 |      0.97212  | True                          | False                     | True                      |
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                   -9.32083  |           0        |                    29 |                     292 |      1.28754  | True                          | True                      | True                      |
| BRAF:MAP2K1      | BRAF            | MAP2K1         | hotspot         |                   -0.333282 |           0.408136 |                    14 |                     307 |      1.40631  | True                          | False                     | True                      |
| CD151:ITGA6      | ITGA6           | CD151          | damaging        |                   -0.182734 |           0.293465 |                    19 |                     302 |      0.331161 | True                          | False                     | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                   -2.70358  |           0.000596 |                    59 |                     262 |      0.798418 | True                          | True                      | True                      |
| CTNNB1:TCF7L2    | CTNNB1          | TCF7L2         | hotspot         |                  nan        |         nan        |                     0 |                       0 |    nan        | False                         | False                     | False                     |
| DCP2:XRN1        | DCP2            | XRN1           | damaging        |                  nan        |         nan        |                     2 |                     319 |    nan        | False                         | False                     | True                      |
| IFT122:WDR35     | IFT122          | WDR35          | damaging        |                   -1.0401   |           0.017701 |                     6 |                     315 |      0.378315 | True                          | True                      | True                      |
| IL2:IL2RG        | IL2RG           | IL2            | damaging        |                   -1.57797  |           0.01477  |                     4 |                     317 |      0.419397 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                   -7.17211  |           0.001653 |                    11 |                     310 |      1.88069  | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                   -2.22019  |           0.012944 |                    20 |                     301 |      0.922898 | True                          | True                      | True                      |


---

## File: phase13_external_depmap25q3_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_external_depmap25q3_summary.parquet`
- **Matrix Dimensions:** 1 rows × 17 columns

### 1. Data Schema & Quality Audit

| Column Name             | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:------------------------|:--------|-----------------:|-------------:|:---------|
| context                 | object  |                1 |            0 | 0.00%    |
| n_total_families        | int64   |                1 |            0 | 0.00%    |
| n_testable_families     | int64   |                1 |            0 | 0.00%    |
| n_concordant_families   | int64   |                1 |            0 | 0.00%    |
| concordance_rate        | float64 |                1 |            0 | 0.00%    |
| concordance_ci_low      | float64 |                1 |            0 | 0.00%    |
| concordance_ci_high     | float64 |                1 |            0 | 0.00%    |
| n_nominally_significant | int64   |                1 |            0 | 0.00%    |
| meta_mu                 | float64 |                1 |            0 | 0.00%    |
| meta_se                 | float64 |                1 |            0 | 0.00%    |
| meta_ci_low             | float64 |                1 |            0 | 0.00%    |
| meta_ci_high            | float64 |                1 |            0 | 0.00%    |
| meta_p                  | float64 |                1 |            0 | 0.00%    |
| meta_i2                 | float64 |                1 |            0 | 0.00%    |
| bayes_p_negative        | float64 |                1 |            0 | 0.00%    |
| bayes_mu_mean           | float64 |                1 |            0 | 0.00%    |
| bayes_rhat_mu           | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                         |   count | unique   | top         | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:------------------------|--------:|:---------|:------------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| context                 |       1 | 1        | DepMap 25Q3 | 1      | —         | —     | —         | —         | —         | —         | —         |
| n_total_families        |       1 | —        | —           | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| n_testable_families     |       1 | —        | —           | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| n_concordant_families   |       1 | —        | —           | —      | 11.000000 | —     | 11.000000 | 11.000000 | 11.000000 | 11.000000 | 11.000000 |
| concordance_rate        |       1 | —        | —           | —      | 1.000000  | —     | 1.000000  | 1.000000  | 1.000000  | 1.000000  | 1.000000  |
| concordance_ci_low      |       1 | —        | —           | —      | 0.741160  | —     | 0.741160  | 0.741160  | 0.741160  | 0.741160  | 0.741160  |
| concordance_ci_high     |       1 | —        | —           | —      | 1.000000  | —     | 1.000000  | 1.000000  | 1.000000  | 1.000000  | 1.000000  |
| n_nominally_significant |       1 | —        | —           | —      | 8.000000  | —     | 8.000000  | 8.000000  | 8.000000  | 8.000000  | 8.000000  |
| meta_mu                 |       1 | —        | —           | —      | -0.282462 | —     | -0.282462 | -0.282462 | -0.282462 | -0.282462 | -0.282462 |
| meta_se                 |       1 | —        | —           | —      | 0.058935  | —     | 0.058935  | 0.058935  | 0.058935  | 0.058935  | 0.058935  |
| meta_ci_low             |       1 | —        | —           | —      | -0.397975 | —     | -0.397975 | -0.397975 | -0.397975 | -0.397975 | -0.397975 |
| meta_ci_high            |       1 | —        | —           | —      | -0.166949 | —     | -0.166949 | -0.166949 | -0.166949 | -0.166949 | -0.166949 |
| meta_p                  |       1 | —        | —           | —      | 0.000002  | —     | 0.000002  | 0.000002  | 0.000002  | 0.000002  | 0.000002  |
| meta_i2                 |       1 | —        | —           | —      | 0.942031  | —     | 0.942031  | 0.942031  | 0.942031  | 0.942031  | 0.942031  |
| bayes_p_negative        |       1 | —        | —           | —      | 0.998000  | —     | 0.998000  | 0.998000  | 0.998000  | 0.998000  | 0.998000  |
| bayes_mu_mean           |       1 | —        | —           | —      | -0.283401 | —     | -0.283401 | -0.283401 | -0.283401 | -0.283401 | -0.283401 |
| bayes_rhat_mu           |       1 | —        | —           | —      | 0.999957  | —     | 0.999957  | 0.999957  | 0.999957  | 0.999957  | 0.999957  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **1** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context     |   n_total_families |   n_testable_families |   n_concordant_families |   concordance_rate |   concordance_ci_low |   concordance_ci_high |   n_nominally_significant |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   bayes_p_negative |   bayes_mu_mean |   bayes_rhat_mu |
|:------------|-------------------:|----------------------:|------------------------:|-------------------:|---------------------:|----------------------:|--------------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|-------------------:|----------------:|----------------:|
| DepMap 25Q3 |                 11 |                    11 |                      11 |                  1 |              0.74116 |                     1 |                         8 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 |    2e-06 |  0.942031 |              0.998 |       -0.283401 |        0.999957 |

- 📊 **Concordance Metric Profile (`concordance_rate`):** Mean=1.00000, Max=1.00000, Min=1.00000
- 📊 **Concordance Metric Profile (`concordance_ci_low`):** Mean=0.74116, Max=0.74116, Min=0.74116
- 📊 **Concordance Metric Profile (`concordance_ci_high`):** Mean=1.00000, Max=1.00000, Min=1.00000

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| context     |   n_total_families |   n_testable_families |   n_concordant_families |   concordance_rate |   concordance_ci_low |   concordance_ci_high |   n_nominally_significant |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   bayes_p_negative |   bayes_mu_mean |   bayes_rhat_mu |
|:------------|-------------------:|----------------------:|------------------------:|-------------------:|---------------------:|----------------------:|--------------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|-------------------:|----------------:|----------------:|
| DepMap 25Q3 |                 11 |                    11 |                      11 |                  1 |              0.74116 |                     1 |                         8 | -0.282462 |  0.058935 |     -0.397975 |      -0.166949 |    2e-06 |  0.942031 |              0.998 |       -0.283401 |        0.999957 |


---

## File: phase13_external_depmap25q3_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_external_depmap25q3_validation.parquet`
- **Matrix Dimensions:** 11 rows × 12 columns

### 1. Data Schema & Quality Audit

| Column Name                 | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key              | object  |               11 |            0 | 0.00%    |
| mutation_gene               | object  |               11 |            0 | 0.00%    |
| partner_gene                | object  |               11 |            0 | 0.00%    |
| mutation_type               | object  |               11 |            0 | 0.00%    |
| external_delta_dependency   | float64 |               11 |            0 | 0.00%    |
| external_p_value            | float64 |               11 |            0 | 0.00%    |
| external_num_mutant         | int64   |               11 |            0 | 0.00%    |
| external_num_wildtype       | int64   |               11 |            0 | 0.00%    |
| external_se                 | float64 |               11 |            0 | 0.00%    |
| same_direction_as_discovery | bool    |               11 |            0 | 0.00%    |
| passes_external_nominal     | bool    |               11 |            0 | 0.00%    |
| external_gene_available     | bool    |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                             |   count | unique   | top         | freq   | mean        | std       | min         | 25%         | 50%         | 75%         | max         |
|:----------------------------|--------:|:---------|:------------|:-------|:------------|:----------|:------------|:------------|:------------|:------------|:------------|
| undirected_key              |      11 | 11       | AP3B2:AP3M2 | 1      | —           | —         | —           | —           | —           | —           | —           |
| mutation_gene               |      11 | 11       | AP3B2       | 1      | —           | —         | —           | —           | —           | —           | —           |
| partner_gene                |      11 | 11       | AP3M2       | 1      | —           | —         | —           | —           | —           | —           | —           |
| mutation_type               |      11 | 2        | damaging    | 8      | —           | —         | —           | —           | —           | —           | —           |
| external_delta_dependency   |      11 | —        | —           | —      | -0.284506   | 0.240317  | -0.846298   | -0.375784   | -0.331736   | -0.098613   | -0.024744   |
| external_p_value            |      11 | —        | —           | —      | 0.067617    | 0.128733  | 0.000000    | 0.000000    | 0.000048    | 0.052470    | 0.366813    |
| external_num_mutant         |      11 | —        | —           | —      | 38.454545   | 35.553800 | 4.000000    | 5.500000    | 31.000000   | 68.000000   | 91.000000   |
| external_num_wildtype       |      11 | —        | —           | —      | 1147.545455 | 35.553800 | 1095.000000 | 1118.000000 | 1155.000000 | 1180.500000 | 1182.000000 |
| external_se                 |      11 | —        | —           | —      | 0.062752    | 0.032505  | 0.016996    | 0.039660    | 0.064675    | 0.073924    | 0.139602    |
| same_direction_as_discovery |      11 | 1        | True        | 11     | —           | —         | —           | —           | —           | —           | —           |
| passes_external_nominal     |      11 | 2        | True        | 8      | —           | —         | —           | —           | —           | —           | —           |
| external_gene_available     |      11 | 1        | True        | 11     | —           | —         | —           | —           | —           | —           | —           |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2            |                1 | 9.09%                   |
| APC              |                1 | 9.09%                   |
| BRAF             |                1 | 9.09%                   |
| ITGA6            |                1 | 9.09%                   |
| EP300            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| DCP2             |                1 | 9.09%                   |
| IFT122           |                1 | 9.09%                   |
| IL2RG            |                1 | 9.09%                   |
| NRAS             |                1 | 9.09%                   |
| SMARCA4          |                1 | 9.09%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3M2            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| MAP2K1           |                1 | 9.09%                   |
| CD151            |                1 | 9.09%                   |
| CREBBP           |                1 | 9.09%                   |
| TCF7L2           |                1 | 9.09%                   |
| XRN1             |                1 | 9.09%                   |
| WDR35            |                1 | 9.09%                   |
| IL2              |                1 | 9.09%                   |
| SHOC2            |                1 | 9.09%                   |
| SMARCA2          |                1 | 9.09%                   |

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                8 | 72.73%                  |
| hotspot          |                3 | 27.27%                  |

**Column Grouping: `passes_external_nominal`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |                8 | 72.73%                  |
| False            |                3 | 27.27%                  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `external_p_value` contains **8** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                   -0.846298 |              0     |                    78 |                    1108 |      0.081476 | True                          | True                      | True                      |
| BRAF:MAP2K1      | BRAF            | MAP2K1         | hotspot         |                   -0.374534 |              0     |                    91 |                    1095 |      0.038347 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                   -0.439163 |              0     |                    58 |                    1128 |      0.053941 | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                   -0.358296 |              1e-06 |                    58 |                    1128 |      0.065561 | True                          | True                      | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                   -0.331736 |              1e-06 |                    82 |                    1104 |      0.064675 | True                          | True                      | True                      |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| AP3B2:AP3M2      | AP3B2           | AP3M2          | damaging        |                   -0.062059 |           0.09047  |                     6 |                    1180 |      0.040048 | True                          | False                     | True                      |
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                   -0.846298 |           0        |                    78 |                    1108 |      0.081476 | True                          | True                      | True                      |
| BRAF:MAP2K1      | BRAF            | MAP2K1         | hotspot         |                   -0.374534 |           0        |                    91 |                    1095 |      0.038347 | True                          | True                      | True                      |
| CD151:ITGA6      | ITGA6           | CD151          | damaging        |                   -0.024744 |           0.366813 |                     4 |                    1182 |      0.066371 | True                          | False                     | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                   -0.331736 |           1e-06    |                    82 |                    1104 |      0.064675 | True                          | True                      | True                      |
| CTNNB1:TCF7L2    | CTNNB1          | TCF7L2         | hotspot         |                   -0.377035 |           4.8e-05  |                    31 |                    1155 |      0.083989 | True                          | True                      | True                      |
| DCP2:XRN1        | DCP2            | XRN1           | damaging        |                   -0.095931 |           0.270307 |                     4 |                    1182 |      0.139602 | True                          | False                     | True                      |
| IFT122:WDR35     | IFT122          | WDR35          | damaging        |                   -0.118479 |           0.014469 |                     6 |                    1180 |      0.039272 | True                          | True                      | True                      |
| IL2:IL2RG        | IL2RG           | IL2            | damaging        |                   -0.101295 |           0.001673 |                     5 |                    1181 |      0.016996 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                   -0.439163 |           0        |                    58 |                    1128 |      0.053941 | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                   -0.358296 |           1e-06    |                    58 |                    1128 |      0.065561 | True                          | True                      | True                      |


---

## File: phase13_family_dependency_stats.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase13_family_dependency_stats.parquet`
- **Matrix Dimensions:** 10 rows × 13 columns

### 1. Data Schema & Quality Audit

| Column Name             | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:------------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key          | object  |               10 |            0 | 0.00%    |
| gene_a                  | object  |               10 |            0 | 0.00%    |
| gene_b                  | object  |               10 |            0 | 0.00%    |
| mutation_gene           | object  |               10 |            0 | 0.00%    |
| partner_gene            | object  |               10 |            0 | 0.00%    |
| corum_mutation_type     | object  |               10 |            0 | 0.00%    |
| string_mutation_type    | object  |               10 |            0 | 0.00%    |
| corum_delta_dependency  | float64 |               10 |            0 | 0.00%    |
| string_delta_dependency | float64 |               10 |            0 | 0.00%    |
| string_min_hlrc         | float64 |               10 |            0 | 0.00%    |
| delta_dependency        | float64 |               10 |            0 | 0.00%    |
| p_value                 | float64 |               10 |            0 | 0.00%    |
| mutation_type           | object  |               10 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                         |   count | unique   | top        | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:------------------------|--------:|:---------|:-----------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| undirected_key          |      10 | 10       | APC:CTNNB1 | 1      | —         | —        | —         | —         | —         | —         | —         |
| gene_a                  |      10 | 9        | BRAF       | 2      | —         | —        | —         | —         | —         | —         | —         |
| gene_b                  |      10 | 10       | CTNNB1     | 1      | —         | —        | —         | —         | —         | —         | —         |
| mutation_gene           |      10 | 9        | BRAF       | 2      | —         | —        | —         | —         | —         | —         | —         |
| partner_gene            |      10 | 10       | CTNNB1     | 1      | —         | —        | —         | —         | —         | —         | —         |
| corum_mutation_type     |      10 | 2        | damaging   | 5      | —         | —        | —         | —         | —         | —         | —         |
| string_mutation_type    |      10 | 2        | damaging   | 5      | —         | —        | —         | —         | —         | —         | —         |
| corum_delta_dependency  |      10 | —        | —          | —      | -0.371939 | 0.235689 | -0.927101 | -0.447396 | -0.372117 | -0.210570 | -0.105117 |
| string_delta_dependency |      10 | —        | —          | —      | -0.371939 | 0.235689 | -0.927101 | -0.447396 | -0.372117 | -0.210570 | -0.105117 |
| string_min_hlrc         |      10 | —        | —          | —      | -0.745373 | 0.158594 | -0.936707 | -0.863422 | -0.764761 | -0.673900 | -0.459433 |
| delta_dependency        |      10 | —        | —          | —      | -0.329184 | 0.237434 | -0.864850 | -0.396054 | -0.349881 | -0.153646 | -0.005425 |
| p_value                 |      10 | —        | —          | —      | 0.002249  | 0.006730 | 0.000000  | 0.000000  | 0.000002  | 0.000128  | 0.021386  |
| mutation_type           |      10 | 2        | damaging   | 5      | —         | —        | —         | —         | —         | —         | —         |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| APC:CTNNB1       |                1 | 10.0%                   |
| BRAF:MAP2K1      |                1 | 10.0%                   |
| BRAF:MAP2K2      |                1 | 10.0%                   |
| CREBBP:EP300     |                1 | 10.0%                   |
| CTNNB1:TCF7L2    |                1 | 10.0%                   |
| DPY30:KMT2D      |                1 | 10.0%                   |
| HIPK2:TP53       |                1 | 10.0%                   |
| NRAS:SHOC2       |                1 | 10.0%                   |
| POLE:POLE2       |                1 | 10.0%                   |
| SMARCA2:SMARCA4  |                1 | 10.0%                   |

**Column Grouping: `gene_a`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| BRAF             |                2 | 20.0%                   |
| APC              |                1 | 10.0%                   |
| CREBBP           |                1 | 10.0%                   |
| CTNNB1           |                1 | 10.0%                   |
| DPY30            |                1 | 10.0%                   |
| HIPK2            |                1 | 10.0%                   |
| NRAS             |                1 | 10.0%                   |
| POLE             |                1 | 10.0%                   |
| SMARCA2          |                1 | 10.0%                   |

**Column Grouping: `gene_b`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CTNNB1           |                1 | 10.0%                   |
| MAP2K1           |                1 | 10.0%                   |
| MAP2K2           |                1 | 10.0%                   |
| EP300            |                1 | 10.0%                   |
| TCF7L2           |                1 | 10.0%                   |
| KMT2D            |                1 | 10.0%                   |
| TP53             |                1 | 10.0%                   |
| SHOC2            |                1 | 10.0%                   |
| POLE2            |                1 | 10.0%                   |
| SMARCA4          |                1 | 10.0%                   |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| BRAF             |                2 | 20.0%                   |
| APC              |                1 | 10.0%                   |
| EP300            |                1 | 10.0%                   |
| CTNNB1           |                1 | 10.0%                   |
| KMT2D            |                1 | 10.0%                   |
| TP53             |                1 | 10.0%                   |
| NRAS             |                1 | 10.0%                   |
| POLE             |                1 | 10.0%                   |
| SMARCA4          |                1 | 10.0%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CTNNB1           |                1 | 10.0%                   |
| MAP2K1           |                1 | 10.0%                   |
| MAP2K2           |                1 | 10.0%                   |
| CREBBP           |                1 | 10.0%                   |
| TCF7L2           |                1 | 10.0%                   |
| DPY30            |                1 | 10.0%                   |
| HIPK2            |                1 | 10.0%                   |
| SHOC2            |                1 | 10.0%                   |
| POLE2            |                1 | 10.0%                   |
| SMARCA2          |                1 | 10.0%                   |

**Column Grouping: `corum_mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                5 | 50.0%                   |
| hotspot          |                5 | 50.0%                   |

**Column Grouping: `string_mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                5 | 50.0%                   |
| hotspot          |                5 | 50.0%                   |

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                5 | 50.0%                   |
| hotspot          |                5 | 50.0%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **10** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| undirected_key   | gene_a   | gene_b   | mutation_gene   | partner_gene   | corum_mutation_type   | string_mutation_type   |   corum_delta_dependency |   string_delta_dependency |   string_min_hlrc |   delta_dependency |   p_value | mutation_type   |
|:-----------------|:---------|:---------|:----------------|:---------------|:----------------------|:-----------------------|-------------------------:|--------------------------:|------------------:|-------------------:|----------:|:----------------|
| BRAF:MAP2K1      | BRAF     | MAP2K1   | BRAF            | MAP2K1         | hotspot               | hotspot                |                -0.390174 |                 -0.390174 |         -0.726548 |          -0.391778 |     0     | hotspot         |
| APC:CTNNB1       | APC      | CTNNB1   | APC             | CTNNB1         | damaging              | damaging               |                -0.927101 |                 -0.927101 |         -0.903316 |          -0.86485  |     0     | damaging        |
| NRAS:SHOC2       | NRAS     | SHOC2    | NRAS            | SHOC2          | hotspot               | hotspot                |                -0.474233 |                 -0.474233 |         -0.525517 |          -0.442106 |     0     | hotspot         |
| CREBBP:EP300     | CREBBP   | EP300    | EP300           | CREBBP         | damaging              | damaging               |                -0.370856 |                 -0.370856 |         -0.936707 |          -0.354865 |     0     | damaging        |
| SMARCA2:SMARCA4  | SMARCA2  | SMARCA4  | SMARCA4         | SMARCA2        | damaging              | damaging               |                -0.373378 |                 -0.373378 |         -0.868675 |          -0.344897 |     1e-06 | damaging        |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (10 rows total):

| undirected_key   | gene_a   | gene_b   | mutation_gene   | partner_gene   | corum_mutation_type   | string_mutation_type   |   corum_delta_dependency |   string_delta_dependency |   string_min_hlrc |   delta_dependency |   p_value | mutation_type   |
|:-----------------|:---------|:---------|:----------------|:---------------|:----------------------|:-----------------------|-------------------------:|--------------------------:|------------------:|-------------------:|----------:|:----------------|
| APC:CTNNB1       | APC      | CTNNB1   | APC             | CTNNB1         | damaging              | damaging               |                -0.927101 |                 -0.927101 |         -0.903316 |          -0.86485  |  0        | damaging        |
| BRAF:MAP2K1      | BRAF     | MAP2K1   | BRAF            | MAP2K1         | hotspot               | hotspot                |                -0.390174 |                 -0.390174 |         -0.726548 |          -0.391778 |  0        | hotspot         |
| BRAF:MAP2K2      | BRAF     | MAP2K2   | BRAF            | MAP2K2         | hotspot               | hotspot                |                -0.128767 |                 -0.128767 |         -0.459433 |          -0.121823 |  0.000159 | hotspot         |
| CREBBP:EP300     | CREBBP   | EP300    | EP300           | CREBBP         | damaging              | damaging               |                -0.370856 |                 -0.370856 |         -0.936707 |          -0.354865 |  0        | damaging        |
| CTNNB1:TCF7L2    | CTNNB1   | TCF7L2   | CTNNB1          | TCF7L2         | hotspot               | hotspot                |                -0.46647  |                 -0.46647  |         -0.847663 |          -0.397479 |  3.4e-05  | hotspot         |
| DPY30:KMT2D      | DPY30    | KMT2D    | KMT2D           | DPY30          | damaging              | damaging               |                -0.105117 |                 -0.105117 |         -0.65635  |          -0.119498 |  4e-06    | damaging        |
| HIPK2:TP53       | HIPK2    | TP53     | TP53            | HIPK2          | hotspot               | hotspot                |                -0.179495 |                 -0.179495 |         -0.761836 |          -0.005425 |  0.021386 | hotspot         |
| NRAS:SHOC2       | NRAS     | SHOC2    | NRAS            | SHOC2          | hotspot               | hotspot                |                -0.474233 |                 -0.474233 |         -0.525517 |          -0.442106 |  0        | hotspot         |
| POLE:POLE2       | POLE     | POLE2    | POLE            | POLE2          | damaging              | damaging               |                -0.303795 |                 -0.303795 |         -0.767686 |          -0.249117 |  0.000904 | damaging        |
| SMARCA2:SMARCA4  | SMARCA2  | SMARCA4  | SMARCA4         | SMARCA2        | damaging              | damaging               |                -0.373378 |                 -0.373378 |         -0.868675 |          -0.344897 |  1e-06    | damaging        |


---

## File: phase14_benchmark_universe.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase14_benchmark_universe.parquet`
- **Matrix Dimensions:** 79274 rows × 16 columns

### 1. Data Schema & Quality Audit

| Column Name              | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-------------------------|:--------|-----------------:|-------------:|:---------|
| pair_key                 | object  |            79274 |            0 | 0.00%    |
| min_hfrc                 | float64 |            79274 |            0 | 0.00%    |
| median_hfrc              | float64 |            79274 |            0 | 0.00%    |
| mean_hfrc                | float64 |            79274 |            0 | 0.00%    |
| min_hlrc                 | float64 |            79274 |            0 | 0.00%    |
| median_hlrc              | float64 |            79274 |            0 | 0.00%    |
| mean_hlrc                | float64 |            79274 |            0 | 0.00%    |
| mean_hyperedge_size      | float64 |            79274 |            0 | 0.00%    |
| mean_edge_node_degree    | float64 |            79274 |            0 | 0.00%    |
| mean_pair_essentiality   | float64 |            79274 |            0 | 0.00%    |
| pair_max_node_degree     | int64   |            79274 |            0 | 0.00%    |
| pair_hyperedge_count     | int64   |            79274 |            0 | 0.00%    |
| is_systematic_candidate  | int64   |            79274 |            0 | 0.00%    |
| is_validated_candidate   | int64   |            79274 |            0 | 0.00%    |
| log_pair_hyperedge_count | float64 |            79274 |            0 | 0.00%    |
| is_any_discovery         | int64   |            79274 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                          |   count | unique   | top         | freq   | mean         | std         | min           | 25%          | 50%          | 75%         | max        |
|:-------------------------|--------:|:---------|:------------|:-------|:-------------|:------------|:--------------|:-------------|:-------------|:------------|:-----------|
| pair_key                 |   79274 | 79274    | A1BG:CRISP3 | 1      | —            | —           | —             | —            | —            | —           | —          |
| min_hfrc                 |   79274 | —        | —           | —      | -3952.144928 | 4807.317928 | -15894.000000 | -8050.000000 | -1298.000000 | -280.000000 | 0.000000   |
| median_hfrc              |   79274 | —        | —           | —      | -2772.719492 | 3890.262630 | -15846.000000 | -4439.500000 | -848.000000  | -185.500000 | 0.000000   |
| mean_hfrc                |   79274 | —        | —           | —      | -2545.864076 | 3386.757514 | -14912.210526 | -4505.416667 | -806.708333  | -186.000000 | 0.000000   |
| min_hlrc                 |   79274 | —        | —           | —      | -0.261186    | 0.450726    | -0.987050     | -0.658722    | -0.309831    | 0.070487    | 1.000000   |
| median_hlrc              |   79274 | —        | —           | —      | -0.090121    | 0.455806    | -0.987050     | -0.465733    | -0.049680    | 0.231484    | 1.000000   |
| mean_hlrc                |   79274 | —        | —           | —      | -0.073500    | 0.447490    | -0.987050     | -0.434748    | -0.047569    | 0.236009    | 1.000000   |
| mean_hyperedge_size      |   79274 | —        | —           | —      | 17.726226    | 18.263370   | 2.000000      | 4.000000     | 9.648498     | 25.800000   | 74.350000  |
| mean_edge_node_degree    |   79274 | —        | —           | —      | 104.656866   | 79.932842   | 2.000000      | 39.500000    | 86.000000    | 156.507867  | 425.386364 |
| mean_pair_essentiality   |   79274 | —        | —           | —      | -0.632173    | 0.694680    | -4.586777     | -1.035081    | -0.398330    | -0.072329   | 0.352184   |
| pair_max_node_degree     |   79274 | —        | —           | —      | 132.020410   | 127.448025  | 2.000000      | 41.000000    | 94.000000    | 174.000000  | 706.000000 |
| pair_hyperedge_count     |   79274 | —        | —           | —      | 6.547695     | 12.337343   | 2.000000      | 2.000000     | 3.000000     | 6.000000    | 247.000000 |
| is_systematic_candidate  |   79274 | —        | —           | —      | 0.000303     | 0.017397    | 0.000000      | 0.000000     | 0.000000     | 0.000000    | 1.000000   |
| is_validated_candidate   |   79274 | —        | —           | —      | 0.001678     | 0.040926    | 0.000000      | 0.000000     | 0.000000     | 0.000000    | 1.000000   |
| log_pair_hyperedge_count |   79274 | —        | —           | —      | 1.627400     | 0.722322    | 1.098612      | 1.098612     | 1.386294     | 1.945910    | 5.513429   |
| is_any_discovery         |   79274 | —        | —           | —      | 0.000126     | 0.011231    | 0.000000      | 0.000000     | 0.000000     | 0.000000    | 1.000000   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| pair_key      |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   is_any_discovery |
|:--------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|-------------------:|
| A1BG:CRISP3   |         -3 |          -3   |      -3     |   0.333333 |      0.333333 |    0.333333 |               2       |                 3.5     |                 0.048835 |                      5 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1BG:GRB2     |       -745 |        -628   |    -628     |  -0.478311 |     -0.399493 |   -0.399493 |               2.5     |               253.917   |                -0.50401  |                    510 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1BG:PTPN11   |       -745 |        -491   |    -491     |  -0.478311 |     -0.393627 |   -0.393627 |               2.5     |               185.417   |                -0.360209 |                    236 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1CF:APOBEC1  |         -5 |          -5   |      -5     |   0.25     |      0.25     |    0.25     |               2       |                 4.5     |                -0.053671 |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1CF:APOBEC3F |        -11 |          -9.5 |      -9.5   |   0.166667 |      0.1875   |    0.1875   |               2.5     |                 5.83333 |                 0.08001  |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1CF:APOBEC3G |        -11 |          -9.5 |      -9.5   |   0.166667 |      0.1875   |    0.1875   |               2.5     |                 5.83333 |                 0.025798 |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A1CF:SYNCRIP  |        -37 |         -37   |     -37     |  -0.7      |     -0.7      |   -0.7      |               2       |                20.5     |                -0.187088 |                     34 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:ALB       |       -274 |        -199.5 |    -195.25  |  -0.826253 |     -0.688032 |   -0.709627 |               3.5     |                57.5625  |                 0.036788 |                     67 |                      4 |                         0 |                        0 |                    1.60944 |                  0 |
| A2M:APOA1     |       -274 |        -202.5 |    -210.5   |  -0.831304 |     -0.73487  |   -0.72916  |               3.66667 |                59.5417  |                 0.009016 |                     77 |                      6 |                         0 |                        0 |                    1.94591 |                  0 |
| A2M:APOE      |       -274 |        -220   |    -212     |  -0.856791 |     -0.828779 |   -0.800654 |               3.25    |                66.8958  |                 0.005862 |                     93 |                      4 |                         0 |                        0 |                    1.60944 |                  0 |
| A2M:CLU       |       -271 |        -194.5 |    -191.25  |  -0.877964 |     -0.784349 |   -0.778909 |               3.25    |                60.2917  |                 0.014129 |                     64 |                      4 |                         0 |                        0 |                    1.60944 |                  0 |
| A2M:HAMP      |        -49 |         -49   |     -49     |  -0.706522 |     -0.706522 |   -0.706522 |               2       |                26.5     |                -0.192661 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:HP        |       -195 |        -125   |    -125     |  -0.636191 |     -0.565378 |   -0.565378 |               3       |                40.125   |                 0.19937  |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:HSPA5     |       -188 |        -157   |    -157     |  -0.877964 |     -0.872777 |   -0.872777 |               2.5     |                64.8333  |                -0.633714 |                     85 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:IL10      |        -53 |         -53   |     -53     |  -0.831522 |     -0.831522 |   -0.831522 |               2       |                28.5     |                -0.006624 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:IL1B      |        -86 |         -86   |     -86     |  -0.916522 |     -0.916522 |   -0.916522 |               2       |                45       |                 0.003668 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:IL6       |        -72 |         -72   |     -72     |  -0.897698 |     -0.897698 |   -0.897698 |               2       |                38       |                 0.048863 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:KLK3      |        -69 |         -58.5 |     -58.5   |  -0.48286  |     -0.447952 |   -0.447952 |               2.5     |                25.5     |                 0.018472 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:KLK4      |        -68 |         -58.5 |     -58.5   |  -0.551449 |     -0.532246 |   -0.532246 |               2.5     |                25.5833  |                -0.004101 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:KLKB1     |        -71 |         -61.5 |     -61.5   |  -0.601449 |     -0.59058  |   -0.59058  |               2.5     |                26.8333  |                 0.052281 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:KNG1      |        -83 |         -69.5 |     -71     |  -0.73286  |     -0.576449 |   -0.594628 |               2.75    |                28.25    |                -0.052358 |                     45 |                      4 |                         0 |                        0 |                    1.60944 |                  0 |
| A2M:LRP1      |       -169 |        -123   |    -123.333 |  -0.856791 |     -0.819876 |   -0.801125 |               2.66667 |                47.4444  |                -0.060089 |                     45 |                      3 |                         0 |                        0 |                    1.38629 |                  0 |
| A2M:MMP2      |       -115 |         -92.5 |     -92.5   |  -0.791304 |     -0.785507 |   -0.785507 |               2.5     |                38.6667  |                 0.023152 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:MMP3      |       -101 |         -78.5 |     -78.5   |  -0.724638 |     -0.707729 |   -0.707729 |               2.5     |                32.8333  |                 0.022503 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:MMP8      |        -43 |         -43   |     -43     |   0.043478 |      0.043478 |    0.043478 |               2       |                23.5     |                 0.012169 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:MMP9      |       -123 |        -108   |    -106.75  |  -0.819876 |     -0.757971 |   -0.746998 |               2.75    |                41.25    |                -0.005101 |                     47 |                      4 |                         0 |                        0 |                    1.60944 |                  0 |
| A2M:RAB3IL1   |        -48 |         -48   |     -48     |  -0.706522 |     -0.706522 |   -0.706522 |               2       |                26       |                -0.000953 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:SERPINA1  |       -204 |         -83   |    -124.2   |  -0.737395 |     -0.732345 |   -0.59261  |               3.2     |                38.7833  |                 0.004965 |                     45 |                      5 |                         0 |                        0 |                    1.79176 |                  0 |
| A2M:SERPINF2  |        -53 |         -53   |     -53     |  -0.845411 |     -0.845411 |   -0.845411 |               2       |                28.5     |                 0.069865 |                     45 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A2M:TGFB1     |        -96 |         -96   |     -96     |  -0.925272 |     -0.925272 |   -0.925272 |               2       |                50       |                -0.029161 |                     55 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| A4GALT:GLA    |          0 |           0   |       0     |   1        |      1        |    1        |               2       |                 2       |                -0.045523 |                      2 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| AAAS:AHCTF1   |      -1034 |       -1016   |    -705.667 |   0.396248 |      0.46555  |    0.540599 |              16.3333  |                42.2524  |                -0.749528 |                     42 |                      3 |                         0 |                        0 |                    1.38629 |                  0 |
| AAAS:NDC1     |      -1034 |        -881   |    -798.364 |  -0.484841 |      0.101871 |    0.157324 |              17.0909  |                48.4794  |                -0.474216 |                     42 |                     11 |                         0 |                        0 |                    2.48491 |                  0 |
| AAAS:NUP107   |      -1034 |        -883   |    -801.857 |  -0.012666 |      0.146972 |    0.264579 |              17.5714  |                47.2272  |                -0.576566 |                     44 |                      7 |                         0 |                        0 |                    2.07944 |                  0 |
| AAAS:NUP133   |      -1034 |        -885   |    -770.4   |   0.101871 |      0.396248 |    0.37398  |              17.4     |                44.9514  |                -0.915625 |                     42 |                      5 |                         0 |                        0 |                    1.79176 |                  0 |
| AAAS:NUP153   |      -1016 |        -882   |    -800.5   |  -0.012666 |      0.061309 |    0.140242 |              16.875   |                50.1212  |                -0.463235 |                     67 |                      8 |                         0 |                        0 |                    2.19722 |                  0 |
| AAAS:NUP155   |      -1034 |        -881   |    -799.455 |  -0.484841 |      0.101871 |    0.146305 |              17.0909  |                49.0249  |                -0.649105 |                     51 |                     11 |                         0 |                        0 |                    2.48491 |                  0 |
| AAAS:NUP160   |      -1034 |        -885   |    -769.8   |   0.101871 |      0.396248 |    0.381102 |              17.4     |                44.6514  |                -0.635718 |                     42 |                      5 |                         0 |                        0 |                    1.79176 |                  0 |
| AAAS:NUP188   |      -1034 |        -882   |    -825.2   |  -0.012666 |      0.120277 |    0.218207 |              17.8     |                47.7474  |                -0.27134  |                     42 |                     10 |                         0 |                        0 |                    2.3979  |                  0 |
| AAAS:NUP205   |      -1034 |        -881   |    -799.091 |  -0.484841 |      0.101871 |    0.151459 |              17.0909  |                48.8431  |                -0.696137 |                     47 |                     11 |                         0 |                        0 |                    2.48491 |                  0 |


*... [Truncated 79194 standard row items inline] ...*

**Last 40 Structural Rows:**

| pair_key        |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   is_any_discovery |
|:----------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|-------------------:|
| YWHAB:ZFP36     |        -63 |         -63   |     -63     |  -0.839286 |     -0.839286 |   -0.839286 |               2       |                33.5     |                -0.035077 |                     53 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| YWHAB:ZFP36L1   |        -58 |         -58   |     -58     |  -0.764286 |     -0.764286 |   -0.764286 |               2       |                31       |                -0.151808 |                     53 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| YWHAE:YWHAG     |       -394 |        -311   |    -282.4   |  -0.48596  |     -0.412248 |   -0.327192 |               6.4     |                45.1107  |                -0.321776 |                     40 |                      5 |                         0 |                        0 |                    1.79176 |                  0 |
| YWHAE:YWHAH     |       -394 |        -307.5 |    -275.333 |  -0.48596  |     -0.391982 |   -0.281637 |               6.33333 |                43.8145  |                -0.201064 |                     40 |                      6 |                         0 |                        0 |                    1.94591 |                  0 |
| YWHAE:YWHAQ     |       -394 |        -307.5 |    -277.167 |  -0.48596  |     -0.391982 |   -0.309707 |               6.33333 |                44.7312  |                -0.167698 |                     40 |                      6 |                         0 |                        0 |                    1.94591 |                  0 |
| YWHAE:YWHAZ     |       -394 |        -288.5 |    -273.125 |  -0.864814 |     -0.434289 |   -0.465814 |               5.75    |                52.665   |                -0.562597 |                    103 |                      8 |                         0 |                        0 |                    2.19722 |                  0 |
| YWHAG:YWHAH     |       -394 |        -311   |    -279.2   |  -0.48596  |     -0.412248 |   -0.272192 |               6.4     |                43.5107  |                -0.105323 |                     38 |                      5 |                         0 |                        0 |                    1.79176 |                  0 |
| YWHAG:YWHAQ     |       -394 |        -286   |    -273.7   |  -0.708846 |     -0.549952 |   -0.469834 |               5.7     |                49.9054  |                -0.071957 |                     38 |                     10 |                         0 |                        0 |                    2.3979  |                  0 |
| YWHAG:YWHAZ     |       -394 |        -283   |    -274.727 |  -0.76782  |     -0.613943 |   -0.530782 |               5.54545 |                53.5731  |                -0.466855 |                    103 |                     11 |                         0 |                        0 |                    2.48491 |                  0 |
| YWHAH:YWHAQ     |       -394 |        -304   |    -259.714 |  -0.546046 |     -0.412248 |   -0.28357  |               6.14286 |                42.3696  |                 0.048755 |                     35 |                      7 |                         0 |                        0 |                    2.07944 |                  0 |
| YWHAH:YWHAZ     |       -394 |        -304   |    -284.286 |  -0.678929 |     -0.412248 |   -0.365257 |               6.14286 |                50.1981  |                -0.346143 |                    103 |                      7 |                         0 |                        0 |                    2.07944 |                  0 |
| YWHAQ:YWHAZ     |       -394 |        -262   |    -261     |  -0.791268 |     -0.579005 |   -0.513856 |               5.28571 |                53.0693  |                -0.312777 |                    103 |                     14 |                         0 |                        0 |                    2.70805 |                  0 |
| YY1:YY2         |        -93 |         -93   |     -93     |   0.017544 |      0.017544 |    0.017544 |               2       |                48.5     |                -0.306408 |                     95 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZBTB17:ZBTB4    |         -6 |          -6   |      -6     |   0.2      |      0.2      |    0.2      |               2       |                 5       |                -0.251046 |                      8 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZC3H13:ZCCHC4   |        -57 |         -50   |     -50     |   0.070721 |      0.075901 |    0.075901 |               3       |                19.875   |                -0.19615  |                     43 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZCRB1:ZMAT5     |      -3677 |       -1861.5 |   -1861.5   |   0.022682 |      0.490508 |    0.490508 |              13       |                90.1042  |                -0.771819 |                     26 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZCRB1:ZRSR2     |      -3677 |       -1865.5 |   -1865.5   |   0.022682 |      0.407893 |    0.407893 |              13       |                92.1042  |                -0.754783 |                     34 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZEB1:ZEB2       |        -78 |         -50   |     -50     |  -0.369792 |     -0.268229 |   -0.268229 |               2.5     |                20.5     |                -0.213361 |                     21 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZER1:ZYG11B     |      -1001 |        -515.5 |    -515.5   |   0.2725   |      0.63625  |    0.63625  |               9.5     |                38.9412  |                -0.154825 |                     17 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZFP36L1:ZFP36L2 |         -7 |          -7   |      -7     |   0.2      |      0.2      |    0.2      |               2       |                 5.5     |                -0.283718 |                      9 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZFYVE16:ZFYVE9  |        -19 |         -14.5 |     -14.5   |   0.080357 |      0.183036 |    0.183036 |               2.5     |                 7.66667 |                -0.036917 |                     11 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZMAT5:ZRSR2     |      -3677 |       -1866.5 |   -1866.5   |   0.022682 |      0.38706  |    0.38706  |              13       |                92.6042  |                -0.967063 |                     34 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZMYM2:ZMYM3     |         -7 |          -7   |      -7     |  -0.3      |     -0.3      |   -0.3      |               2       |                 5.5     |                -0.112449 |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZMYND8:ZNF592   |       -165 |         -91.5 |     -91.5   |  -0.090972 |      0.148958 |    0.148958 |               4       |                20.25    |                -0.204002 |                     14 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZMYND8:ZNF687   |       -205 |        -165   |    -129.333 |  -0.231323 |     -0.090972 |    0.11479  |               4.66667 |                25.5556  |                -0.376565 |                     14 |                      3 |                         0 |                        0 |                    1.38629 |                  0 |
| ZNF174:ZSCAN1   |         -2 |          -2   |      -2     |   0.5      |      0.5      |    0.5      |               2       |                 3       |                -0.088947 |                      4 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZNF24:ZSCAN1    |         -4 |          -4   |      -4     |   0        |      0        |    0        |               2       |                 4       |                -0.075563 |                      4 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZNF592:ZNF687   |       -165 |         -88.5 |     -88.5   |  -0.090972 |      0.287847 |    0.287847 |               4       |                18.75    |                -0.183685 |                      8 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZNF787:ZW10     |        -90 |         -54.5 |     -54.5   |  -0.128959 |      0.012443 |    0.012443 |               2.5     |                21.75    |                -0.179628 |                     20 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZNHIT3:ZNHIT6   |       -171 |         -89.5 |     -89.5   |  -0.122466 |      0.188767 |    0.188767 |               3       |                25.375   |                -0.662114 |                      8 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP1:ZP2         |        -17 |         -11.5 |     -11.5   |   0.875    |      0.9375   |    0.9375   |               3.5     |                 5.2     |                -0.008769 |                      5 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP1:ZP3         |        -17 |         -12.5 |     -12.5   |   0.8      |      0.8375   |    0.8375   |               3.5     |                 5.7     |                -0.09711  |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP1:ZP4         |        -17 |         -11.5 |     -11.5   |   0.875    |      0.9375   |    0.9375   |               3.5     |                 5.2     |                -0.016391 |                      5 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP2:ZP3         |        -17 |         -12.5 |     -12.5   |   0.8      |      0.8375   |    0.8375   |               3.5     |                 5.7     |                -0.041124 |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP2:ZP4         |        -17 |         -11.5 |     -11.5   |   0.875    |      0.9375   |    0.9375   |               3.5     |                 5.2     |                 0.039595 |                      5 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZP3:ZP4         |        -17 |         -12.5 |     -12.5   |   0.8      |      0.8375   |    0.8375   |               3.5     |                 5.7     |                -0.048746 |                      7 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZW10:ZWILCH     |        -62 |         -22   |     -35     |  -0.367521 |      0.198718 |    0.020655 |               2.66667 |                14.8333  |                -0.27625  |                     20 |                      3 |                         0 |                        0 |                    1.38629 |                  0 |
| ZW10:ZWINT      |        -62 |         -60.5 |     -60.5   |  -0.77208  |     -0.569801 |   -0.569801 |               2.5     |                27.0833  |                -0.43499  |                     43 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZWILCH:ZWINT    |        -62 |         -53   |     -53     |  -0.367521 |     -0.31339  |   -0.31339  |               2.5     |                23.3333  |                -0.349437 |                     43 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |
| ZXDA:ZXDC       |          0 |           0   |       0     |   1        |      1        |    1        |               2       |                 2       |                 0.007577 |                      2 |                      2 |                         0 |                        0 |                    1.09861 |                  0 |


---

## File: phase17_tcga_patient_bridge.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase17_tcga_patient_bridge.parquet`
- **Matrix Dimensions:** 114 rows × 10 columns

### 1. Data Schema & Quality Audit

| Column Name         | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key      | object  |              114 |            0 | 0.00%    |
| tumor_type          | object  |              114 |            0 | 0.00%    |
| n_mutant            | int64   |              114 |            0 | 0.00%    |
| n_wildtype          | int64   |              114 |            0 | 0.00%    |
| median_pfi_mutant   | float64 |              114 |            0 | 0.00%    |
| median_pfi_wildtype | float64 |              114 |            0 | 0.00%    |
| cox_p_value         | float64 |              107 |            7 | 6.14%    |
| hazard_ratio        | float64 |              107 |            7 | 6.14%    |
| n_total_rigor       | float64 |              107 |            7 | 6.14%    |
| n_events_rigor      | float64 |              107 |            7 | 6.14%    |

### 2. Full Descriptive Summary Statistics

|                     |   count | unique   | top          | freq   | mean       | std        | min        | 25%        | 50%        | 75%        | max         |
|:--------------------|--------:|:---------|:-------------|:-------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:------------|
| undirected_key      |     114 | 8        | CREBBP:EP300 | 19     | —          | —          | —          | —          | —          | —          | —           |
| tumor_type          |     114 | 23       | BLCA         | 8      | —          | —          | —          | —          | —          | —          | —           |
| n_mutant            |     114 | —        | —            | —      | 31.307018  | 48.215616  | 5.000000   | 8.000000   | 14.000000  | 31.750000  | 291.000000  |
| n_wildtype          |     114 | —        | —            | —      | 433.201754 | 199.752200 | 51.000000  | 311.250000 | 432.500000 | 500.250000 | 1092.000000 |
| median_pfi_mutant   |     114 | —        | —            | —      | 634.078947 | 279.768572 | 155.000000 | 442.750000 | 580.250000 | 796.875000 | 1354.000000 |
| median_pfi_wildtype |     114 | —        | —            | —      | 572.425439 | 171.793793 | 183.000000 | 447.000000 | 578.000000 | 678.750000 | 1014.000000 |
| cox_p_value         |     107 | —        | —            | —      | 0.444350   | 0.300612   | 0.000715   | 0.166336   | 0.444184   | 0.682869   | 1.000000    |
| hazard_ratio        |     107 | —        | —            | —      | 1.133209   | 0.947949   | 0.000000   | 0.586771   | 1.012627   | 1.351374   | 8.930356    |
| n_total_rigor       |     107 | —        | —            | —      | 458.476636 | 189.524447 | 90.000000  | 409.000000 | 447.000000 | 505.000000 | 1072.000000 |
| n_events_rigor      |     107 | —        | —            | —      | 164.168224 | 102.862290 | 35.000000  | 120.000000 | 139.000000 | 177.000000 | 506.000000  |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CREBBP:EP300     |               19 | 16.67%                  |
| SMARCA2:SMARCA4  |               19 | 16.67%                  |
| APC:CTNNB1       |               18 | 15.79%                  |
| BRAF:MAP2K1      |               15 | 13.16%                  |
| CTNNB1:TCF7L2    |               15 | 13.16%                  |
| SPTLC1:SPTLC3    |               11 | 9.65%                   |
| NRAS:SHOC2       |               10 | 8.77%                   |
| DCP2:XRN1        |                7 | 6.14%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `cox_p_value` contains **10** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| undirected_key   | tumor_type   |   n_mutant |   n_wildtype |   median_pfi_mutant |   median_pfi_wildtype |   cox_p_value |   hazard_ratio |   n_total_rigor |   n_events_rigor |
|:-----------------|:-------------|-----------:|-------------:|--------------------:|----------------------:|--------------:|---------------:|----------------:|-----------------:|
| SMARCA2:SMARCA4  | LUAD         |         48 |          474 |               405.5 |                 536   |      0.000715 |       2.03652  |             495 |              201 |
| DCP2:XRN1        | SKCM         |         13 |          457 |               364   |                 717   |      0.005592 |       2.49712  |             410 |              275 |
| SMARCA2:SMARCA4  | LGG          |         26 |          489 |               735.5 |                 513.5 |      0.006517 |       0.273561 |             514 |              192 |
| CTNNB1:TCF7L2    | UCEC         |        145 |          403 |               845.5 |                 721   |      0.008493 |       0.499867 |             545 |              124 |
| APC:CTNNB1       | UCEC         |         85 |          463 |              1195   |                 703   |      0.011593 |       0.330831 |             545 |              124 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (114 rows total):

| undirected_key   | tumor_type   |   n_mutant |   n_wildtype |   median_pfi_mutant |   median_pfi_wildtype |   cox_p_value |   hazard_ratio |   n_total_rigor |   n_events_rigor |
|:-----------------|:-------------|-----------:|-------------:|--------------------:|----------------------:|--------------:|---------------:|----------------:|-----------------:|
| APC:CTNNB1       | BLCA         |         28 |          384 |               414   |                 434   |      0.521675 |       1.22278  |             410 |              177 |
| APC:CTNNB1       | BRCA         |         21 |         1076 |               612   |                 783   |      0.616062 |       1.34127  |            1072 |              136 |
| APC:CTNNB1       | CESC         |         13 |          294 |               469   |                 599   |      0.105513 |       2.16861  |             307 |               71 |
| APC:CTNNB1       | COAD         |        289 |          170 |               588   |                 578   |      0.735089 |       1.0742   |             447 |              120 |
| APC:CTNNB1       | ESCA         |         10 |          175 |               200.5 |                 325   |      0.671053 |       0.726798 |             162 |               72 |
| APC:CTNNB1       | GBM          |         12 |          584 |               244   |                 183   |      0.611502 |       0.846981 |             596 |              506 |
| APC:CTNNB1       | HNSC         |         24 |          504 |               507.5 |                 560   |      0.489589 |       0.760176 |             452 |              171 |
| APC:CTNNB1       | KIRC         |          6 |          531 |               720   |                1014   |      0.536161 |       0.534305 |             532 |              159 |
| APC:CTNNB1       | LIHC         |         14 |          363 |               333   |                 365.5 |      0.779094 |       0.889415 |             352 |              169 |
| APC:CTNNB1       | LUAD         |         28 |          494 |               402   |                 526   |      0.524759 |       1.21142  |             495 |              201 |
| APC:CTNNB1       | LUSC         |         31 |          473 |               442   |                 583   |      0.050942 |       1.81799  |             489 |              145 |
| APC:CTNNB1       | OV           |         12 |          575 |               374   |                 454   |      0.114144 |       1.84261  |             582 |              413 |
| APC:CTNNB1       | PRAD         |         12 |          488 |               727   |                 801.5 |      0.047135 |       2.49484  |             500 |               93 |
| APC:CTNNB1       | READ         |        119 |           51 |               592   |                 485   |      0.081538 |       0.454142 |             161 |               38 |
| APC:CTNNB1       | SARC         |          7 |          254 |               828   |                 499   |      0.551992 |       0.73205  |             261 |              139 |
| APC:CTNNB1       | SKCM         |         77 |          393 |               799   |                 651   |      0.801775 |       1.04278  |             410 |              275 |
| APC:CTNNB1       | STAD         |         57 |          386 |               288   |                 383   |      0.935606 |       1.02484  |             409 |              136 |
| APC:CTNNB1       | UCEC         |         85 |          463 |              1195   |                 703   |      0.011593 |       0.330831 |             545 |              124 |
| BRAF:MAP2K1      | BLCA         |         15 |          397 |               573   |                 425   |      0.071381 |       0.275417 |             410 |              177 |
| BRAF:MAP2K1      | BRCA         |          8 |         1089 |               584.5 |                 773   |      0.539599 |       1.86128  |            1072 |              136 |
| BRAF:MAP2K1      | CESC         |          5 |          302 |               533   |                 590.5 |      0.943949 |       1.07417  |             307 |               71 |
| BRAF:MAP2K1      | COAD         |         58 |          401 |               554   |                 580   |      0.238683 |       0.674458 |             447 |              120 |
| BRAF:MAP2K1      | GBM          |          9 |          587 |               256   |                 183   |      0.972438 |       1.01263  |             596 |              506 |
| BRAF:MAP2K1      | HNSC         |         10 |          518 |               735   |                 549   |      0.379616 |       0.532346 |             452 |              171 |
| BRAF:MAP2K1      | KIRP         |          5 |          286 |              1251   |                 668   |      0.873011 |       1.17686  |             257 |               51 |
| BRAF:MAP2K1      | LUAD         |         42 |          480 |               567   |                 523   |      0.167075 |       1.36148  |             495 |              201 |
| BRAF:MAP2K1      | LUSC         |         17 |          487 |               350.5 |                 579   |      0.419308 |       0.560031 |             489 |              145 |
| BRAF:MAP2K1      | PRAD         |          7 |          493 |               938   |                 787   |      0.562103 |       0.551911 |             500 |               93 |
| BRAF:MAP2K1      | READ         |          6 |          164 |               584.5 |                 578.5 |    nan        |     nan        |             nan |              nan |
| BRAF:MAP2K1      | SKCM         |        247 |          223 |               733   |                 678   |      0.763655 |       1.03843  |             410 |              275 |
| BRAF:MAP2K1      | STAD         |         22 |          421 |               439   |                 378.5 |      0.464045 |       0.643924 |             409 |              136 |
| BRAF:MAP2K1      | THCA         |        291 |          216 |               938   |                 825   |      0.449314 |       1.24932  |             505 |               52 |
| BRAF:MAP2K1      | UCEC         |         31 |          517 |              1041   |                 749   |      0.226607 |       0.412595 |             545 |              124 |
| CREBBP:EP300     | BLCA         |         64 |          348 |               508   |                 411.5 |      0.595664 |       0.888162 |             410 |              177 |
| CREBBP:EP300     | BRCA         |         22 |         1075 |               532   |                 784   |      0.923579 |       1.07096  |            1072 |              136 |
| CREBBP:EP300     | CESC         |         37 |          270 |               607   |                 580.5 |      0.309647 |       1.405    |             307 |               71 |
| CREBBP:EP300     | COAD         |         33 |          426 |               670   |                 578   |      0.628553 |       1.17481  |             447 |              120 |
| CREBBP:EP300     | ESCA         |         11 |          174 |               236   |                 321   |      0.372345 |       1.517    |             162 |               72 |
| CREBBP:EP300     | GBM          |          8 |          588 |               220   |                 183   |      0.843422 |       0.913506 |             596 |              506 |
| CREBBP:EP300     | HNSC         |         38 |          490 |               481   |                 553   |      0.364699 |       1.28245  |             452 |              171 |
| CREBBP:EP300     | KIRC         |          9 |          528 |              1218   |                1001.5 |      0.710572 |       1.24491  |             532 |              159 |
| CREBBP:EP300     | KIRP         |         16 |          275 |               579.5 |                 679   |      0.887726 |       1.09101  |             257 |               51 |
| CREBBP:EP300     | LIHC         |         11 |          366 |               208   |                 366   |      0.774096 |       1.15709  |             352 |              169 |
| CREBBP:EP300     | LUAD         |         15 |          507 |               397   |                 526.5 |      0.730458 |       1.17328  |             495 |              201 |
| CREBBP:EP300     | LUSC         |         24 |          480 |               581   |                 573   |      0.067452 |       1.84299  |             489 |              145 |
| CREBBP:EP300     | OV           |         12 |          575 |               517.5 |                 447   |      0.063732 |       0.42908  |             582 |              413 |
| CREBBP:EP300     | PRAD         |          6 |          494 |               934.5 |                 788   |      0.638674 |       0.610043 |             500 |               93 |
| CREBBP:EP300     | READ         |          6 |          164 |               700   |                 552   |    nan        |     nan        |             nan |              nan |
| CREBBP:EP300     | SARC         |          6 |          255 |               503   |                 499   |      0.694256 |       1.22928  |             261 |              139 |
| CREBBP:EP300     | SKCM         |         52 |          418 |               750   |                 703   |      0.210498 |       1.27484  |             410 |              275 |
| CREBBP:EP300     | STAD         |         29 |          414 |               487   |                 378   |      0.821764 |       0.906753 |             409 |              136 |
| CREBBP:EP300     | UCEC         |         85 |          463 |               955.5 |                 739   |      0.065015 |       0.457412 |             545 |              124 |
| CTNNB1:TCF7L2    | ACC          |         14 |           78 |               277   |                 839.5 |      0.015234 |       2.42808  |              90 |               48 |
| CTNNB1:TCF7L2    | BLCA         |         14 |          398 |               517.5 |                 426.5 |      0.555968 |       1.25729  |             410 |              177 |
| CTNNB1:TCF7L2    | BRCA         |          7 |         1090 |              1010   |                 769   |      0.563074 |       1.79072  |            1072 |              136 |
| CTNNB1:TCF7L2    | CESC         |          7 |          300 |               474   |                 584   |      0.621748 |       1.44794  |             307 |               71 |
| CTNNB1:TCF7L2    | COAD         |         29 |          430 |               547   |                 580   |      0.84804  |       0.928953 |             447 |              120 |
| CTNNB1:TCF7L2    | ESCA         |          7 |          178 |               236   |                 320   |    nan        |     nan        |             nan |              nan |
| CTNNB1:TCF7L2    | HNSC         |          9 |          519 |               378   |                 559.5 |      0.23144  |       1.74202  |             452 |              171 |
| CTNNB1:TCF7L2    | LIHC         |         95 |          282 |               341   |                 382   |      0.388909 |       1.17647  |             352 |              169 |
| CTNNB1:TCF7L2    | LUAD         |         21 |          501 |               610   |                 521   |      0.888183 |       0.950259 |             495 |              201 |
| CTNNB1:TCF7L2    | LUSC         |          9 |          495 |               862   |                 569   |      0.551625 |       0.652626 |             489 |              145 |
| CTNNB1:TCF7L2    | PRAD         |         11 |          489 |               583   |                 819   |      0.125356 |       2.21459  |             500 |               93 |
| CTNNB1:TCF7L2    | READ         |          7 |          163 |               531   |                 592   |      0.787992 |       1.32801  |             161 |               38 |
| CTNNB1:TCF7L2    | SKCM         |         33 |          437 |              1065   |                 651   |      0.221424 |       0.745603 |             410 |              275 |
| CTNNB1:TCF7L2    | STAD         |         30 |          413 |               731   |                 377   |      0.026429 |       0.318038 |             409 |              136 |
| CTNNB1:TCF7L2    | UCEC         |        145 |          403 |               845.5 |                 721   |      0.008493 |       0.499867 |             545 |              124 |
| DCP2:XRN1        | BLCA         |          8 |          404 |               618   |                 424   |      0.422054 |       0.563499 |             410 |              177 |
| DCP2:XRN1        | COAD         |          8 |          451 |               621   |                 579.5 |      0.658403 |       0.725934 |             447 |              120 |
| DCP2:XRN1        | LUSC         |          6 |          498 |               592   |                 576   |      0.436215 |       0.456793 |             489 |              145 |
| DCP2:XRN1        | READ         |          6 |          164 |               763.5 |                 578.5 |    nan        |     nan        |             nan |              nan |
| DCP2:XRN1        | SKCM         |         13 |          457 |               364   |                 717   |      0.005592 |       2.49712  |             410 |              275 |
| DCP2:XRN1        | STAD         |          8 |          435 |               846.5 |                 379   |    nan        |     nan        |             nan |              nan |
| DCP2:XRN1        | UCEC         |         53 |          495 |              1116   |                 728   |      0.244469 |       0.562354 |             545 |              124 |
| NRAS:SHOC2       | BLCA         |          8 |          404 |              1077   |                 420.5 |      0.18793  |       0.390636 |             410 |              177 |
| NRAS:SHOC2       | COAD         |         20 |          439 |               466   |                 580   |      0.875681 |       0.930729 |             447 |              120 |
| NRAS:SHOC2       | LIHC         |          5 |          372 |               566   |                 365   |      0.761946 |       1.19457  |             352 |              169 |
| NRAS:SHOC2       | LUSC         |          6 |          498 |               392   |                 578   |      0.155513 |       2.30186  |             489 |              145 |
| NRAS:SHOC2       | OV           |          5 |          582 |               445   |                 448   |      0.28475  |       0.467811 |             582 |              413 |
| NRAS:SHOC2       | READ         |         16 |          154 |               425.5 |                 585.5 |      0.994464 |       1.0043   |             161 |               38 |
| NRAS:SHOC2       | SKCM         |        131 |          339 |               790.5 |                 631   |      0.509263 |       1.09178  |             410 |              275 |
| NRAS:SHOC2       | TGCT         |          5 |          129 |               471   |                 838   |      1        |       0        |             134 |               35 |
| NRAS:SHOC2       | THCA         |         39 |          468 |               659   |                 916   |      0.163541 |       1.85267  |             505 |               52 |
| NRAS:SHOC2       | UCEC         |         38 |          510 |              1195   |                 739   |      0.444184 |       0.696817 |             545 |              124 |
| SMARCA2:SMARCA4  | BLCA         |         29 |          383 |               536   |                 423   |      0.643686 |       0.870052 |             410 |              177 |
| SMARCA2:SMARCA4  | BRCA         |         19 |         1078 |               533   |                 785   |      0.196477 |       2.15233  |            1072 |              136 |
| SMARCA2:SMARCA4  | CESC         |         17 |          290 |               805   |                 556.5 |      0.23792  |       0.494503 |             307 |               71 |
| SMARCA2:SMARCA4  | COAD         |         36 |          423 |               511.5 |                 580   |      0.858848 |       0.93413  |             447 |              120 |
| SMARCA2:SMARCA4  | ESCA         |         14 |          171 |               348.5 |                 318   |      0.277321 |       0.618726 |             162 |               72 |
| SMARCA2:SMARCA4  | GBM          |         10 |          586 |               155   |                 186.5 |      0.136256 |       1.71279  |             596 |              506 |
| SMARCA2:SMARCA4  | HNSC         |         25 |          503 |               619   |                 550.5 |      0.812027 |       0.92029  |             452 |              171 |
| SMARCA2:SMARCA4  | KIRC         |         12 |          525 |              1354   |                 972   |      0.161031 |       0.243732 |             532 |              159 |
| SMARCA2:SMARCA4  | KIRP         |         14 |          277 |              1091.5 |                 665   |      0.647379 |       1.27604  |             257 |               51 |
| SMARCA2:SMARCA4  | LGG          |         26 |          489 |               735.5 |                 513.5 |      0.006517 |       0.273561 |             514 |              192 |
| SMARCA2:SMARCA4  | LIHC         |         11 |          366 |               199   |                 366   |      0.173951 |       1.76937  |             352 |              169 |
| SMARCA2:SMARCA4  | LUAD         |         48 |          474 |               405.5 |                 536   |      0.000715 |       2.03652  |             495 |              201 |
| SMARCA2:SMARCA4  | LUSC         |         26 |          478 |               521.5 |                 576   |      0.144332 |       1.59432  |             489 |              145 |
| SMARCA2:SMARCA4  | OV           |          7 |          580 |               641   |                 447   |      0.362729 |       1.41871  |             582 |              413 |
| SMARCA2:SMARCA4  | READ         |          7 |          163 |               607   |                 578   |      0.671481 |       0.644204 |             161 |               38 |
| SMARCA2:SMARCA4  | SKCM         |         58 |          412 |              1319   |                 646   |      0.569539 |       0.898792 |             410 |              275 |
| SMARCA2:SMARCA4  | STAD         |         32 |          411 |               519   |                 378.5 |      0.165597 |       0.433268 |             409 |              136 |
| SMARCA2:SMARCA4  | THCA         |          5 |          502 |               881   |                 897   |    nan        |     nan        |             nan |              nan |
| SMARCA2:SMARCA4  | UCEC         |         74 |          474 |              1213   |                 712   |      0.048357 |       0.438546 |             545 |              124 |
| SPTLC1:SPTLC3    | BLCA         |         12 |          400 |               816   |                 416.5 |      0.155504 |       0.434868 |             410 |              177 |
| SPTLC1:SPTLC3    | BRCA         |          5 |         1092 |               441   |                 783   |      0.034321 |       8.93036  |            1072 |              136 |
| SPTLC1:SPTLC3    | CESC         |          5 |          302 |               533   |                 584   |      0.319961 |       2.08877  |             307 |               71 |
| SPTLC1:SPTLC3    | COAD         |         19 |          440 |               388   |                 580   |      0.807608 |       1.1215   |             447 |              120 |
| SPTLC1:SPTLC3    | HNSC         |          5 |          523 |               401   |                 552.5 |      0.487283 |       1.50984  |             452 |              171 |
| SPTLC1:SPTLC3    | LUAD         |         10 |          512 |               807   |                 520   |      0.29291  |       1.50697  |             495 |              201 |
| SPTLC1:SPTLC3    | LUSC         |         12 |          492 |               929.5 |                 570   |      0.229858 |       0.423576 |             489 |              145 |
| SPTLC1:SPTLC3    | READ         |          5 |          165 |               531   |                 579   |    nan        |     nan        |             nan |              nan |
| SPTLC1:SPTLC3    | SKCM         |         49 |          421 |              1188   |                 631   |      0.926163 |       0.981679 |             410 |              275 |
| SPTLC1:SPTLC3    | STAD         |         18 |          425 |               628.5 |                 378   |      0.181945 |       0.452348 |             409 |              136 |
| SPTLC1:SPTLC3    | UCEC         |         44 |          504 |              1313.5 |                 726   |      0.059647 |       0.246838 |             545 |              124 |


---

## File: phase25_prism_cdks_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase25_prism_cdks_validation.parquet`
- **Matrix Dimensions:** 17 rows × 5 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| drug          | object  |               17 |            0 | 0.00%    |
| target        | object  |               17 |            0 | 0.00%    |
| delta_auc     | float64 |               17 |            0 | 0.00%    |
| p_value       | float64 |               17 |            0 | 0.00%    |
| q_value       | float64 |               17 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|           |   count | unique   | top                                | freq   | mean     | std      | min       | 25%       | 50%       | 75%      | max      |
|:----------|--------:|:---------|:-----------------------------------|:-------|:---------|:---------|:----------|:----------|:----------|:---------|:---------|
| drug      |      17 | 17       | AT-7519                            | 1      | —        | —        | —         | —         | —         | —        | —        |
| target    |      17 | 17       | CDK1, CDK2, CDK4, CDK5, CDK6, CDK9 | 1      | —        | —        | —         | —         | —         | —        | —        |
| delta_auc |      17 | —        | —                                  | —      | 0.003123 | 0.038993 | -0.090865 | -0.010641 | -0.003664 | 0.024437 | 0.092358 |
| p_value   |      17 | —        | —                                  | —      | 0.499368 | 0.344475 | 0.001256  | 0.262879  | 0.458006  | 0.807156 | 0.994432 |
| q_value   |      17 | —        | —                                  | —      | 0.746629 | 0.342930 | 0.013624  | 0.722523  | 0.865122  | 0.993458 | 0.994432 |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **3** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug       | target                             |   delta_auc |   p_value |   q_value |
|:-----------|:-----------------------------------|------------:|----------:|----------:|
| AT-7519    | CDK1, CDK2, CDK4, CDK5, CDK6, CDK9 |   -0.036081 |  0.001256 |  0.013624 |
| PHA-793887 | CDK1, CDK2, CDK4, CDK5, CDK7, CDK9 |   -0.090865 |  0.001603 |  0.013624 |
| dinaciclib | CDK1, CDK2, CDK5, CDK9             |   -0.026623 |  0.031551 |  0.178791 |

- 💡 **Significance Hit:** Column `q_value` contains **2** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug       | target                             |   delta_auc |   p_value |   q_value |
|:-----------|:-----------------------------------|------------:|----------:|----------:|
| AT-7519    | CDK1, CDK2, CDK4, CDK5, CDK6, CDK9 |   -0.036081 |  0.001256 |  0.013624 |
| PHA-793887 | CDK1, CDK2, CDK4, CDK5, CDK7, CDK9 |   -0.090865 |  0.001603 |  0.013624 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (17 rows total):

| drug              | target                                                       |   delta_auc |   p_value |   q_value |
|:------------------|:-------------------------------------------------------------|------------:|----------:|----------:|
| AT-7519           | CDK1, CDK2, CDK4, CDK5, CDK6, CDK9                           |   -0.036081 |  0.001256 |  0.013624 |
| PHA-793887        | CDK1, CDK2, CDK4, CDK5, CDK7, CDK9                           |   -0.090865 |  0.001603 |  0.013624 |
| dinaciclib        | CDK1, CDK2, CDK5, CDK9                                       |   -0.026623 |  0.031551 |  0.178791 |
| TG-02             | CDK1, CDK2, CDK7, CDK9, FLT3, JAK2                           |   -0.006536 |  0.221421 |  0.722523 |
| BMS-387032        | CDK2, CDK7, CDK9                                             |   -0.007714 |  0.262879 |  0.722523 |
| BX-912            | CDK2, CHEK1, GSK3B, KDR, PDK1, PDPK1                         |   -0.012173 |  0.28228  |  0.722523 |
| ryuvidine         | CDK2, CDK4                                                   |   -0.005163 |  0.29751  |  0.722523 |
| PF-573228         | CDK1, CDK2, CDK7, GSK3B, IKBKB                               |   -0.010641 |  0.409519 |  0.865122 |
| BMS-265246        | CDK1, CDK2                                                   |   -0.003664 |  0.458006 |  0.865122 |
| aminopurvalanol-a | CDK1, CDK2, CDK5, CDK6                                       |    0.002948 |  0.535387 |  0.910158 |
| SCH-900776        | CDK2, CHEK1                                                  |    0.007441 |  0.68765  |  0.993458 |
| JNJ-7706621       | AURKA, AURKB, CDK1, CDK2                                     |    0.024437 |  0.792758 |  0.993458 |
| NU6027            | CCNA2, CDK2                                                  |    0.029669 |  0.807156 |  0.993458 |
| R547              | CDK1, CDK2, CDK4, CDK7                                       |    0.028269 |  0.874613 |  0.993458 |
| alvocidib         | CDK1, CDK2, CDK4, CDK5, CDK6, CDK7, CDK8, CDK9, EGFR, PYGM   |    0.015305 |  0.876581 |  0.993458 |
| bosutinib         | ABL1, BCR, CAMK1D, CAMK2G, CDK2, FRK, FYN, HCK, LYN, MAP2... |    0.092358 |  0.954654 |  0.994432 |
| PHA-848125        | CDK2, CDK4, CDK7, NTRK1                                      |    0.052131 |  0.994432 |  0.994432 |


---

## File: phase25_prism_mek_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/phase25_prism_mek_validation.parquet`
- **Matrix Dimensions:** 17 rows × 5 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| drug          | object  |               17 |            0 | 0.00%    |
| target        | object  |               17 |            0 | 0.00%    |
| delta_auc     | float64 |               17 |            0 | 0.00%    |
| p_value       | float64 |               17 |            0 | 0.00%    |
| q_value       | float64 |               17 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|           |   count | unique   | top       | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max      |
|:----------|--------:|:---------|:----------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:---------|
| drug      |      17 | 17       | AS-703026 | 1      | —         | —        | —         | —         | —         | —         | —        |
| target    |      17 | 8        | MAP2K1    | 6      | —         | —        | —         | —         | —         | —         | —        |
| delta_auc |      17 | —        | —         | —      | -0.106430 | 0.086795 | -0.221045 | -0.172948 | -0.153665 | -0.022380 | 0.034982 |
| p_value   |      17 | —        | —         | —      | 0.166795  | 0.304694 | 0.000000  | 0.000000  | 0.000003  | 0.207577  | 0.842300 |
| q_value   |      17 | —        | —         | —      | 0.181451  | 0.321346 | 0.000000  | 0.000000  | 0.000005  | 0.271447  | 0.842300 |

### 3. Categorical Distribution Breakdown

**Column Grouping: `target`**

| Value Category                                                                                                           |   Absolute Count | Percentage Proportion   |
|:-------------------------------------------------------------------------------------------------------------------------|-----------------:|:------------------------|
| MAP2K1                                                                                                                   |                6 | 35.29%                  |
| MAP2K1, MAP2K2                                                                                                           |                5 | 29.41%                  |
| MAP2K1, MAP3K1, MAP3K2                                                                                                   |                1 | 5.88%                   |
| AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAP2K2, MAP2K7, MAPK1, MAPK11, MAPK12, MAPK14, MAPK8, PRKCA, RAF1, ROCK1, RPS6KB1, SGK1 |                1 | 5.88%                   |
| MAP2K2                                                                                                                   |                1 | 5.88%                   |
| AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAPK1, MAPK11, MAPK12, MAPK14, MAPK8, PRKCA, RAF1, ROCK1, RPS6KB1, SGK1                 |                1 | 5.88%                   |
| ABL1, BCR, CAMK1D, CAMK2G, CDK2, FRK, FYN, HCK, LYN, MAP2K1, MAP2K2, MAP3K2, MAP4K5, SRC, STK10, STK24, STK4, TNK2, TXK  |                1 | 5.88%                   |
| CHUK, MAP2K1                                                                                                             |                1 | 5.88%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **12** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug        | target         |   delta_auc |   p_value |   q_value |
|:------------|:---------------|------------:|----------:|----------:|
| AS-703026   | MAP2K1, MAP2K2 |   -0.178683 |         0 |         0 |
| selumetinib | MAP2K1         |   -0.221045 |         0 |         0 |
| trametinib  | MAP2K1, MAP2K2 |   -0.167878 |         0 |         0 |
| PD-318088   | MAP2K1         |   -0.183536 |         0 |         0 |
| TAK-733     | MAP2K1         |   -0.153665 |         0 |         0 |

- 💡 **Significance Hit:** Column `q_value` contains **12** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug        | target         |   delta_auc |   p_value |   q_value |
|:------------|:---------------|------------:|----------:|----------:|
| AS-703026   | MAP2K1, MAP2K2 |   -0.178683 |         0 |         0 |
| selumetinib | MAP2K1         |   -0.221045 |         0 |         0 |
| trametinib  | MAP2K1, MAP2K2 |   -0.167878 |         0 |         0 |
| PD-318088   | MAP2K1         |   -0.183536 |         0 |         0 |
| TAK-733     | MAP2K1         |   -0.153665 |         0 |         0 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (17 rows total):

| drug             | target                                                       |   delta_auc |   p_value |   q_value |
|:-----------------|:-------------------------------------------------------------|------------:|----------:|----------:|
| AS-703026        | MAP2K1, MAP2K2                                               |   -0.178683 |  0        |  0        |
| selumetinib      | MAP2K1                                                       |   -0.221045 |  0        |  0        |
| trametinib       | MAP2K1, MAP2K2                                               |   -0.167878 |  0        |  0        |
| PD-318088        | MAP2K1                                                       |   -0.183536 |  0        |  0        |
| TAK-733          | MAP2K1                                                       |   -0.153665 |  0        |  0        |
| MEK162           | MAP2K1, MAP2K2                                               |   -0.164189 |  0        |  0        |
| PD-184352        | MAP2K1, MAP3K1, MAP3K2                                       |   -0.172948 |  0        |  0        |
| PD-0325901       | MAP2K1                                                       |   -0.183071 |  0        |  1e-06    |
| Ro-4987655       | MAP2K1                                                       |   -0.168835 |  3e-06    |  5e-06    |
| refametinib      | MAP2K1, MAP2K2                                               |   -0.125569 |  9e-06    |  1.5e-05  |
| PD-198306        | MAP2K1, MAP2K2                                               |   -0.075902 |  5.9e-05  |  9.1e-05  |
| U-0126           | AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAP2K2, MAP2K7, MAPK1, M... |   -0.056312 |  0.003121 |  0.004421 |
| MEK1-2-inhibitor | MAP2K2                                                       |   -0.018212 |  0.207577 |  0.271447 |
| PD-98059         | AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAPK1, MAPK11, MAPK12, M... |   -0.02238  |  0.290609 |  0.352883 |
| nobiletin        | MAP2K1                                                       |    0.019889 |  0.680478 |  0.771208 |
| bosutinib        | ABL1, BCR, CAMK1D, CAMK2G, CDK2, FRK, FYN, HCK, LYN, MAP2... |    0.034982 |  0.811352 |  0.8423   |
| arctigenin       | CHUK, MAP2K1                                                 |    0.028048 |  0.8423   |  0.8423   |


---

## File: prism_pharmacologic_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/prism_pharmacologic_validation.parquet`
- **Matrix Dimensions:** 17 rows × 5 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| drug          | object  |               17 |            0 | 0.00%    |
| target        | object  |               17 |            0 | 0.00%    |
| delta_auc     | float64 |               17 |            0 | 0.00%    |
| p_value       | float64 |               17 |            0 | 0.00%    |
| q_value       | float64 |               17 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|           |   count | unique   | top       | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max      |
|:----------|--------:|:---------|:----------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:---------|
| drug      |      17 | 17       | AS-703026 | 1      | —         | —        | —         | —         | —         | —         | —        |
| target    |      17 | 8        | MAP2K1    | 6      | —         | —        | —         | —         | —         | —         | —        |
| delta_auc |      17 | —        | —         | —      | -0.106430 | 0.086795 | -0.221045 | -0.172948 | -0.153665 | -0.022380 | 0.034982 |
| p_value   |      17 | —        | —         | —      | 0.166795  | 0.304694 | 0.000000  | 0.000000  | 0.000003  | 0.207577  | 0.842300 |
| q_value   |      17 | —        | —         | —      | 0.181451  | 0.321346 | 0.000000  | 0.000000  | 0.000005  | 0.271447  | 0.842300 |

### 3. Categorical Distribution Breakdown

**Column Grouping: `target`**

| Value Category                                                                                                           |   Absolute Count | Percentage Proportion   |
|:-------------------------------------------------------------------------------------------------------------------------|-----------------:|:------------------------|
| MAP2K1                                                                                                                   |                6 | 35.29%                  |
| MAP2K1, MAP2K2                                                                                                           |                5 | 29.41%                  |
| MAP2K1, MAP3K1, MAP3K2                                                                                                   |                1 | 5.88%                   |
| AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAP2K2, MAP2K7, MAPK1, MAPK11, MAPK12, MAPK14, MAPK8, PRKCA, RAF1, ROCK1, RPS6KB1, SGK1 |                1 | 5.88%                   |
| MAP2K2                                                                                                                   |                1 | 5.88%                   |
| AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAPK1, MAPK11, MAPK12, MAPK14, MAPK8, PRKCA, RAF1, ROCK1, RPS6KB1, SGK1                 |                1 | 5.88%                   |
| ABL1, BCR, CAMK1D, CAMK2G, CDK2, FRK, FYN, HCK, LYN, MAP2K1, MAP2K2, MAP3K2, MAP4K5, SRC, STK10, STK24, STK4, TNK2, TXK  |                1 | 5.88%                   |
| CHUK, MAP2K1                                                                                                             |                1 | 5.88%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `p_value` contains **12** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug        | target         |   delta_auc |   p_value |   q_value |
|:------------|:---------------|------------:|----------:|----------:|
| AS-703026   | MAP2K1, MAP2K2 |   -0.178683 |         0 |         0 |
| selumetinib | MAP2K1         |   -0.221045 |         0 |         0 |
| trametinib  | MAP2K1, MAP2K2 |   -0.167878 |         0 |         0 |
| PD-318088   | MAP2K1         |   -0.183536 |         0 |         0 |
| TAK-733     | MAP2K1         |   -0.153665 |         0 |         0 |

- 💡 **Significance Hit:** Column `q_value` contains **12** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| drug        | target         |   delta_auc |   p_value |   q_value |
|:------------|:---------------|------------:|----------:|----------:|
| AS-703026   | MAP2K1, MAP2K2 |   -0.178683 |         0 |         0 |
| selumetinib | MAP2K1         |   -0.221045 |         0 |         0 |
| trametinib  | MAP2K1, MAP2K2 |   -0.167878 |         0 |         0 |
| PD-318088   | MAP2K1         |   -0.183536 |         0 |         0 |
| TAK-733     | MAP2K1         |   -0.153665 |         0 |         0 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (17 rows total):

| drug             | target                                                       |   delta_auc |   p_value |   q_value |
|:-----------------|:-------------------------------------------------------------|------------:|----------:|----------:|
| AS-703026        | MAP2K1, MAP2K2                                               |   -0.178683 |  0        |  0        |
| selumetinib      | MAP2K1                                                       |   -0.221045 |  0        |  0        |
| trametinib       | MAP2K1, MAP2K2                                               |   -0.167878 |  0        |  0        |
| PD-318088        | MAP2K1                                                       |   -0.183536 |  0        |  0        |
| TAK-733          | MAP2K1                                                       |   -0.153665 |  0        |  0        |
| MEK162           | MAP2K1, MAP2K2                                               |   -0.164189 |  0        |  0        |
| PD-184352        | MAP2K1, MAP3K1, MAP3K2                                       |   -0.172948 |  0        |  0        |
| PD-0325901       | MAP2K1                                                       |   -0.183071 |  0        |  1e-06    |
| Ro-4987655       | MAP2K1                                                       |   -0.168835 |  3e-06    |  5e-06    |
| refametinib      | MAP2K1, MAP2K2                                               |   -0.125569 |  9e-06    |  1.5e-05  |
| PD-198306        | MAP2K1, MAP2K2                                               |   -0.075902 |  5.9e-05  |  9.1e-05  |
| U-0126           | AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAP2K2, MAP2K7, MAPK1, M... |   -0.056312 |  0.003121 |  0.004421 |
| MEK1-2-inhibitor | MAP2K2                                                       |   -0.018212 |  0.207577 |  0.271447 |
| PD-98059         | AKT1, CHEK1, GSK3B, LCK, MAP2K1, MAPK1, MAPK11, MAPK12, M... |   -0.02238  |  0.290609 |  0.352883 |
| nobiletin        | MAP2K1                                                       |    0.019889 |  0.680478 |  0.771208 |
| bosutinib        | ABL1, BCR, CAMK1D, CAMK2G, CDK2, FRK, FYN, HCK, LYN, MAP2... |    0.034982 |  0.811352 |  0.8423   |
| arctigenin       | CHUK, MAP2K1                                                 |    0.028048 |  0.8423   |  0.8423   |


---

## File: robustness_summary.csv

- **Source Framework Category:** Robustness CSV
- **Project Relative Path:** `results/robustness/robustness_summary.csv`
- **Matrix Dimensions:** 4 rows × 8 columns

### 1. Data Schema & Quality Audit

| Column Name                | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:---------------------------|:--------|-----------------:|-------------:|:---------|
| label                      | object  |                4 |            0 | 0.00%    |
| sanger_concordance         | float64 |                4 |            0 | 0.00%    |
| sanger_p_neg               | float64 |                4 |            0 | 0.00%    |
| depmap_concordance         | float64 |                4 |            0 | 0.00%    |
| depmap_p_neg               | float64 |                4 |            0 | 0.00%    |
| mutation_min_mutant_models | float64 |                2 |            2 | 50.00%   |
| random_seed                | int64   |                4 |            0 | 0.00%    |
| corum_min_size             | float64 |                2 |            2 | 50.00%   |

### 2. Full Descriptive Summary Statistics

|                            |   count | unique   | top       | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:---------------------------|--------:|:---------|:----------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| label                      |       4 | 4        | min_mut_5 | 1      | —         | —        | —         | —         | —         | —         | —         |
| sanger_concordance         |       4 | —        | —         | —      | 0.879545  | 0.040909 | 0.818182  | 0.879545  | 0.900000  | 0.900000  | 0.900000  |
| sanger_p_neg               |       4 | —        | —         | —      | 0.988600  | 0.000400 | 0.988000  | 0.988600  | 0.988800  | 0.988800  | 0.988800  |
| depmap_concordance         |       4 | —        | —         | —      | 1.000000  | 0.000000 | 1.000000  | 1.000000  | 1.000000  | 1.000000  | 1.000000  |
| depmap_p_neg               |       4 | —        | —         | —      | 0.998000  | 0.000000 | 0.998000  | 0.998000  | 0.998000  | 0.998000  | 0.998000  |
| mutation_min_mutant_models |       2 | —        | —         | —      | 7.500000  | 3.535534 | 5.000000  | 6.250000  | 7.500000  | 8.750000  | 10.000000 |
| random_seed                |       4 | —        | —         | —      | 43.500000 | 1.290994 | 42.000000 | 42.750000 | 43.500000 | 44.250000 | 45.000000 |
| corum_min_size             |       2 | —        | —         | —      | 2.500000  | 0.707107 | 2.000000  | 2.250000  | 2.500000  | 2.750000  | 3.000000  |

### 3. Categorical Distribution Breakdown

**Column Grouping: `label`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| min_mut_5        |                1 | 25.0%                   |
| min_mut_10       |                1 | 25.0%                   |
| corum_min_2      |                1 | 25.0%                   |
| corum_min_3      |                1 | 25.0%                   |

### 4. Significant Signals & Key Highlights

- 📊 **Concordance Metric Profile (`sanger_concordance`):** Mean=0.87955, Max=0.90000, Min=0.81818
- 📊 **Concordance Metric Profile (`depmap_concordance`):** Mean=1.00000, Max=1.00000, Min=1.00000

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (4 rows total):

| label       |   sanger_concordance |   sanger_p_neg |   depmap_concordance |   depmap_p_neg |   mutation_min_mutant_models |   random_seed |   corum_min_size |
|:------------|---------------------:|---------------:|---------------------:|---------------:|-----------------------------:|--------------:|-----------------:|
| min_mut_5   |             0.818182 |         0.988  |                    1 |          0.998 |                            5 |            42 |              nan |
| min_mut_10  |             0.9      |         0.9888 |                    1 |          0.998 |                           10 |            43 |              nan |
| corum_min_2 |             0.9      |         0.9888 |                    1 |          0.998 |                          nan |            44 |                2 |
| corum_min_3 |             0.9      |         0.9888 |                    1 |          0.998 |                          nan |            45 |                3 |


---

## File: sanger_cohort_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/sanger_cohort_validation.parquet`
- **Matrix Dimensions:** 11 rows × 12 columns

### 1. Data Schema & Quality Audit

| Column Name                 | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------------------|:--------|-----------------:|-------------:|:---------|
| undirected_key              | object  |               11 |            0 | 0.00%    |
| mutation_gene               | object  |               11 |            0 | 0.00%    |
| partner_gene                | object  |               11 |            0 | 0.00%    |
| mutation_type               | object  |               11 |            0 | 0.00%    |
| external_delta_dependency   | float64 |                9 |            2 | 18.18%   |
| external_p_value            | float64 |                9 |            2 | 18.18%   |
| external_num_mutant         | int64   |               11 |            0 | 0.00%    |
| external_num_wildtype       | int64   |               11 |            0 | 0.00%    |
| external_se                 | float64 |                9 |            2 | 18.18%   |
| same_direction_as_discovery | bool    |               11 |            0 | 0.00%    |
| passes_external_nominal     | bool    |               11 |            0 | 0.00%    |
| external_gene_available     | bool    |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                             |   count | unique   | top         | freq   | mean       | std       | min       | 25%        | 50%        | 75%        | max        |
|:----------------------------|--------:|:---------|:------------|:-------|:-----------|:----------|:----------|:-----------|:-----------|:-----------|:-----------|
| undirected_key              |      11 | 11       | AP3B2:AP3M2 | 1      | —          | —         | —         | —          | —          | —          | —          |
| mutation_gene               |      11 | 11       | AP3B2       | 1      | —          | —         | —         | —          | —          | —          | —          |
| partner_gene                |      11 | 11       | AP3M2       | 1      | —          | —         | —         | —          | —          | —          | —          |
| mutation_type               |      11 | 2        | damaging    | 8      | —          | —         | —         | —          | —          | —          | —          |
| external_delta_dependency   |       9 | —        | —           | —      | -2.794659  | 3.246963  | -9.320826 | -2.703582  | -1.577966  | -0.601137  | -0.182734  |
| external_p_value            |       9 | —        | —           | —      | 0.114875   | 0.164178  | 0.000000  | 0.001653   | 0.014770   | 0.284608   | 0.408136   |
| external_num_mutant         |      11 | —        | —           | —      | 15.363636  | 16.983950 | 0.000000  | 4.500000   | 11.000000  | 19.500000  | 59.000000  |
| external_num_wildtype       |      11 | —        | —           | —      | 276.454545 | 93.110003 | 0.000000  | 296.500000 | 307.000000 | 315.500000 | 319.000000 |
| external_se                 |       9 | —        | —           | —      | 0.932982   | 0.524553  | 0.331161  | 0.419397   | 0.922898   | 1.287535   | 1.880686   |
| same_direction_as_discovery |      11 | 2        | True        | 9      | —          | —         | —         | —          | —          | —          | —          |
| passes_external_nominal     |      11 | 2        | True        | 6      | —          | —         | —         | —          | —          | —          | —          |
| external_gene_available     |      11 | 2        | True        | 10     | —          | —         | —         | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `undirected_key`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2            |                1 | 9.09%                   |
| APC              |                1 | 9.09%                   |
| BRAF             |                1 | 9.09%                   |
| ITGA6            |                1 | 9.09%                   |
| EP300            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| DCP2             |                1 | 9.09%                   |
| IFT122           |                1 | 9.09%                   |
| IL2RG            |                1 | 9.09%                   |
| NRAS             |                1 | 9.09%                   |
| SMARCA4          |                1 | 9.09%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3M2            |                1 | 9.09%                   |
| CTNNB1           |                1 | 9.09%                   |
| MAP2K1           |                1 | 9.09%                   |
| CD151            |                1 | 9.09%                   |
| CREBBP           |                1 | 9.09%                   |
| TCF7L2           |                1 | 9.09%                   |
| XRN1             |                1 | 9.09%                   |
| WDR35            |                1 | 9.09%                   |
| IL2              |                1 | 9.09%                   |
| SHOC2            |                1 | 9.09%                   |
| SMARCA2          |                1 | 9.09%                   |

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |                8 | 72.73%                  |
| hotspot          |                3 | 27.27%                  |

**Column Grouping: `same_direction_as_discovery`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |                9 | 81.82%                  |
| False            |                2 | 18.18%                  |

**Column Grouping: `passes_external_nominal`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |                6 | 54.55%                  |
| False            |                5 | 45.45%                  |

**Column Grouping: `external_gene_available`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |               10 | 90.91%                  |
| False            |                1 | 9.09%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `external_p_value` contains **6** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                    -9.32083 |           0        |                    29 |                     292 |      1.28754  | True                          | True                      | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                    -2.70358 |           0.000596 |                    59 |                     262 |      0.798418 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                    -7.17211 |           0.001653 |                    11 |                     310 |      1.88069  | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                    -2.22019 |           0.012944 |                    20 |                     301 |      0.922898 | True                          | True                      | True                      |
| IL2:IL2RG        | IL2RG           | IL2            | damaging        |                    -1.57797 |           0.01477  |                     4 |                     317 |      0.419397 | True                          | True                      | True                      |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| undirected_key   | mutation_gene   | partner_gene   | mutation_type   |   external_delta_dependency |   external_p_value |   external_num_mutant |   external_num_wildtype |   external_se | same_direction_as_discovery   | passes_external_nominal   | external_gene_available   |
|:-----------------|:----------------|:---------------|:----------------|----------------------------:|-------------------:|----------------------:|------------------------:|--------------:|:------------------------------|:--------------------------|:--------------------------|
| AP3B2:AP3M2      | AP3B2           | AP3M2          | damaging        |                   -0.601137 |           0.284608 |                     5 |                     316 |      0.97212  | True                          | False                     | True                      |
| APC:CTNNB1       | APC             | CTNNB1         | damaging        |                   -9.32083  |           0        |                    29 |                     292 |      1.28754  | True                          | True                      | True                      |
| BRAF:MAP2K1      | BRAF            | MAP2K1         | hotspot         |                   -0.333282 |           0.408136 |                    14 |                     307 |      1.40631  | True                          | False                     | True                      |
| CD151:ITGA6      | ITGA6           | CD151          | damaging        |                   -0.182734 |           0.293465 |                    19 |                     302 |      0.331161 | True                          | False                     | True                      |
| CREBBP:EP300     | EP300           | CREBBP         | damaging        |                   -2.70358  |           0.000596 |                    59 |                     262 |      0.798418 | True                          | True                      | True                      |
| CTNNB1:TCF7L2    | CTNNB1          | TCF7L2         | hotspot         |                  nan        |         nan        |                     0 |                       0 |    nan        | False                         | False                     | False                     |
| DCP2:XRN1        | DCP2            | XRN1           | damaging        |                  nan        |         nan        |                     2 |                     319 |    nan        | False                         | False                     | True                      |
| IFT122:WDR35     | IFT122          | WDR35          | damaging        |                   -1.0401   |           0.017701 |                     6 |                     315 |      0.378315 | True                          | True                      | True                      |
| IL2:IL2RG        | IL2RG           | IL2            | damaging        |                   -1.57797  |           0.01477  |                     4 |                     317 |      0.419397 | True                          | True                      | True                      |
| NRAS:SHOC2       | NRAS            | SHOC2          | hotspot         |                   -7.17211  |           0.001653 |                    11 |                     310 |      1.88069  | True                          | True                      | True                      |
| SMARCA2:SMARCA4  | SMARCA4         | SMARCA2        | damaging        |                   -2.22019  |           0.012944 |                    20 |                     301 |      0.922898 | True                          | True                      | True                      |


---

## File: sanger_continuous_meta_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/sanger_continuous_meta_summary.parquet`
- **Matrix Dimensions:** 1 rows × 13 columns

### 1. Data Schema & Quality Audit

| Column Name     | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------|:--------|-----------------:|-------------:|:---------|
| context         | object  |                1 |            0 | 0.00%    |
| endpoint_type   | object  |                1 |            0 | 0.00%    |
| effect_col      | object  |                1 |            0 | 0.00%    |
| se_col          | object  |                1 |            0 | 0.00%    |
| n_rows          | int64   |                1 |            0 | 0.00%    |
| n_unique_groups | int64   |                1 |            0 | 0.00%    |
| meta_mu         | float64 |                1 |            0 | 0.00%    |
| meta_se         | float64 |                1 |            0 | 0.00%    |
| meta_ci_low     | float64 |                1 |            0 | 0.00%    |
| meta_ci_high    | float64 |                1 |            0 | 0.00%    |
| meta_p          | float64 |                1 |            0 | 0.00%    |
| meta_i2         | float64 |                1 |            0 | 0.00%    |
| meta_tau2       | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                 |   count | unique   | top                       | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:----------------|--------:|:---------|:--------------------------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| context         |       1 | 1        | Sanger                    | 1      | —         | —     | —         | —         | —         | —         | —         |
| endpoint_type   |       1 | 1        | continuous                | 1      | —         | —     | —         | —         | —         | —         | —         |
| effect_col      |       1 | 1        | external_delta_dependency | 1      | —         | —     | —         | —         | —         | —         | —         |
| se_col          |       1 | 1        | external_se               | 1      | —         | —     | —         | —         | —         | —         | —         |
| n_rows          |       1 | —        | —                         | —      | 9.000000  | —     | 9.000000  | 9.000000  | 9.000000  | 9.000000  | 9.000000  |
| n_unique_groups |       1 | —        | —                         | —      | 9.000000  | —     | 9.000000  | 9.000000  | 9.000000  | 9.000000  | 9.000000  |
| meta_mu         |       1 | —        | —                         | —      | -2.371364 | —     | -2.371364 | -2.371364 | -2.371364 | -2.371364 | -2.371364 |
| meta_se         |       1 | —        | —                         | —      | 0.639285  | —     | 0.639285  | 0.639285  | 0.639285  | 0.639285  | 0.639285  |
| meta_ci_low     |       1 | —        | —                         | —      | -3.624362 | —     | -3.624362 | -3.624362 | -3.624362 | -3.624362 | -3.624362 |
| meta_ci_high    |       1 | —        | —                         | —      | -1.118366 | —     | -1.118366 | -1.118366 | -1.118366 | -1.118366 | -1.118366 |
| meta_p          |       1 | —        | —                         | —      | 0.000208  | —     | 0.000208  | 0.000208  | 0.000208  | 0.000208  | 0.000208  |
| meta_i2         |       1 | —        | —                         | —      | 0.878410  | —     | 0.878410  | 0.878410  | 0.878410  | 0.878410  | 0.878410  |
| meta_tau2       |       1 | —        | —                         | —      | 2.794024  | —     | 2.794024  | 2.794024  | 2.794024  | 2.794024  | 2.794024  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **1** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context   | endpoint_type   | effect_col                | se_col      |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:----------|:----------------|:--------------------------|:------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| Sanger    | continuous      | external_delta_dependency | external_se |        9 |                 9 |  -2.37136 |  0.639285 |      -3.62436 |       -1.11837 | 0.000208 |   0.87841 |     2.79402 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| context   | endpoint_type   | effect_col                | se_col      |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:----------|:----------------|:--------------------------|:------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| Sanger    | continuous      | external_delta_dependency | external_se |        9 |                 9 |  -2.37136 |  0.639285 |      -3.62436 |       -1.11837 | 0.000208 |   0.87841 |     2.79402 |


---

## File: sanger_leave_one_out.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/sanger_leave_one_out.parquet`
- **Matrix Dimensions:** 9 rows × 10 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| context       | object  |                9 |            0 | 0.00%    |
| omitted_group | object  |                9 |            0 | 0.00%    |
| n_remaining   | int64   |                9 |            0 | 0.00%    |
| meta_mu       | float64 |                9 |            0 | 0.00%    |
| meta_se       | float64 |                9 |            0 | 0.00%    |
| meta_ci_low   | float64 |                9 |            0 | 0.00%    |
| meta_ci_high  | float64 |                9 |            0 | 0.00%    |
| meta_p        | float64 |                9 |            0 | 0.00%    |
| meta_i2       | float64 |                9 |            0 | 0.00%    |
| meta_tau2     | float64 |                9 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|               |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:--------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| context       |       9 | 1        | Sanger      | 9      | —         | —        | —         | —         | —         | —         | —         |
| omitted_group |       9 | 9        | AP3B2:AP3M2 | 1      | —         | —        | —         | —         | —         | —         | —         |
| n_remaining   |       9 | —        | —           | —      | 8.000000  | 0.000000 | 8.000000  | 8.000000  | 8.000000  | 8.000000  | 8.000000  |
| meta_mu       |       9 | —        | —           | —      | -2.387525 | 0.405956 | -2.772805 | -2.611024 | -2.575692 | -2.340845 | -1.486186 |
| meta_se       |       9 | —        | —           | —      | 0.685427  | 0.107732 | 0.441685  | 0.679699  | 0.696984  | 0.741089  | 0.810210  |
| meta_ci_low   |       9 | —        | —           | —      | -3.730962 | 0.606953 | -4.276149 | -4.129302 | -3.907902 | -3.701681 | -2.351889 |
| meta_ci_high  |       9 | —        | —           | —      | -1.044088 | 0.224457 | -1.320271 | -1.243482 | -1.046625 | -0.980009 | -0.620483 |
| meta_p        |       9 | —        | —           | —      | 0.000628  | 0.000383 | 0.000151  | 0.000183  | 0.000748  | 0.000907  | 0.001172  |
| meta_i2       |       9 | —        | —           | —      | 0.867871  | 0.054834 | 0.724519  | 0.874346  | 0.891629  | 0.892898  | 0.893052  |
| meta_tau2     |       9 | —        | —           | —      | 2.956341  | 0.938581 | 0.922735  | 2.908971  | 2.987495  | 3.357655  | 4.193507  |

### 3. Categorical Distribution Breakdown

**Column Grouping: `omitted_group`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 11.11%                  |
| APC:CTNNB1       |                1 | 11.11%                  |
| BRAF:MAP2K1      |                1 | 11.11%                  |
| CD151:ITGA6      |                1 | 11.11%                  |
| CREBBP:EP300     |                1 | 11.11%                  |
| IFT122:WDR35     |                1 | 11.11%                  |
| IL2:IL2RG        |                1 | 11.11%                  |
| NRAS:SHOC2       |                1 | 11.11%                  |
| SMARCA2:SMARCA4  |                1 | 11.11%                  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **9** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context   | omitted_group   |   n_remaining |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:----------|:----------------|--------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| Sanger    | BRAF:MAP2K1     |             8 |  -2.57569 |  0.679699 |      -3.9079  |      -1.24348  | 0.000151 |  0.892933 |     2.90897 |
| Sanger    | AP3B2:AP3M2     |             8 |  -2.61102 |  0.697698 |      -3.97851 |      -1.24354  | 0.000182 |  0.892898 |     3.00613 |
| Sanger    | CD151:ITGA6     |             8 |  -2.7728  |  0.741089 |      -4.22534 |      -1.32027  | 0.000183 |  0.861852 |     3.35765 |
| Sanger    | SMARCA2:SMARCA4 |             8 |  -2.41031 |  0.696984 |      -3.77639 |      -1.04422  | 0.000544 |  0.891629 |     2.9875  |
| Sanger    | CREBBP:EP300    |             8 |  -2.34084 |  0.694304 |      -3.70168 |      -0.980009 | 0.000748 |  0.887426 |     2.93136 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (9 rows total):

| context   | omitted_group   |   n_remaining |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:----------|:----------------|--------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| Sanger    | AP3B2:AP3M2     |             8 |  -2.61102 |  0.697698 |      -3.97851 |      -1.24354  | 0.000182 |  0.892898 |    3.00613  |
| Sanger    | APC:CTNNB1      |             8 |  -1.48619 |  0.441685 |      -2.35189 |      -0.620483 | 0.000766 |  0.724519 |    0.922735 |
| Sanger    | BRAF:MAP2K1     |             8 |  -2.57569 |  0.679699 |      -3.9079  |      -1.24348  | 0.000151 |  0.892933 |    2.90897  |
| Sanger    | CD151:ITGA6     |             8 |  -2.7728  |  0.741089 |      -4.22534 |      -1.32027  | 0.000183 |  0.861852 |    3.35765  |
| Sanger    | CREBBP:EP300    |             8 |  -2.34084 |  0.694304 |      -3.70168 |      -0.980009 | 0.000748 |  0.887426 |    2.93136  |
| Sanger    | IFT122:WDR35    |             8 |  -2.68814 |  0.81021  |      -4.27615 |      -1.10013  | 0.000907 |  0.893052 |    4.19351  |
| Sanger    | IL2:IL2RG       |             8 |  -2.58796 |  0.786397 |      -4.1293  |      -1.04662  | 0.000999 |  0.892185 |    3.90435  |
| Sanger    | NRAS:SHOC2      |             8 |  -2.01477 |  0.620779 |      -3.23149 |      -0.798038 | 0.001172 |  0.874346 |    2.39487  |
| Sanger    | SMARCA2:SMARCA4 |             8 |  -2.41031 |  0.696984 |      -3.77639 |      -1.04422  | 0.000544 |  0.891629 |    2.9875   |


---

## File: sensitivity_backbone_off_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/sensitivity_backbone_off_summary.parquet`
- **Matrix Dimensions:** 1 rows × 5 columns

### 1. Data Schema & Quality Audit

| Column Name          | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:---------------------|:--------|-----------------:|-------------:|:---------|
| topology             | object  |                1 |            0 | 0.00%    |
| backbone             | object  |                1 |            0 | 0.00%    |
| overlap_mean_hlrc    | float64 |                1 |            0 | 0.00%    |
| background_mean_hlrc | float64 |                1 |            0 | 0.00%    |
| delta                | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                      |   count | unique   | top    | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:---------------------|--------:|:---------|:-------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| topology             |       1 | 1        | STRING | 1      | —         | —     | —         | —         | —         | —         | —         |
| backbone             |       1 | 1        | OFF    | 1      | —         | —     | —         | —         | —         | —         | —         |
| overlap_mean_hlrc    |       1 | —        | —      | —      | -0.710965 | —     | -0.710965 | -0.710965 | -0.710965 | -0.710965 | -0.710965 |
| background_mean_hlrc |       1 | —        | —      | —      | -0.248657 | —     | -0.248657 | -0.248657 | -0.248657 | -0.248657 | -0.248657 |
| delta                |       1 | —        | —      | —      | -0.462307 | —     | -0.462307 | -0.462307 | -0.462307 | -0.462307 | -0.462307 |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| topology   | backbone   |   overlap_mean_hlrc |   background_mean_hlrc |     delta |
|:-----------|:-----------|--------------------:|-----------------------:|----------:|
| STRING     | OFF        |           -0.710965 |              -0.248657 | -0.462307 |


---

## File: sensitivity_backbone_on_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/sensitivity_backbone_on_summary.parquet`
- **Matrix Dimensions:** 1 rows × 5 columns

### 1. Data Schema & Quality Audit

| Column Name          | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:---------------------|:--------|-----------------:|-------------:|:---------|
| topology             | object  |                1 |            0 | 0.00%    |
| backbone             | object  |                1 |            0 | 0.00%    |
| overlap_mean_hlrc    | float64 |                1 |            0 | 0.00%    |
| background_mean_hlrc | float64 |                1 |            0 | 0.00%    |
| delta                | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                      |   count | unique   | top    | freq   | mean      | std   | min       | 25%       | 50%       | 75%       | max       |
|:---------------------|--------:|:---------|:-------|:-------|:----------|:------|:----------|:----------|:----------|:----------|:----------|
| topology             |       1 | 1        | STRING | 1      | —         | —     | —         | —         | —         | —         | —         |
| backbone             |       1 | 1        | ON     | 1      | —         | —     | —         | —         | —         | —         | —         |
| overlap_mean_hlrc    |       1 | —        | —      | —      | -0.584272 | —     | -0.584272 | -0.584272 | -0.584272 | -0.584272 | -0.584272 |
| background_mean_hlrc |       1 | —        | —      | —      | -0.260839 | —     | -0.260839 | -0.260839 | -0.260839 | -0.260839 | -0.260839 |
| delta                |       1 | —        | —      | —      | -0.323432 | —     | -0.323432 | -0.323432 | -0.323432 | -0.323432 | -0.323432 |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| topology   | backbone   |   overlap_mean_hlrc |   background_mean_hlrc |     delta |
|:-----------|:-----------|--------------------:|-----------------------:|----------:|
| STRING     | ON         |           -0.584272 |              -0.260839 | -0.323432 |


---

## File: string_family_pair_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/string_family_pair_summary.parquet`
- **Matrix Dimensions:** 79274 rows × 19 columns

### 1. Data Schema & Quality Audit

| Column Name               | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------------|:--------|-----------------:|-------------:|:---------|
| pair_key                  | object  |            79274 |            0 | 0.00%    |
| min_hfrc                  | float64 |            79274 |            0 | 0.00%    |
| median_hfrc               | float64 |            79274 |            0 | 0.00%    |
| mean_hfrc                 | float64 |            79274 |            0 | 0.00%    |
| min_hlrc                  | float64 |            79274 |            0 | 0.00%    |
| median_hlrc               | float64 |            79274 |            0 | 0.00%    |
| mean_hlrc                 | float64 |            79274 |            0 | 0.00%    |
| mean_hyperedge_size       | float64 |            79274 |            0 | 0.00%    |
| min_hlrc_hyperedge_size   | int64   |            79274 |            0 | 0.00%    |
| mean_edge_node_degree     | float64 |            79274 |            0 | 0.00%    |
| mean_pair_essentiality    | float64 |            79274 |            0 | 0.00%    |
| pair_max_node_degree      | int64   |            79274 |            0 | 0.00%    |
| pair_hyperedge_count      | int64   |            79274 |            0 | 0.00%    |
| is_systematic_candidate   | int64   |            79274 |            0 | 0.00%    |
| is_validated_candidate    | int64   |            79274 |            0 | 0.00%    |
| log_pair_hyperedge_count  | float64 |            79274 |            0 | 0.00%    |
| log_pair_max_node_degree  | float64 |            79274 |            0 | 0.00%    |
| log_mean_edge_node_degree | float64 |            79274 |            0 | 0.00%    |
| log_mean_hyperedge_size   | float64 |            79274 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                           |   count | unique   | top         | freq   | mean         | std         | min          | 25%          | 50%         | 75%        | max        |
|:--------------------------|--------:|:---------|:------------|:-------|:-------------|:------------|:-------------|:-------------|:------------|:-----------|:-----------|
| pair_key                  |   79274 | 79274    | A1BG:CRISP3 | 1      | —            | —           | —            | —            | —           | —          | —          |
| min_hfrc                  |   79274 | —        | —           | —      | -1118.240470 | 1404.460809 | -5877.000000 | -1802.000000 | -458.000000 | -88.000000 | 9.000000   |
| median_hfrc               |   79274 | —        | —           | —      | -950.319468  | 1253.566281 | -5627.000000 | -1129.000000 | -365.000000 | -78.500000 | 9.000000   |
| mean_hfrc                 |   79274 | —        | —           | —      | -946.652961  | 1218.935729 | -5405.300000 | -1285.444444 | -373.000000 | -80.250000 | 9.000000   |
| min_hlrc                  |   79274 | —        | —           | —      | -0.248716    | 0.457065    | -0.987050    | -0.655155    | -0.305079   | 0.085619   | 1.000000   |
| median_hlrc               |   79274 | —        | —           | —      | -0.150444    | 0.433417    | -0.987050    | -0.503389    | -0.122891   | 0.132296   | 1.000000   |
| mean_hlrc                 |   79274 | —        | —           | —      | -0.145306    | 0.427433    | -0.987050    | -0.488474    | -0.125219   | 0.132625   | 1.000000   |
| mean_hyperedge_size       |   79274 | —        | —           | —      | 23.798326    | 23.411268   | 2.000000     | 5.000000     | 14.000000   | 37.000000  | 84.000000  |
| min_hlrc_hyperedge_size   |   79274 | —        | —           | —      | 19.956430    | 20.881088   | 2.000000     | 5.000000     | 11.000000   | 29.000000  | 84.000000  |
| mean_edge_node_degree     |   79274 | —        | —           | —      | 42.607295    | 46.093390   | 1.000000     | 12.361111    | 25.666667   | 52.115278  | 285.333333 |
| mean_pair_essentiality    |   79274 | —        | —           | —      | -0.632173    | 0.694680    | -4.586777    | -1.035081    | -0.398330   | -0.072329  | 0.352184   |
| pair_max_node_degree      |   79274 | —        | —           | —      | 52.408583    | 72.559261   | 1.000000     | 10.000000    | 25.000000   | 57.000000  | 443.000000 |
| pair_hyperedge_count      |   79274 | —        | —           | —      | 5.547695     | 12.337343   | 1.000000     | 1.000000     | 2.000000    | 5.000000   | 246.000000 |
| is_systematic_candidate   |   79274 | —        | —           | —      | 0.000290     | 0.017031    | 0.000000     | 0.000000     | 0.000000    | 0.000000   | 1.000000   |
| is_validated_candidate    |   79274 | —        | —           | —      | 0.006219     | 0.078615    | 0.000000     | 0.000000     | 0.000000    | 0.000000   | 1.000000   |
| log_pair_hyperedge_count  |   79274 | —        | —           | —      | 1.349609     | 0.847959    | 0.693147     | 0.693147     | 1.098612    | 1.791759   | 5.509388   |
| log_pair_max_node_degree  |   79274 | —        | —           | —      | 3.275117     | 1.207816    | 0.693147     | 2.397895     | 3.258097    | 4.060443   | 6.095825   |
| log_mean_edge_node_degree |   79274 | —        | —           | —      | 3.262924     | 1.060547    | 0.693147     | 2.592348     | 3.283414    | 3.972465   | 5.657157   |
| log_mean_hyperedge_size   |   79274 | —        | —           | —      | 2.723674     | 1.028676    | 1.098612     | 1.791759     | 2.708050    | 3.637586   | 4.442651   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| pair_key      |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:--------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| A1BG:CRISP3   |          1 |           1   |      1      |   0.333333 |      0.333333 |    0.333333 |               2       |                         2 |                 1.5     |                 0.048835 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.916291 |                   1.09861 |
| A1BG:GRB2     |       -502 |        -502   |   -502      |  -0.478311 |     -0.478311 |   -0.478311 |               3       |                         3 |               169.333   |                -0.50401  |                    352 |                      1 |                         0 |                        0 |                   0.693147 |                   5.86647  |                    5.13776  |                   1.38629 |
| A1BG:PTPN11   |       -502 |        -502   |   -502      |  -0.478311 |     -0.478311 |   -0.478311 |               3       |                         3 |               169.333   |                -0.360209 |                    154 |                      1 |                         0 |                        0 |                   0.693147 |                   5.04343  |                    5.13776  |                   1.38629 |
| A1CF:APOBEC1  |          0 |           0   |      0      |   0.25     |      0.25     |    0.25     |               2       |                         2 |                 2       |                -0.053671 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                   1.38629  |                    1.09861  |                   1.09861 |
| A1CF:APOBEC3F |         -1 |          -1   |     -1      |   0.208333 |      0.208333 |    0.208333 |               3       |                         3 |                 2.33333 |                 0.08001  |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                   1.38629  |                    1.20397  |                   1.38629 |
| A1CF:APOBEC3G |         -1 |          -1   |     -1      |   0.208333 |      0.208333 |    0.208333 |               3       |                         3 |                 2.33333 |                 0.025798 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                   1.38629  |                    1.20397  |                   1.38629 |
| A1CF:SYNCRIP  |        -13 |         -13   |    -13      |  -0.7      |     -0.7      |   -0.7      |               2       |                         2 |                 8.5     |                -0.187088 |                     14 |                      1 |                         0 |                        0 |                   0.693147 |                   2.70805  |                    2.25129  |                   1.09861 |
| A2M:ALB       |       -115 |         -85   |    -93.6667 |  -0.826253 |     -0.732345 |   -0.731596 |               4       |                         4 |                25.4167  |                 0.036788 |                     31 |                      3 |                         0 |                        0 |                   1.38629  |                   3.46574  |                    3.274    |                   1.60944 |
| A2M:APOA1     |       -115 |         -85   |    -91.8    |  -0.831304 |     -0.737395 |   -0.752698 |               4       |                         4 |                24.95    |                 0.009016 |                     30 |                      5 |                         0 |                        0 |                   1.79176  |                   3.43399  |                    3.25617  |                   1.60944 |
| A2M:APOE      |       -115 |        -104   |    -97      |  -0.856791 |     -0.831304 |   -0.838116 |               3.66667 |                         3 |                28.25    |                 0.005862 |                     40 |                      3 |                         0 |                        0 |                   1.38629  |                   3.71357  |                    3.37588  |                   1.54045 |
| A2M:CLU       |       -104 |         -77   |    -85      |  -0.877964 |     -0.831304 |   -0.815554 |               3.66667 |                         3 |                25.3889  |                 0.014129 |                     22 |                      3 |                         0 |                        0 |                   1.38629  |                   3.13549  |                    3.27294  |                   1.54045 |
| A2M:HAMP      |        -22 |         -22   |    -22      |  -0.706522 |     -0.706522 |   -0.706522 |               2       |                         2 |                13       |                -0.192661 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.63906  |                   1.09861 |
| A2M:HP        |        -81 |         -81   |    -81      |  -0.636191 |     -0.636191 |   -0.636191 |               4       |                         4 |                22.25    |                 0.19937  |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    3.1463   |                   1.60944 |
| A2M:HSPA5     |        -77 |         -77   |    -77      |  -0.877964 |     -0.877964 |   -0.877964 |               3       |                         3 |                27.6667  |                -0.633714 |                     41 |                      1 |                         0 |                        0 |                   0.693147 |                   3.73767  |                    3.35574  |                   1.38629 |
| A2M:IL10      |        -22 |         -22   |    -22      |  -0.831522 |     -0.831522 |   -0.831522 |               2       |                         2 |                13       |                -0.006624 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.63906  |                   1.09861 |
| A2M:IL1B      |        -38 |         -38   |    -38      |  -0.916522 |     -0.916522 |   -0.916522 |               2       |                         2 |                21       |                 0.003668 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    3.09104  |                   1.09861 |
| A2M:IL6       |        -32 |         -32   |    -32      |  -0.897698 |     -0.897698 |   -0.897698 |               2       |                         2 |                18       |                 0.048863 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.94444  |                   1.09861 |
| A2M:KLK3      |        -29 |         -29   |    -29      |  -0.48286  |     -0.48286  |   -0.48286  |               3       |                         3 |                11.6667  |                 0.018472 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.53897  |                   1.38629 |
| A2M:KLK4      |        -28 |         -28   |    -28      |  -0.551449 |     -0.551449 |   -0.551449 |               3       |                         3 |                11.3333  |                -0.004101 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.51231  |                   1.38629 |
| A2M:KLKB1     |        -30 |         -30   |    -30      |  -0.601449 |     -0.601449 |   -0.601449 |               3       |                         3 |                12       |                 0.052281 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.56495  |                   1.38629 |
| A2M:KNG1      |        -35 |         -30   |    -31      |  -0.73286  |     -0.601449 |   -0.628586 |               3       |                         3 |                12.3333  |                -0.052358 |                     22 |                      3 |                         0 |                        0 |                   1.38629  |                   3.13549  |                    2.59027  |                   1.38629 |
| A2M:LRP1      |        -72 |         -64   |    -64      |  -0.856791 |     -0.838334 |   -0.838334 |               3       |                         3 |                23.3333  |                -0.060089 |                     22 |                      2 |                         0 |                        0 |                   1.09861  |                   3.13549  |                    3.19185  |                   1.38629 |
| A2M:MMP2      |        -54 |         -54   |    -54      |  -0.791304 |     -0.791304 |   -0.791304 |               3       |                         3 |                20       |                 0.023152 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    3.04452  |                   1.38629 |
| A2M:MMP3      |        -46 |         -46   |    -46      |  -0.724638 |     -0.724638 |   -0.724638 |               3       |                         3 |                17.3333  |                 0.022503 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.90872  |                   1.38629 |
| A2M:MMP8      |        -19 |         -19   |    -19      |   0.043478 |      0.043478 |    0.043478 |               2       |                         2 |                11.5     |                 0.012169 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.52573  |                   1.09861 |
| A2M:MMP9      |        -56 |         -54   |    -52      |  -0.819876 |     -0.791304 |   -0.778606 |               3       |                         3 |                19.3333  |                -0.005101 |                     24 |                      3 |                         0 |                        0 |                   1.38629  |                   3.21888  |                    3.01226  |                   1.38629 |
| A2M:RAB3IL1   |        -21 |         -21   |    -21      |  -0.706522 |     -0.706522 |   -0.706522 |               2       |                         2 |                12.5     |                -0.000953 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.60269  |                   1.09861 |
| A2M:SERPINA1  |        -85 |         -54.5 |    -55.75   |  -0.737395 |     -0.732602 |   -0.671365 |               3.5     |                         4 |                17.2708  |                 0.004965 |                     22 |                      4 |                         0 |                        0 |                   1.60944  |                   3.13549  |                    2.90531  |                   1.50408 |
| A2M:SERPINF2  |        -21 |         -21   |    -21      |  -0.845411 |     -0.845411 |   -0.845411 |               2       |                         2 |                12.5     |                 0.069865 |                     22 |                      1 |                         0 |                        0 |                   0.693147 |                   3.13549  |                    2.60269  |                   1.09861 |
| A2M:TGFB1     |        -41 |         -41   |    -41      |  -0.925272 |     -0.925272 |   -0.925272 |               2       |                         2 |                22.5     |                -0.029161 |                     23 |                      1 |                         0 |                        0 |                   0.693147 |                   3.17805  |                    3.157    |                   1.09861 |
| A4GALT:GLA    |          2 |           2   |      2      |   1        |      1        |    1        |               2       |                         2 |                 1       |                -0.045523 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.09861 |
| AAAS:AHCTF1   |       -283 |        -276.5 |   -276.5    |   0.396248 |      0.430899 |    0.430899 |              23.5     |                        23 |                13.7772  |                -0.749528 |                     12 |                      2 |                         0 |                        0 |                   1.09861  |                   2.56495  |                    2.69308  |                   3.19867 |
| AAAS:NDC1     |       -283 |        -266   |   -257.1    |  -0.484841 |      0.061309 |    0.07639  |              18.6     |                        10 |                16.1391  |                -0.474216 |                     12 |                     10 |                         0 |                        0 |                   2.3979   |                   2.56495  |                    2.84136  |                   2.97553 |
| AAAS:NUP107   |       -283 |        -266   |   -265.167  |  -0.012666 |      0.124421 |    0.186454 |              20.1667  |                        18 |                15.2878  |                -0.576566 |                     14 |                      6 |                         0 |                        0 |                   1.94591  |                   2.70805  |                    2.79042  |                   3.05243 |
| AAAS:NUP133   |       -283 |        -268.5 |   -266      |   0.101871 |      0.27161  |    0.27766  |              21.25    |                        19 |                14.6123  |                -0.915625 |                     12 |                      4 |                         0 |                        0 |                   1.60944  |                   2.56495  |                    2.74806  |                   3.10234 |
| AAAS:NUP153   |       -283 |        -267   |   -268.143  |  -0.012666 |      0.020747 |    0.090888 |              19       |                        18 |                16.1855  |                -0.463235 |                     25 |                      7 |                         0 |                        0 |                   2.07944  |                   3.2581   |                    2.84407  |                   2.99573 |
| AAAS:NUP155   |       -283 |        -266   |   -257.1    |  -0.484841 |      0.061309 |    0.07639  |              18.6     |                        10 |                16.1391  |                -0.649105 |                     18 |                     10 |                         0 |                        0 |                   2.3979   |                   2.94444  |                    2.84136  |                   2.97553 |
| AAAS:NUP160   |       -283 |        -268.5 |   -266      |   0.101871 |      0.27161  |    0.27766  |              21.25    |                        19 |                14.6123  |                -0.635718 |                     12 |                      4 |                         0 |                        0 |                   1.60944  |                   2.56495  |                    2.74806  |                   3.10234 |
| AAAS:NUP188   |       -283 |        -267   |   -265.667  |  -0.012666 |      0.101871 |    0.138749 |              19.5556  |                        18 |                15.7101  |                -0.27134  |                     12 |                      9 |                         0 |                        0 |                   2.30259  |                   2.56495  |                    2.81601  |                   3.02313 |
| AAAS:NUP205   |       -283 |        -266   |   -257.1    |  -0.484841 |      0.061309 |    0.07639  |              18.6     |                        10 |                16.1391  |                -0.696137 |                     16 |                     10 |                         0 |                        0 |                   2.3979   |                   2.83321  |                    2.84136  |                   2.97553 |


*... [Truncated 79194 standard row items inline] ...*

**Last 40 Structural Rows:**

| pair_key        |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:----------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| YWHAB:ZFP36     |        -27 |         -27   |     -27     |  -0.839286 |     -0.839286 |   -0.839286 |               2       |                         2 |                15.5     |                -0.035077 |                     25 |                      1 |                         0 |                        0 |                   0.693147 |                   3.2581   |                    2.80336  |                   1.09861 |
| YWHAB:ZFP36L1   |        -25 |         -25   |     -25     |  -0.764286 |     -0.764286 |   -0.764286 |               2       |                         2 |                14.5     |                -0.151808 |                     25 |                      1 |                         0 |                        0 |                   0.693147 |                   3.2581   |                    2.74084  |                   1.09861 |
| YWHAE:YWHAG     |       -172 |        -135.5 |    -142.5   |  -0.48596  |     -0.434289 |   -0.404525 |               7.5     |                         7 |                21.0223  |                -0.321776 |                     17 |                      4 |                         0 |                        0 |                   1.60944  |                   2.89037  |                    3.09206  |                   2.14007 |
| YWHAE:YWHAH     |       -172 |        -129   |    -135.4   |  -0.48596  |     -0.412248 |   -0.397964 |               7.2     |                         7 |                20.7845  |                -0.201064 |                     16 |                      5 |                         0 |                        0 |                   1.79176  |                   2.83321  |                    3.0812   |                   2.10413 |
| YWHAE:YWHAQ     |       -172 |        -129   |    -135.4   |  -0.48596  |     -0.412248 |   -0.397964 |               7.2     |                         7 |                20.7845  |                -0.167698 |                     16 |                      5 |                         0 |                        0 |                   1.79176  |                   2.83321  |                    3.0812   |                   2.10413 |
| YWHAE:YWHAZ     |       -172 |        -127   |    -125.429 |  -0.864814 |     -0.456331 |   -0.510571 |               6.28571 |                         3 |                22.7032  |                -0.562597 |                     50 |                      7 |                         0 |                        0 |                   2.07944  |                   3.93183  |                    3.16561  |                   1.98592 |
| YWHAG:YWHAH     |       -172 |        -135.5 |    -142.5   |  -0.48596  |     -0.434289 |   -0.404525 |               7.5     |                         7 |                21.0223  |                -0.105323 |                     17 |                      4 |                         0 |                        0 |                   1.60944  |                   2.89037  |                    3.09206  |                   2.14007 |
| YWHAG:YWHAQ     |       -172 |        -129   |    -129.556 |  -0.708846 |     -0.613943 |   -0.555733 |               6.11111 |                         5 |                23.6988  |                -0.071957 |                     17 |                      9 |                         0 |                        0 |                   2.30259  |                   2.89037  |                    3.20675  |                   1.96166 |
| YWHAG:YWHAZ     |       -172 |        -128   |    -126.3   |  -0.76782  |     -0.634777 |   -0.576942 |               5.9     |                         4 |                23.9539  |                -0.466855 |                     50 |                     10 |                         0 |                        0 |                   2.3979   |                   3.93183  |                    3.21703  |                   1.93152 |
| YWHAH:YWHAQ     |       -172 |        -128   |    -124.5   |  -0.546046 |     -0.434289 |   -0.422644 |               6.83333 |                         5 |                19.9871  |                 0.048755 |                     16 |                      6 |                         0 |                        0 |                   1.94591  |                   2.83321  |                    3.04391  |                   2.05839 |
| YWHAH:YWHAZ     |       -172 |        -128   |    -133.333 |  -0.678929 |     -0.434289 |   -0.444791 |               6.83333 |                         5 |                21.7538  |                -0.346143 |                     50 |                      6 |                         0 |                        0 |                   1.94591  |                   3.93183  |                    3.12473  |                   2.05839 |
| YWHAQ:YWHAZ     |       -172 |        -126   |    -119.154 |  -0.791268 |     -0.613943 |   -0.56446  |               5.53846 |                         4 |                24.1056  |                -0.312777 |                     50 |                     13 |                         0 |                        0 |                   2.63906  |                   3.93183  |                    3.22309  |                   1.8777  |
| YY1:YY2         |        -35 |         -35   |     -35     |   0.017544 |      0.017544 |    0.017544 |               2       |                         2 |                19.5     |                -0.306408 |                     38 |                      1 |                         0 |                        0 |                   0.693147 |                   3.66356  |                    3.02042  |                   1.09861 |
| ZBTB17:ZBTB4    |          0 |           0   |       0     |   0.2      |      0.2      |    0.2      |               2       |                         2 |                 2       |                -0.251046 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                   1.38629  |                    1.09861  |                   1.09861 |
| ZC3H13:ZCCHC4   |         -3 |          -3   |      -3     |   0.070721 |      0.070721 |    0.070721 |               4       |                         4 |                 2.75    |                -0.19615  |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                   1.94591  |                    1.32176  |                   1.60944 |
| ZCRB1:ZMAT5     |      -1513 |       -1513   |   -1513     |   0.022682 |      0.022682 |    0.022682 |              24       |                        24 |                65.0417  |                -0.771819 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    4.19029  |                   3.21888 |
| ZCRB1:ZRSR2     |      -1513 |       -1513   |   -1513     |   0.022682 |      0.022682 |    0.022682 |              24       |                        24 |                65.0417  |                -0.754783 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    4.19029  |                   3.21888 |
| ZEB1:ZEB2       |        -31 |         -31   |     -31     |  -0.369792 |     -0.369792 |   -0.369792 |               3       |                         3 |                12.3333  |                -0.213361 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                   2.30259  |                    2.59027  |                   1.38629 |
| ZER1:ZYG11B     |       -251 |        -251   |    -251     |   0.2725   |      0.2725   |    0.2725   |              17       |                        17 |                16.7647  |                -0.154825 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    2.87721  |                   2.89037 |
| ZFP36L1:ZFP36L2 |         -1 |          -1   |      -1     |   0.2      |      0.2      |    0.2      |               2       |                         2 |                 2.5     |                -0.283718 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.25276  |                   1.09861 |
| ZFYVE16:ZFYVE9  |         -2 |          -2   |      -2     |   0.080357 |      0.080357 |    0.080357 |               3       |                         3 |                 2.66667 |                -0.036917 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                   1.60944  |                    1.29928  |                   1.38629 |
| ZMAT5:ZRSR2     |      -1513 |       -1513   |   -1513     |   0.022682 |      0.022682 |    0.022682 |              24       |                        24 |                65.0417  |                -0.967063 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    4.19029  |                   3.21888 |
| ZMYM2:ZMYM3     |          0 |           0   |       0     |  -0.3      |     -0.3      |   -0.3      |               2       |                         2 |                 2       |                -0.112449 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    1.09861  |                   1.09861 |
| ZMYND8:ZNF592   |        -32 |         -32   |     -32     |  -0.090972 |     -0.090972 |   -0.090972 |               6       |                         6 |                 7.33333 |                -0.204002 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                   1.79176  |                    2.12026  |                   1.94591 |
| ZMYND8:ZNF687   |        -40 |         -36   |     -36     |  -0.231323 |     -0.161148 |   -0.161148 |               6       |                         6 |                 8       |                -0.376565 |                      5 |                      2 |                         0 |                        0 |                   1.09861  |                   1.79176  |                    2.19722  |                   1.94591 |
| ZNF174:ZSCAN1   |          1 |           1   |       1     |   0.5      |      0.5      |    0.5      |               2       |                         2 |                 1.5     |                -0.088947 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.916291 |                   1.09861 |
| ZNF24:ZSCAN1    |          0 |           0   |       0     |   0        |      0        |    0        |               2       |                         2 |                 2       |                -0.075563 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    1.09861  |                   1.09861 |
| ZNF592:ZNF687   |        -32 |         -32   |     -32     |  -0.090972 |     -0.090972 |   -0.090972 |               6       |                         6 |                 7.33333 |                -0.183685 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.12026  |                   1.94591 |
| ZNF787:ZW10     |        -41 |         -41   |     -41     |  -0.128959 |     -0.128959 |   -0.128959 |               3       |                         3 |                15.6667  |                -0.179628 |                      7 |                      1 |                         0 |                        0 |                   0.693147 |                   2.07944  |                    2.81341  |                   1.38629 |
| ZNHIT3:ZNHIT6   |        -26 |         -26   |     -26     |  -0.122466 |     -0.122466 |   -0.122466 |               4       |                         4 |                 8.5     |                -0.662114 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    2.25129  |                   1.60944 |
| ZP1:ZP2         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                -0.008769 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.788457 |                   1.79176 |
| ZP1:ZP3         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                -0.09711  |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.788457 |                   1.79176 |
| ZP1:ZP4         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                -0.016391 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.788457 |                   1.79176 |
| ZP2:ZP3         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                -0.041124 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.788457 |                   1.79176 |
| ZP2:ZP4         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                 0.039595 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.788457 |                   1.79176 |
| ZP3:ZP4         |          4 |           4   |       4     |   0.875    |      0.875    |    0.875    |               5       |                         5 |                 1.2     |                -0.048746 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                   1.09861  |                    0.788457 |                   1.79176 |
| ZW10:ZWILCH     |        -19 |         -11.5 |     -11.5   |  -0.367521 |     -0.084402 |   -0.084402 |               3       |                         3 |                 5.83333 |                -0.27625  |                      7 |                      2 |                         0 |                        0 |                   1.09861  |                   2.07944  |                    1.92181  |                   1.38629 |
| ZW10:ZWINT      |        -19 |         -19   |     -19     |  -0.367521 |     -0.367521 |   -0.367521 |               3       |                         3 |                 8.33333 |                -0.43499  |                     16 |                      1 |                         0 |                        0 |                   0.693147 |                   2.83321  |                    2.23359  |                   1.38629 |
| ZWILCH:ZWINT    |        -19 |         -19   |     -19     |  -0.367521 |     -0.367521 |   -0.367521 |               3       |                         3 |                 8.33333 |                -0.349437 |                     16 |                      1 |                         0 |                        0 |                   0.693147 |                   2.83321  |                    2.23359  |                   1.38629 |
| ZXDA:ZXDC       |          2 |           2   |       2     |   1        |      1        |    1        |               2       |                         2 |                 1       |                 0.007577 |                      1 |                      1 |                         0 |                        0 |                   0.693147 |                   0.693147 |                    0.693147 |                   1.09861 |


---

## File: tcga_bridge_leave_one_family_out.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tcga_bridge_leave_one_family_out.parquet`
- **Matrix Dimensions:** 8 rows × 10 columns

### 1. Data Schema & Quality Audit

| Column Name   | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------|:--------|-----------------:|-------------:|:---------|
| context       | object  |                8 |            0 | 0.00%    |
| omitted_group | object  |                8 |            0 | 0.00%    |
| n_remaining   | int64   |                8 |            0 | 0.00%    |
| meta_mu       | float64 |                8 |            0 | 0.00%    |
| meta_se       | float64 |                8 |            0 | 0.00%    |
| meta_ci_low   | float64 |                8 |            0 | 0.00%    |
| meta_ci_high  | float64 |                8 |            0 | 0.00%    |
| meta_p        | float64 |                8 |            0 | 0.00%    |
| meta_i2       | float64 |                8 |            0 | 0.00%    |
| meta_tau2     | float64 |                8 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|               |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max        |
|:--------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:-----------|
| context       |       8 | 1        | TCGA bridge | 8      | —         | —        | —         | —         | —         | —         | —          |
| omitted_group |       8 | 8        | APC:CTNNB1  | 1      | —         | —        | —         | —         | —         | —         | —          |
| n_remaining   |       8 | —        | —           | —      | 93.625000 | 4.749060 | 89.000000 | 89.000000 | 93.000000 | 97.000000 | 102.000000 |
| meta_mu       |       8 | —        | —           | —      | 0.024428  | 0.009501 | 0.008046  | 0.018724  | 0.027548  | 0.031416  | 0.034618   |
| meta_se       |       8 | —        | —           | —      | 0.049841  | 0.002666 | 0.046423  | 0.047795  | 0.049337  | 0.051887  | 0.053943   |
| meta_ci_low   |       8 | —        | —           | —      | -0.073260 | 0.013424 | -0.097682 | -0.080460 | -0.066853 | -0.063811 | -0.061842  |
| meta_ci_high  |       8 | —        | —           | —      | 0.122116  | 0.007413 | 0.113775  | 0.117049  | 0.121266  | 0.125730  | 0.135842   |
| meta_p        |       8 | —        | —           | —      | 0.625045  | 0.144625 | 0.502665  | 0.509683  | 0.564414  | 0.710837  | 0.881423   |
| meta_i2       |       8 | —        | —           | —      | 0.286989  | 0.045428 | 0.204394  | 0.267953  | 0.284877  | 0.323281  | 0.343718   |
| meta_tau2     |       8 | —        | —           | —      | 0.054912  | 0.012220 | 0.034639  | 0.048253  | 0.053744  | 0.064994  | 0.070224   |

### 3. Categorical Distribution Breakdown

**Column Grouping: `omitted_group`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| APC:CTNNB1       |                1 | 12.5%                   |
| BRAF:MAP2K1      |                1 | 12.5%                   |
| CREBBP:EP300     |                1 | 12.5%                   |
| CTNNB1:TCF7L2    |                1 | 12.5%                   |
| DCP2:XRN1        |                1 | 12.5%                   |
| NRAS:SHOC2       |                1 | 12.5%                   |
| SMARCA2:SMARCA4  |                1 | 12.5%                   |
| SPTLC1:SPTLC3    |                1 | 12.5%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (8 rows total):

| context     | omitted_group   |   n_remaining |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|--------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| TCGA bridge | APC:CTNNB1      |            89 |  0.014653 |  0.052612 |     -0.088466 |       0.117773 | 0.780618 |  0.292584 |    0.05763  |
| TCGA bridge | BRAF:MAP2K1     |            93 |  0.034618 |  0.051645 |     -0.066606 |       0.135842 | 0.502665 |  0.330053 |    0.067933 |
| TCGA bridge | CREBBP:EP300    |            89 |  0.008046 |  0.053943 |     -0.097682 |       0.113775 | 0.881423 |  0.343718 |    0.070224 |
| TCGA bridge | CTNNB1:TCF7L2   |            93 |  0.031207 |  0.04874  |     -0.064323 |       0.126738 | 0.52199  |  0.254544 |    0.045984 |
| TCGA bridge | DCP2:XRN1       |           102 |  0.023889 |  0.046423 |     -0.0671   |       0.114878 | 0.606837 |  0.272422 |    0.049009 |
| TCGA bridge | NRAS:SHOC2      |            97 |  0.020081 |  0.049934 |     -0.077791 |       0.117952 | 0.687577 |  0.321024 |    0.064015 |
| TCGA bridge | SMARCA2:SMARCA4 |            89 |  0.03156  |  0.047874 |     -0.062273 |       0.125393 | 0.509742 |  0.204394 |    0.034639 |
| TCGA bridge | SPTLC1:SPTLC3   |            97 |  0.031368 |  0.047556 |     -0.061842 |       0.124579 | 0.509507 |  0.277171 |    0.049858 |


---

## File: tcga_bridge_meta_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tcga_bridge_meta_summary.parquet`
- **Matrix Dimensions:** 1 rows × 13 columns

### 1. Data Schema & Quality Audit

| Column Name     | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:----------------|:--------|-----------------:|-------------:|:---------|
| context         | object  |                1 |            0 | 0.00%    |
| endpoint_type   | object  |                1 |            0 | 0.00%    |
| effect_col      | object  |                1 |            0 | 0.00%    |
| se_col          | object  |                1 |            0 | 0.00%    |
| n_rows          | int64   |                1 |            0 | 0.00%    |
| n_unique_groups | int64   |                1 |            0 | 0.00%    |
| meta_mu         | float64 |                1 |            0 | 0.00%    |
| meta_se         | float64 |                1 |            0 | 0.00%    |
| meta_ci_low     | float64 |                1 |            0 | 0.00%    |
| meta_ci_high    | float64 |                1 |            0 | 0.00%    |
| meta_p          | float64 |                1 |            0 | 0.00%    |
| meta_i2         | float64 |                1 |            0 | 0.00%    |
| meta_tau2       | float64 |                1 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                 |   count | unique   | top                 | freq   | mean       | std   | min        | 25%        | 50%        | 75%        | max        |
|:----------------|--------:|:---------|:--------------------|:-------|:-----------|:------|:-----------|:-----------|:-----------|:-----------|:-----------|
| context         |       1 | 1        | TCGA bridge         | 1      | —          | —     | —          | —          | —          | —          | —          |
| endpoint_type   |       1 | 1        | continuous          | 1      | —          | —     | —          | —          | —          | —          | —          |
| effect_col      |       1 | 1        | log_hazard_ratio    | 1      | —          | —     | —          | —          | —          | —          | —          |
| se_col          |       1 | 1        | log_hazard_ratio_se | 1      | —          | —     | —          | —          | —          | —          | —          |
| n_rows          |       1 | —        | —                   | —      | 107.000000 | —     | 107.000000 | 107.000000 | 107.000000 | 107.000000 | 107.000000 |
| n_unique_groups |       1 | —        | —                   | —      | 8.000000   | —     | 8.000000   | 8.000000   | 8.000000   | 8.000000   | 8.000000   |
| meta_mu         |       1 | —        | —                   | —      | 0.024628   | —     | 0.024628   | 0.024628   | 0.024628   | 0.024628   | 0.024628   |
| meta_se         |       1 | —        | —                   | —      | 0.046560   | —     | 0.046560   | 0.046560   | 0.046560   | 0.046560   | 0.046560   |
| meta_ci_low     |       1 | —        | —                   | —      | -0.066629  | —     | -0.066629  | -0.066629  | -0.066629  | -0.066629  | -0.066629  |
| meta_ci_high    |       1 | —        | —                   | —      | 0.115885   | —     | 0.115885   | 0.115885   | 0.115885   | 0.115885   | 0.115885   |
| meta_p          |       1 | —        | —                   | —      | 0.596833   | —     | 0.596833   | 0.596833   | 0.596833   | 0.596833   | 0.596833   |
| meta_i2         |       1 | —        | —                   | —      | 0.288638   | —     | 0.288638   | 0.288638   | 0.288638   | 0.288638   | 0.288638   |
| meta_tau2       |       1 | —        | —                   | —      | 0.054438   | —     | 0.054438   | 0.054438   | 0.054438   | 0.054438   | 0.054438   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (1 rows total):

| context     | endpoint_type   | effect_col       | se_col              |   n_rows |   n_unique_groups |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:----------------|:-----------------|:--------------------|---------:|------------------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| TCGA bridge | continuous      | log_hazard_ratio | log_hazard_ratio_se |      107 |                 8 |  0.024628 |   0.04656 |     -0.066629 |       0.115885 | 0.596833 |  0.288638 |    0.054438 |


---

## File: tcga_bridge_tumor_type_meta.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tcga_bridge_tumor_type_meta.parquet`
- **Matrix Dimensions:** 20 rows × 11 columns

### 1. Data Schema & Quality Audit

| Column Name    | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:---------------|:--------|-----------------:|-------------:|:---------|
| context        | object  |               20 |            0 | 0.00%    |
| subgroup_col   | object  |               20 |            0 | 0.00%    |
| subgroup_value | object  |               20 |            0 | 0.00%    |
| n_rows         | int64   |               20 |            0 | 0.00%    |
| meta_mu        | float64 |               20 |            0 | 0.00%    |
| meta_se        | float64 |               20 |            0 | 0.00%    |
| meta_ci_low    | float64 |               20 |            0 | 0.00%    |
| meta_ci_high   | float64 |               20 |            0 | 0.00%    |
| meta_p         | float64 |               20 |            0 | 0.00%    |
| meta_i2        | float64 |               20 |            0 | 0.00%    |
| meta_tau2      | float64 |               20 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max      |
|:---------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:---------|
| context        |      20 | 1        | TCGA bridge | 20     | —         | —        | —         | —         | —         | —         | —        |
| subgroup_col   |      20 | 1        | tumor_type  | 20     | —         | —        | —         | —         | —         | —         | —        |
| subgroup_value |      20 | 20       | BLCA        | 1      | —         | —        | —         | —         | —         | —         | —        |
| n_rows         |      20 | —        | —           | —      | 5.200000  | 2.092593 | 2.000000  | 3.750000  | 5.500000  | 6.500000  | 8.000000 |
| meta_mu        |      20 | —        | —           | —      | 0.042183  | 0.346236 | -0.764275 | -0.112636 | 0.069781  | 0.307751  | 0.603270 |
| meta_se        |      20 | —        | —           | —      | 0.240701  | 0.107827 | 0.079705  | 0.150899  | 0.210034  | 0.318618  | 0.471077 |
| meta_ci_low    |      20 | —        | —           | —      | -0.429591 | 0.411165 | -1.226124 | -0.780136 | -0.278656 | -0.106122 | 0.148371 |
| meta_ci_high   |      20 | —        | —           | —      | 0.513956  | 0.400039 | -0.465957 | 0.218320  | 0.549418  | 0.701371  | 1.221845 |
| meta_p         |      20 | —        | —           | —      | 0.371447  | 0.314219 | 0.000001  | 0.101259  | 0.248767  | 0.650646  | 0.886207 |
| meta_i2        |      20 | —        | —           | —      | 0.072621  | 0.157204 | 0.000000  | 0.000000  | 0.000000  | 0.054678  | 0.618685 |
| meta_tau2      |      20 | —        | —           | —      | 0.025222  | 0.075239 | 0.000000  | 0.000000  | 0.000000  | 0.015981  | 0.337255 |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `meta_p` contains **3** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| context     | subgroup_col   | subgroup_value   |   n_rows |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:---------------|:-----------------|---------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| TCGA bridge | tumor_type     | UCEC             |        8 | -0.764275 |  0.152203 |     -1.06259  |      -0.465957 | 1e-06    |         0 |           0 |
| TCGA bridge | tumor_type     | LUAD             |        6 |  0.378566 |  0.117446 |      0.148371 |       0.60876  | 0.001267 |         0 |           0 |
| TCGA bridge | tumor_type     | BRCA             |        6 |  0.602581 |  0.30703  |      0.000802 |       1.20436  | 0.049691 |         0 |           0 |


### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (20 rows total):

| context     | subgroup_col   | subgroup_value   |   n_rows |   meta_mu |   meta_se |   meta_ci_low |   meta_ci_high |   meta_p |   meta_i2 |   meta_tau2 |
|:------------|:---------------|:-----------------|---------:|----------:|----------:|--------------:|---------------:|---------:|----------:|------------:|
| TCGA bridge | tumor_type     | BLCA             |        8 | -0.159205 |  0.144447 |     -0.442322 |       0.123912 | 0.270391 |  0.089985 |    0.015578 |
| TCGA bridge | tumor_type     | BRCA             |        6 |  0.602581 |  0.30703  |      0.000802 |       1.20436  | 0.049691 |  0        |    0        |
| TCGA bridge | tumor_type     | CESC             |        6 |  0.314984 |  0.219932 |     -0.116082 |       0.74605  | 0.15209  |  0        |    0        |
| TCGA bridge | tumor_type     | COAD             |        8 | -0.02874  |  0.123987 |     -0.271755 |       0.214275 | 0.816697 |  0        |    0        |
| TCGA bridge | tumor_type     | ESCA             |        3 | -0.097114 |  0.299587 |     -0.684304 |       0.490076 | 0.745818 |  0.023559 |    0.00681  |
| TCGA bridge | tumor_type     | GBM              |        4 |  0.076115 |  0.184527 |     -0.285557 |       0.437788 | 0.67998  |  0        |    0        |
| TCGA bridge | tumor_type     | HNSC             |        6 |  0.091464 |  0.163835 |     -0.229652 |       0.41258  | 0.57666  |  0        |    0        |
| TCGA bridge | tumor_type     | KIRC             |        3 | -0.302813 |  0.471077 |     -1.22612  |       0.620499 | 0.520348 |  0.045007 |    0.034567 |
| TCGA bridge | tumor_type     | KIRP             |        3 |  0.174924 |  0.374983 |     -0.560042 |       0.90989  | 0.640868 |  0        |    0        |
| TCGA bridge | tumor_type     | LIHC             |        5 |  0.177526 |  0.146988 |     -0.110572 |       0.465623 | 0.227143 |  0        |    0        |
| TCGA bridge | tumor_type     | LUAD             |        6 |  0.378566 |  0.117446 |      0.148371 |       0.60876  | 0.001267 |  0        |    0        |
| TCGA bridge | tumor_type     | LUSC             |        8 |  0.305341 |  0.194458 |     -0.075797 |       0.686478 | 0.116365 |  0.2257   |    0.065393 |
| TCGA bridge | tumor_type     | OV               |        4 | -0.066863 |  0.374312 |     -0.800515 |       0.666789 | 0.858229 |  0.618685 |    0.337255 |
| TCGA bridge | tumor_type     | PRAD             |        4 |  0.60327  |  0.315599 |     -0.015304 |       1.22185  | 0.055939 |  0.014485 |    0.006667 |
| TCGA bridge | tumor_type     | READ             |        4 | -0.428037 |  0.327674 |     -1.07028  |       0.214203 | 0.191453 |  0        |    0        |
| TCGA bridge | tumor_type     | SARC             |        2 | -0.053102 |  0.371071 |     -0.780402 |       0.674198 | 0.886207 |  0        |    0        |
| TCGA bridge | tumor_type     | SKCM             |        8 |  0.063447 |  0.079705 |     -0.092774 |       0.219668 | 0.426019 |  0.351314 |    0.01719  |
| TCGA bridge | tumor_type     | STAD             |        6 | -0.38778  |  0.200136 |     -0.780047 |       0.004487 | 0.052674 |  0.083692 |    0.020985 |
| TCGA bridge | tumor_type     | THCA             |        2 |  0.343366 |  0.24502  |     -0.136874 |       0.823606 | 0.161101 |  0        |    0        |
| TCGA bridge | tumor_type     | UCEC             |        8 | -0.764275 |  0.152203 |     -1.06259  |      -0.465957 | 1e-06    |  0        |    0        |


---

## File: tcga_schoenfeld_diagnostics.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tcga_schoenfeld_diagnostics.parquet`
- **Matrix Dimensions:** 96 rows × 9 columns

### 1. Data Schema & Quality Audit

| Column Name        | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-------------------|:--------|-----------------:|-------------:|:---------|
| histology          | object  |               96 |            0 | 0.00%    |
| mutation_gene      | object  |               96 |            0 | 0.00%    |
| partner_gene       | object  |               96 |            0 | 0.00%    |
| coefficient        | object  |               96 |            0 | 0.00%    |
| schoenfeld_rho     | float64 |               56 |           40 | 41.67%   |
| schoenfeld_p_value | float64 |               56 |           40 | 41.67%   |
| n_event_rows       | int64   |               96 |            0 | 0.00%    |
| ph_global_p_value  | float64 |               56 |           40 | 41.67%   |
| ph_flag            | bool    |               96 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                    |   count | unique   | top    | freq   | mean       | std        | min       | 25%      | 50%        | 75%        | max        |
|:-------------------|--------:|:---------|:-------|:-------|:-----------|:-----------|:----------|:---------|:-----------|:-----------|:-----------|
| histology          |      96 | 2        | LUAD   | 56     | —          | —          | —         | —        | —          | —          | —          |
| mutation_gene      |      96 | 7        | APC    | 16     | —          | —          | —         | —        | —          | —          | —          |
| partner_gene       |      96 | 7        | CTNNB1 | 16     | —          | —          | —         | —        | —          | —          | —          |
| coefficient        |      96 | 14       | age    | 12     | —          | —          | —         | —        | —          | —          | —          |
| schoenfeld_rho     |      56 | —        | —      | —      | 0.167150   | 0.219814   | -0.557644 | 0.031554 | 0.159464   | 0.352059   | 0.533688   |
| schoenfeld_p_value |      56 | —        | —      | —      | 0.228346   | 0.355232   | 0.000000  | 0.000000 | 0.020434   | 0.188744   | 0.994020   |
| n_event_rows       |      96 | —        | —      | —      | 119.000000 | 101.101304 | 0.000000  | 0.000000 | 204.000000 | 204.000000 | 204.000000 |
| ph_global_p_value  |      56 | —        | —      | —      | 0.000000   | 0.000000   | 0.000000  | 0.000000 | 0.000000   | 0.000000   | 0.000000   |
| ph_flag            |      96 | 2        | True   | 56     | —          | —          | —         | —        | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `histology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| LUAD             |               56 | 58.33%                  |
| BRCA             |               40 | 41.67%                  |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| APC              |               16 | 16.67%                  |
| BRAF             |               16 | 16.67%                  |
| CREBBP           |               16 | 16.67%                  |
| IFT122           |               16 | 16.67%                  |
| SMARCA2          |               16 | 16.67%                  |
| AP3B2            |                8 | 8.33%                   |
| CTNNB1           |                8 | 8.33%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CTNNB1           |               16 | 16.67%                  |
| MAP2K1           |               16 | 16.67%                  |
| EP300            |               16 | 16.67%                  |
| WDR35            |               16 | 16.67%                  |
| SMARCA4          |               16 | 16.67%                  |
| AP3M2            |                8 | 8.33%                   |
| TCF7L2           |                8 | 8.33%                   |

**Column Grouping: `coefficient`**

| Value Category       |   Absolute Count | Percentage Proportion   |
|:---------------------|-----------------:|:------------------------|
| age                  |               12 | 12.5%                   |
| gender_MALE          |               12 | 12.5%                   |
| simplified_stage_II  |               12 | 12.5%                   |
| simplified_stage_III |               12 | 12.5%                   |
| simplified_stage_IV  |               12 | 12.5%                   |
| KRAS_mutation        |               12 | 12.5%                   |
| TP53_mutation        |               12 | 12.5%                   |
| APC_mutation         |                2 | 2.08%                   |
| BRAF_mutation        |                2 | 2.08%                   |
| CREBBP_mutation      |                2 | 2.08%                   |
| IFT122_mutation      |                2 | 2.08%                   |
| SMARCA2_mutation     |                2 | 2.08%                   |
| AP3B2_mutation       |                1 | 1.04%                   |
| CTNNB1_mutation      |                1 | 1.04%                   |

**Column Grouping: `ph_flag`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| True             |               56 | 58.33%                  |
| False            |               40 | 41.67%                  |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `schoenfeld_p_value` contains **33** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| histology   | mutation_gene   | partner_gene   | coefficient         |   schoenfeld_rho |   schoenfeld_p_value |   n_event_rows |   ph_global_p_value | ph_flag   |
|:------------|:----------------|:---------------|:--------------------|-----------------:|---------------------:|---------------:|--------------------:|:----------|
| LUAD        | SMARCA2         | SMARCA4        | SMARCA2_mutation    |        -0.557644 |                    0 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | simplified_stage_IV |         0.533688 |                    0 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | simplified_stage_IV |         0.518498 |                    0 |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | simplified_stage_IV |         0.513995 |                    0 |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | simplified_stage_IV |         0.513896 |                    0 |            204 |                   0 | True      |

- 💡 **Significance Hit:** Column `ph_global_p_value` contains **56** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| histology   | mutation_gene   | partner_gene   | coefficient          |   schoenfeld_rho |   schoenfeld_p_value |   n_event_rows |   ph_global_p_value | ph_flag   |
|:------------|:----------------|:---------------|:---------------------|-----------------:|---------------------:|---------------:|--------------------:|:----------|
| LUAD        | SMARCA2         | SMARCA4        | SMARCA2_mutation     |        -0.557644 |             0        |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | age                  |         0.099425 |             0.157112 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | gender_MALE          |        -0.007728 |             0.912649 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | simplified_stage_II  |         0.159326 |             0.022834 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | simplified_stage_III |         0.008097 |             0.908488 |            204 |                   0 | True      |

- 📈 **Peak Performance Asset (`schoenfeld_rho`):** Maximal value observed is `0.53369`.

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (96 rows total):

| histology   | mutation_gene   | partner_gene   | coefficient          |   schoenfeld_rho |   schoenfeld_p_value |   n_event_rows |   ph_global_p_value | ph_flag   |
|:------------|:----------------|:---------------|:---------------------|-----------------:|---------------------:|---------------:|--------------------:|:----------|
| LUAD        | AP3B2           | AP3M2          | AP3B2_mutation       |        -0.095822 |             0.172777 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | age                  |         0.103421 |             0.141013 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | gender_MALE          |        -0.009108 |             0.897126 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | simplified_stage_II  |         0.147714 |             0.034997 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | simplified_stage_III |         0.035952 |             0.609698 |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | simplified_stage_IV  |         0.533688 |             0        |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | KRAS_mutation        |         0.395054 |             0        |            204 |                   0 | True      |
| LUAD        | AP3B2           | AP3M2          | TP53_mutation        |         0.174698 |             0.012451 |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | APC_mutation         |         0.339137 |             1e-06    |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | age                  |         0.103523 |             0.140621 |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | gender_MALE          |         0.000528 |             0.99402  |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | simplified_stage_II  |         0.164393 |             0.018794 |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | simplified_stage_III |         0.052652 |             0.454509 |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | simplified_stage_IV  |         0.513995 |             0        |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | KRAS_mutation        |         0.396051 |             0        |            204 |                   0 | True      |
| LUAD        | APC             | CTNNB1         | TP53_mutation        |         0.181344 |             0.009439 |            204 |                   0 | True      |
| BRCA        | APC             | CTNNB1         | APC_mutation         |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | age                  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | gender_MALE          |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | simplified_stage_II  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | simplified_stage_III |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | simplified_stage_IV  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | KRAS_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | APC             | CTNNB1         | TP53_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| LUAD        | BRAF            | MAP2K1         | BRAF_mutation        |        -0.513431 |             0        |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | age                  |         0.10252  |             0.144528 |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | gender_MALE          |        -0.015863 |             0.821834 |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | simplified_stage_II  |         0.159603 |             0.022595 |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | simplified_stage_III |         0.083223 |             0.236645 |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | simplified_stage_IV  |         0.470784 |             0        |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | KRAS_mutation        |         0.391857 |             0        |            204 |                   0 | True      |
| LUAD        | BRAF            | MAP2K1         | TP53_mutation        |         0.209879 |             0.002588 |            204 |                   0 | True      |
| BRCA        | BRAF            | MAP2K1         | BRAF_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | age                  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | gender_MALE          |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | simplified_stage_II  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | simplified_stage_III |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | simplified_stage_IV  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | KRAS_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | BRAF            | MAP2K1         | TP53_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| LUAD        | CREBBP          | EP300          | CREBBP_mutation      |         0.12115  |             0.084329 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | age                  |         0.099927 |             0.155018 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | gender_MALE          |        -0.005478 |             0.938016 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | simplified_stage_II  |         0.160967 |             0.021451 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | simplified_stage_III |         0.009413 |             0.893697 |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | simplified_stage_IV  |         0.518498 |             0        |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | KRAS_mutation        |         0.390823 |             0        |            204 |                   0 | True      |
| LUAD        | CREBBP          | EP300          | TP53_mutation        |         0.18746  |             0.007256 |            204 |                   0 | True      |
| BRCA        | CREBBP          | EP300          | CREBBP_mutation      |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | age                  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | gender_MALE          |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | simplified_stage_II  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | simplified_stage_III |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | simplified_stage_IV  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | KRAS_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | CREBBP          | EP300          | TP53_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| LUAD        | CTNNB1          | TCF7L2         | CTNNB1_mutation      |         0.163555 |             0.019416 |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | age                  |         0.100982 |             0.150681 |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | gender_MALE          |        -0.008015 |             0.909411 |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | simplified_stage_II  |         0.143209 |             0.041012 |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | simplified_stage_III |         0.018361 |             0.794355 |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | simplified_stage_IV  |         0.504851 |             0        |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | KRAS_mutation        |         0.39404  |             0        |            204 |                   0 | True      |
| LUAD        | CTNNB1          | TCF7L2         | TP53_mutation        |         0.18729  |             0.00731  |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | IFT122_mutation      |         0.264924 |             0.000129 |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | age                  |         0.099395 |             0.157237 |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | gender_MALE          |        -0.007346 |             0.916947 |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | simplified_stage_II  |         0.223828 |             0.00129  |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | simplified_stage_III |        -0.003476 |             0.960648 |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | simplified_stage_IV  |         0.513896 |             0        |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | KRAS_mutation        |         0.399811 |             0        |            204 |                   0 | True      |
| LUAD        | IFT122          | WDR35          | TP53_mutation        |         0.182236 |             0.009088 |            204 |                   0 | True      |
| BRCA        | IFT122          | WDR35          | IFT122_mutation      |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | age                  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | gender_MALE          |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | simplified_stage_II  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | simplified_stage_III |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | simplified_stage_IV  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | KRAS_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | IFT122          | WDR35          | TP53_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| LUAD        | SMARCA2         | SMARCA4        | SMARCA2_mutation     |        -0.557644 |             0        |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | age                  |         0.099425 |             0.157112 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | gender_MALE          |        -0.007728 |             0.912649 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | simplified_stage_II  |         0.159326 |             0.022834 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | simplified_stage_III |         0.008097 |             0.908488 |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | simplified_stage_IV  |         0.4854   |             0        |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | KRAS_mutation        |         0.393117 |             0        |            204 |                   0 | True      |
| LUAD        | SMARCA2         | SMARCA4        | TP53_mutation        |         0.194292 |             0.00536  |            204 |                   0 | True      |
| BRCA        | SMARCA2         | SMARCA4        | SMARCA2_mutation     |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | age                  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | gender_MALE          |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | simplified_stage_II  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | simplified_stage_III |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | simplified_stage_IV  |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | KRAS_mutation        |       nan        |           nan        |              0 |                 nan | False     |
| BRCA        | SMARCA2         | SMARCA4        | TP53_mutation        |       nan        |           nan        |              0 |                 nan | False     |


---

## File: tcga_survival_validation.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tcga_survival_validation.parquet`
- **Matrix Dimensions:** 12 rows × 23 columns

### 1. Data Schema & Quality Audit

| Column Name              | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-------------------------|:--------|-----------------:|-------------:|:---------|
| histology                | object  |               12 |            0 | 0.00%    |
| mutation_gene            | object  |               12 |            0 | 0.00%    |
| partner_gene             | object  |               12 |            0 | 0.00%    |
| mutation_col             | object  |               12 |            0 | 0.00%    |
| partner_col              | object  |                8 |            4 | 33.33%   |
| time_col                 | object  |               12 |            0 | 0.00%    |
| event_col                | object  |               12 |            0 | 0.00%    |
| p_value                  | float64 |                7 |            5 | 41.67%   |
| hazard_ratio             | float64 |                7 |            5 | 41.67%   |
| coef                     | float64 |                7 |            5 | 41.67%   |
| coef_se                  | float64 |                7 |            5 | 41.67%   |
| log_hazard_ratio         | float64 |                7 |            5 | 41.67%   |
| log_hazard_ratio_se      | float64 |                7 |            5 | 41.67%   |
| log_hazard_ratio_ci_low  | float64 |                7 |            5 | 41.67%   |
| log_hazard_ratio_ci_high | float64 |                7 |            5 | 41.67%   |
| hazard_ratio_ci_low      | float64 |                7 |            5 | 41.67%   |
| hazard_ratio_ci_high     | float64 |                7 |            5 | 41.67%   |
| n_total                  | int64   |               12 |            0 | 0.00%    |
| n_events                 | int64   |               12 |            0 | 0.00%    |
| n_mutant                 | int64   |               12 |            0 | 0.00%    |
| n_wildtype               | int64   |               12 |            0 | 0.00%    |
| covariates_used          | object  |               12 |            0 | 0.00%    |
| covariates_dropped       | object  |               12 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                          |   count | unique   | top                                                     | freq   | mean       | std        | min        | 25%        | 50%        | 75%         | max         |
|:-------------------------|--------:|:---------|:--------------------------------------------------------|:-------|:-----------|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| histology                |      12 | 2        | LUAD                                                    | 7      | —          | —          | —          | —          | —          | —           | —           |
| mutation_gene            |      12 | 7        | APC                                                     | 2      | —          | —          | —          | —          | —          | —           | —           |
| partner_gene             |      12 | 7        | CTNNB1                                                  | 2      | —          | —          | —          | —          | —          | —           | —           |
| mutation_col             |      12 | 7        | APC_mutation                                            | 2      | —          | —          | —          | —          | —          | —           | —           |
| partner_col              |       8 | 5        | CTNNB1_expression                                       | 2      | —          | —          | —          | —          | —          | —           | —           |
| time_col                 |      12 | 1        | PFI.time                                                | 12     | —          | —          | —          | —          | —          | —           | —           |
| event_col                |      12 | 1        | PFI                                                     | 12     | —          | —          | —          | —          | —          | —           | —           |
| p_value                  |       7 | —        | —                                                       | —      | 0.544758   | 0.231298   | 0.208494   | 0.400518   | 0.586483   | 0.649708    | 0.917876    |
| hazard_ratio             |       7 | —        | —                                                       | —      | 1.058117   | 0.286346   | 0.532197   | 0.938254   | 1.142333   | 1.262034    | 1.331714    |
| coef                     |       7 | —        | —                                                       | —      | 0.016404   | 0.325950   | -0.630741  | -0.069501  | 0.133073   | 0.232515    | 0.286467    |
| coef_se                  |       7 | —        | —                                                       | —      | 0.385255   | 0.154779   | 0.227767   | 0.321199   | 0.352481   | 0.379145    | 0.715849    |
| log_hazard_ratio         |       7 | —        | —                                                       | —      | 0.016404   | 0.325950   | -0.630741  | -0.069501  | 0.133073   | 0.232515    | 0.286467    |
| log_hazard_ratio_se      |       7 | —        | —                                                       | —      | 0.385255   | 0.154779   | 0.227767   | 0.321199   | 0.352481   | 0.379145    | 0.715849    |
| log_hazard_ratio_ci_low  |       7 | —        | —                                                       | —      | -0.738696  | 0.613656   | -2.033805  | -0.776045  | -0.551991  | -0.436515   | -0.159956   |
| log_hazard_ratio_ci_high |       7 | —        | —                                                       | —      | 0.771503   | 0.141339   | 0.513865   | 0.746555   | 0.772323   | 0.822586    | 0.976055    |
| hazard_ratio_ci_low      |       7 | —        | —                                                       | —      | 0.539853   | 0.227064   | 0.130837   | 0.462164   | 0.575802   | 0.647910    | 0.852181    |
| hazard_ratio_ci_high     |       7 | —        | —                                                       | —      | 2.181222   | 0.299788   | 1.671740   | 2.109916   | 2.164789   | 2.279113    | 2.653965    |
| n_total                  |      12 | —        | —                                                       | —      | 744.666667 | 298.658617 | 503.000000 | 503.000000 | 503.000000 | 1083.000000 | 1083.000000 |
| n_events                 |      12 | —        | —                                                       | —      | 177.333333 | 32.955434  | 140.000000 | 140.000000 | 204.000000 | 204.000000  | 204.000000  |
| n_mutant                 |      12 | —        | —                                                       | —      | 18.083333  | 8.948929   | 8.000000   | 12.000000  | 17.000000  | 23.000000   | 39.000000   |
| n_wildtype               |      12 | —        | —                                                       | —      | 726.583333 | 302.722633 | 464.000000 | 481.500000 | 492.000000 | 1068.250000 | 1075.000000 |
| covariates_used          |      12 | 1        | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | 12     | —          | —          | —          | —          | —          | —           | —           |
| covariates_dropped       |      12 | 1        | log_TMB                                                 | 12     | —          | —          | —          | —          | —          | —           | —           |

### 3. Categorical Distribution Breakdown

**Column Grouping: `histology`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| LUAD             |                7 | 58.33%                  |
| BRCA             |                5 | 41.67%                  |

**Column Grouping: `mutation_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| APC              |                2 | 16.67%                  |
| BRAF             |                2 | 16.67%                  |
| CREBBP           |                2 | 16.67%                  |
| IFT122           |                2 | 16.67%                  |
| SMARCA2          |                2 | 16.67%                  |
| AP3B2            |                1 | 8.33%                   |
| CTNNB1           |                1 | 8.33%                   |

**Column Grouping: `partner_gene`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| CTNNB1           |                2 | 16.67%                  |
| MAP2K1           |                2 | 16.67%                  |
| EP300            |                2 | 16.67%                  |
| WDR35            |                2 | 16.67%                  |
| SMARCA4          |                2 | 16.67%                  |
| AP3M2            |                1 | 8.33%                   |
| TCF7L2           |                1 | 8.33%                   |

**Column Grouping: `mutation_col`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| APC_mutation     |                2 | 16.67%                  |
| BRAF_mutation    |                2 | 16.67%                  |
| CREBBP_mutation  |                2 | 16.67%                  |
| IFT122_mutation  |                2 | 16.67%                  |
| SMARCA2_mutation |                2 | 16.67%                  |
| AP3B2_mutation   |                1 | 8.33%                   |
| CTNNB1_mutation  |                1 | 8.33%                   |

**Column Grouping: `partner_col`**

| Value Category    |   Absolute Count | Percentage Proportion   |
|:------------------|-----------------:|:------------------------|
|                   |                4 | 33.33%                  |
| CTNNB1_expression |                2 | 16.67%                  |
| MAP2K1_expression |                2 | 16.67%                  |
| WDR35_expression  |                2 | 16.67%                  |
| AP3M2_expression  |                1 | 8.33%                   |
| TCF7L2_expression |                1 | 8.33%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (12 rows total):

| histology   | mutation_gene   | partner_gene   | mutation_col     | partner_col       | time_col   | event_col   |    p_value |   hazard_ratio |       coef |    coef_se |   log_hazard_ratio |   log_hazard_ratio_se |   log_hazard_ratio_ci_low |   log_hazard_ratio_ci_high |   hazard_ratio_ci_low |   hazard_ratio_ci_high |   n_total |   n_events |   n_mutant |   n_wildtype | covariates_used                                         | covariates_dropped   |
|:------------|:----------------|:---------------|:-----------------|:------------------|:-----------|:------------|-----------:|---------------:|-----------:|-----------:|-------------------:|----------------------:|--------------------------:|---------------------------:|----------------------:|-----------------------:|----------:|-----------:|-----------:|-------------:|:--------------------------------------------------------|:---------------------|
| LUAD        | AP3B2           | AP3M2          | AP3B2_mutation   | AP3M2_expression  | PFI.time   | PFI         |   0.586483 |       1.23619  |   0.212032 |   0.389808 |           0.212032 |              0.389808 |                 -0.551991 |                   0.976055 |              0.575802 |                2.65396 |       503 |        204 |         13 |          490 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | APC             | CTNNB1         | APC_mutation     | CTNNB1_expression | PFI.time   | PFI         |   0.422777 |       1.28788  |   0.252998 |   0.315611 |           0.252998 |              0.315611 |                 -0.3656   |                   0.871596 |              0.69378  |                2.39072 |       503 |        204 |         25 |          478 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| BRCA        | APC             | CTNNB1         | APC_mutation     | CTNNB1_expression | PFI.time   | PFI         | nan        |     nan        | nan        | nan        |         nan        |            nan        |                nan        |                 nan        |            nan        |              nan       |      1083 |        140 |         15 |         1068 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | BRAF            | MAP2K1         | BRAF_mutation    | MAP2K1_expression | PFI.time   | PFI         |   0.208494 |       1.33171  |   0.286467 |   0.227767 |           0.286467 |              0.227767 |                 -0.159956 |                   0.73289  |              0.852181 |                2.08109 |       503 |        204 |         39 |          464 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| BRCA        | BRAF            | MAP2K1         | BRAF_mutation    | MAP2K1_expression | PFI.time   | PFI         | nan        |     nan        | nan        | nan        |         nan        |            nan        |                nan        |                 nan        |            nan        |              nan       |      1083 |        140 |          8 |         1075 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | CREBBP          | EP300          | CREBBP_mutation  |                   | PFI.time   | PFI         |   0.615565 |       0.837783 |  -0.176997 |   0.352481 |          -0.176997 |              0.352481 |                 -0.867858 |                   0.513865 |              0.41985  |                1.67174 |       503 |        204 |         23 |          480 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| BRCA        | CREBBP          | EP300          | CREBBP_mutation  |                   | PFI.time   | PFI         | nan        |     nan        | nan        | nan        |         nan        |            nan        |                nan        |                 nan        |            nan        |              nan       |      1083 |        140 |         23 |         1060 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | CTNNB1          | TCF7L2         | CTNNB1_mutation  | TCF7L2_expression | PFI.time   | PFI         |   0.917876 |       1.03872  |   0.037994 |   0.368482 |           0.037994 |              0.368482 |                 -0.684231 |                   0.760219 |              0.504478 |                2.13875 |       503 |        204 |         19 |          484 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | IFT122          | WDR35          | IFT122_mutation  | WDR35_expression  | PFI.time   | PFI         |   0.378259 |       0.532197 |  -0.630741 |   0.715849 |          -0.630741 |              0.715849 |                 -2.03381  |                   0.772323 |              0.130837 |                2.16479 |       503 |        204 |          9 |          494 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| BRCA        | IFT122          | WDR35          | IFT122_mutation  | WDR35_expression  | PFI.time   | PFI         | nan        |     nan        | nan        | nan        |         nan        |            nan        |                nan        |                 nan        |            nan        |              nan       |      1083 |        140 |          8 |         1075 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| LUAD        | SMARCA2         | SMARCA4        | SMARCA2_mutation |                   | PFI.time   | PFI         |   0.683851 |       1.14233  |   0.133073 |   0.326787 |           0.133073 |              0.326787 |                 -0.507431 |                   0.773576 |              0.60204  |                2.1675  |       503 |        204 |         21 |          482 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |
| BRCA        | SMARCA2         | SMARCA4        | SMARCA2_mutation |                   | PFI.time   | PFI         | nan        |     nan        | nan        | nan        |         nan        |            nan        |                nan        |                 nan        |            nan        |              nan       |      1083 |        140 |         14 |         1069 | age;gender;simplified_stage;KRAS_mutation;TP53_mutation | log_TMB              |


---

## File: tight_null_framework_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tight_null_framework_summary.parquet`
- **Matrix Dimensions:** 15 rows × 15 columns

### 1. Data Schema & Quality Audit

| Column Name         | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------|:--------|-----------------:|-------------:|:---------|
| metric              | object  |               15 |            0 | 0.00%    |
| observed_count      | int64   |               15 |            0 | 0.00%    |
| observed_value      | float64 |               15 |            0 | 0.00%    |
| null_mean           | float64 |               15 |            0 | 0.00%    |
| iter_null_std       | float64 |               15 |            0 | 0.00%    |
| iter_null_min       | float64 |               15 |            0 | 0.00%    |
| iter_null_max       | float64 |               15 |            0 | 0.00%    |
| empirical_p_less    | float64 |               14 |            1 | 6.67%    |
| n_permutations      | int64   |               15 |            0 | 0.00%    |
| null_type           | object  |               15 |            0 | 0.00%    |
| description         | object  |               15 |            0 | 0.00%    |
| frozen_primary      | object  |               14 |            1 | 6.67%    |
| testing_tier        | object  |                6 |            9 | 60.00%   |
| holm_adjusted_p     | float64 |                6 |            9 | 60.00%   |
| hierarchical_reject | object  |                6 |            9 | 60.00%   |

### 2. Full Descriptive Summary Statistics

|                     |   count | unique   | top                                                                                                                                       | freq   | mean        | std         | min          | 25%        | 50%        | 75%         | max          |
|:--------------------|--------:|:---------|:------------------------------------------------------------------------------------------------------------------------------------------|:-------|:------------|:------------|:-------------|:-----------|:-----------|:------------|:-------------|
| metric              |      15 | 8        | min_hlrc                                                                                                                                  | 8      | —           | —           | —            | —          | —          | —           | —            |
| observed_count      |      15 | —        | —                                                                                                                                         | —      | 11.000000   | 0.000000    | 11.000000    | 11.000000  | 11.000000  | 11.000000   | 11.000000    |
| observed_value      |      15 | —        | —                                                                                                                                         | —      | -74.758443  | 203.160486  | -732.363636  | -0.567756  | -0.567756  | -0.497860   | 91.909091    |
| null_mean           |      15 | —        | —                                                                                                                                         | —      | -103.485659 | 232.408085  | -673.427364  | -0.490867  | -0.400373  | -0.284712   | 73.200909    |
| iter_null_std       |      15 | —        | —                                                                                                                                         | —      | 34.623844   | 69.888885   | 0.000000     | 0.056108   | 0.068427   | 7.079709    | 197.642064   |
| iter_null_min       |      15 | —        | —                                                                                                                                         | —      | -203.023930 | 438.564576  | -1313.727273 | -0.694159  | -0.629159  | -0.496516   | 44.818182    |
| iter_null_max       |      15 | —        | —                                                                                                                                         | —      | -31.657041  | 93.745873   | -257.000000  | -0.324985  | -0.212698  | 0.041171    | 115.090909   |
| empirical_p_less    |      14 | —        | —                                                                                                                                         | —      | 0.285492    | 0.381160    | 0.005994     | 0.025766   | 0.080888   | 0.429271    | 0.983017     |
| n_permutations      |      15 | —        | —                                                                                                                                         | —      | 1300.066667 | 2426.010849 | 1.000000     | 500.000000 | 500.000000 | 1000.000000 | 10000.000000 |
| null_type           |      15 | 10       | feature_matched                                                                                                                           | 6      | —           | —           | —            | —          | —          | —           | —            |
| description         |      15 | 10       | Matched on log_pair_hyperedge_count, log_pair_max_node_degree, log_mean_edge_node_degree, mean_pair_essentiality, log_mean_hyperedge_size | 6      | —           | —           | —            | —          | —          | —           | —            |
| frozen_primary      |      14 | 2        | False                                                                                                                                     | 13     | —           | —           | —            | —          | —          | —           | —            |
| testing_tier        |       6 | 2        | secondary                                                                                                                                 | 5      | —           | —           | —            | —          | —          | —           | —            |
| holm_adjusted_p     |       6 | —        | —                                                                                                                                         | —      | 0.621917    | 0.430635    | 0.037196     | 0.320929   | 0.699800   | 1.000000    | 1.000000     |
| hierarchical_reject |       6 | 2        | False                                                                                                                                     | 5      | —           | —           | —            | —          | —          | —           | —            |

### 3. Categorical Distribution Breakdown

**Column Grouping: `metric`**

| Value Category       |   Absolute Count | Percentage Proportion   |
|:---------------------|-----------------:|:------------------------|
| min_hlrc             |                8 | 53.33%                  |
| median_hlrc          |                1 | 6.67%                   |
| mean_hlrc            |                1 | 6.67%                   |
| min_hfrc             |                1 | 6.67%                   |
| median_hfrc          |                1 | 6.67%                   |
| mean_hfrc            |                1 | 6.67%                   |
| mean_hyperedge_size  |                1 | 6.67%                   |
| pair_max_node_degree |                1 | 6.67%                   |

**Column Grouping: `null_type`**

| Value Category                          |   Absolute Count | Percentage Proportion   |
|:----------------------------------------|-----------------:|:------------------------|
| feature_matched                         |                6 | 40.0%                   |
| random_matching                         |                1 | 6.67%                   |
| ablation_size                           |                1 | 6.67%                   |
| ablation_degree                         |                1 | 6.67%                   |
| ablation_drop_log_pair_hyperedge_count  |                1 | 6.67%                   |
| ablation_drop_log_pair_max_node_degree  |                1 | 6.67%                   |
| ablation_drop_log_mean_edge_node_degree |                1 | 6.67%                   |
| ablation_drop_mean_pair_essentiality    |                1 | 6.67%                   |
| ablation_drop_log_mean_hyperedge_size   |                1 | 6.67%                   |
| bipartite_shuffle                       |                1 | 6.67%                   |

**Column Grouping: `description`**

| Value Category                                                                                                                            |   Absolute Count | Percentage Proportion   |
|:------------------------------------------------------------------------------------------------------------------------------------------|-----------------:|:------------------------|
| Matched on log_pair_hyperedge_count, log_pair_max_node_degree, log_mean_edge_node_degree, mean_pair_essentiality, log_mean_hyperedge_size |                6 | 40.0%                   |
| Uniform random sampling from background                                                                                                   |                1 | 6.67%                   |
| Testing if size alone explains overlap                                                                                                    |                1 | 6.67%                   |
| Testing if degree alone explains overlap                                                                                                  |                1 | 6.67%                   |
| Dropped log_pair_hyperedge_count from matching                                                                                            |                1 | 6.67%                   |
| Dropped log_pair_max_node_degree from matching                                                                                            |                1 | 6.67%                   |
| Dropped log_mean_edge_node_degree from matching                                                                                           |                1 | 6.67%                   |
| Dropped mean_pair_essentiality from matching                                                                                              |                1 | 6.67%                   |
| Dropped log_mean_hyperedge_size from matching                                                                                             |                1 | 6.67%                   |
| Single-instance bipartite degree-preserving shuffle                                                                                       |                1 | 6.67%                   |

**Column Grouping: `frozen_primary`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |               13 | 86.67%                  |
| True             |                1 | 6.67%                   |
|                  |                1 | 6.67%                   |

**Column Grouping: `testing_tier`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
|                  |                9 | 60.0%                   |
| secondary        |                5 | 33.33%                  |
| primary          |                1 | 6.67%                   |

**Column Grouping: `hierarchical_reject`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
|                  |                9 | 60.0%                   |
| False            |                5 | 33.33%                  |
| True             |                1 | 6.67%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (15 rows total):

| metric               |   observed_count |   observed_value |   null_mean |   iter_null_std |   iter_null_min |   iter_null_max |   empirical_p_less |   n_permutations | null_type                               | description                                                  | frozen_primary   | testing_tier   |   holm_adjusted_p | hierarchical_reject   |
|:---------------------|-----------------:|-----------------:|------------:|----------------:|----------------:|----------------:|-------------------:|-----------------:|:----------------------------------------|:-------------------------------------------------------------|:-----------------|:---------------|------------------:|:----------------------|
| min_hlrc             |               11 |        -0.567756 |   -0.46836  |        0.055519 |       -0.689173 |       -0.274007 |           0.037196 |            10000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | True             | primary        |          0.037196 | True                  |
| median_hlrc          |               11 |        -0.427964 |   -0.339531 |        0.056697 |       -0.509562 |       -0.169748 |           0.058941 |             1000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | False            | secondary      |          0.294705 | False                 |
| mean_hlrc            |               11 |        -0.394721 |   -0.325718 |        0.051865 |       -0.48347  |       -0.158354 |           0.0999   |             1000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | False            | secondary      |          0.3996   | False                 |
| min_hfrc             |               11 |      -732.364    | -673.427    |      197.642    |    -1313.73     |     -257        |           0.506494 |             1000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | False            | secondary      |          1        | False                 |
| median_hfrc          |               11 |      -225.591    | -476.779    |      156.844    |     -929.409    |     -165.682    |           0.983017 |             1000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | False            | secondary      |          1        | False                 |
| mean_hfrc            |               11 |      -256.762    | -480.194    |      150.083    |     -848.115    |     -176.682    |           0.954046 |             1000 | feature_matched                         | Matched on log_pair_hyperedge_count, log_pair_max_node_de... | False            | secondary      |          1        | False                 |
| min_hlrc             |               11 |        -0.567756 |   -0.243706 |        0.139718 |       -0.653113 |        0.217586 |           0.005994 |             1000 | random_matching                         | Uniform random sampling from background                      |                  |                |        nan        |                       |
| mean_hyperedge_size  |               11 |         6.7957   |    7.66882  |        0.885826 |        5.78002  |       10.2675   |           0.197605 |              500 | ablation_size                           | Testing if size alone explains overlap                       | False            |                |        nan        |                       |
| pair_max_node_degree |               11 |        91.9091   |   73.2009   |       13.2736   |       44.8182   |      115.091    |           0.904192 |              500 | ablation_degree                         | Testing if degree alone explains overlap                     | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |   -0.400373 |        0.068427 |       -0.584378 |       -0.212698 |           0.00998  |              500 | ablation_drop_log_pair_hyperedge_count  | Dropped log_pair_hyperedge_count from matching               | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |   -0.456935 |        0.058753 |       -0.622741 |       -0.317755 |           0.021956 |              500 | ablation_drop_log_pair_max_node_degree  | Dropped log_pair_max_node_degree from matching               | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |   -0.501304 |        0.060204 |       -0.666299 |       -0.332214 |           0.143713 |              500 | ablation_drop_log_mean_edge_node_degree | Dropped log_mean_edge_node_degree from matching              | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |   -0.480429 |        0.054197 |       -0.629159 |       -0.298611 |           0.061876 |              500 | ablation_drop_mean_pair_essentiality    | Dropped mean_pair_essentiality from matching                 | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |   -0.368504 |        0.083175 |       -0.699146 |       -0.135244 |           0.011976 |              500 | ablation_drop_log_mean_hyperedge_size   | Dropped log_mean_hyperedge_size from matching                | False            |                |        nan        |                       |
| min_hlrc             |               11 |        -0.567756 |    0.830835 |        0        |        0.830835 |        0.830835 |         nan        |                1 | bipartite_shuffle                       | Single-instance bipartite degree-preserving shuffle          | False            |                |        nan        |                       |


---

## File: tight_null_lofo_fragility.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/tight_null_lofo_fragility.parquet`
- **Matrix Dimensions:** 11 rows × 4 columns

### 1. Data Schema & Quality Audit

| Column Name      | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:-----------------|:--------|-----------------:|-------------:|:---------|
| omitted_family   | object  |               11 |            0 | 0.00%    |
| n_remaining      | int64   |               11 |            0 | 0.00%    |
| empirical_p_less | float64 |               11 |            0 | 0.00%    |
| observed_value   | float64 |               11 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                  |   count | unique   | top         | freq   | mean      | std      | min       | 25%       | 50%       | 75%       | max       |
|:-----------------|--------:|:---------|:------------|:-------|:----------|:---------|:----------|:----------|:----------|:----------|:----------|
| omitted_family   |      11 | 11       | AP3B2:AP3M2 | 1      | —         | —        | —         | —         | —         | —         | —         |
| n_remaining      |      11 | —        | —           | —      | 10.000000 | 0.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 |
| empirical_p_less |      11 | —        | —           | —      | 0.047583  | 0.021331 | 0.006999  | 0.040696  | 0.048195  | 0.058516  | 0.085914  |
| observed_value   |      11 | —        | —           | —      | -0.567756 | 0.041850 | -0.651956 | -0.573035 | -0.554133 | -0.538715 | -0.530861 |

### 3. Categorical Distribution Breakdown

**Column Grouping: `omitted_family`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| AP3B2:AP3M2      |                1 | 9.09%                   |
| APC:CTNNB1       |                1 | 9.09%                   |
| BRAF:MAP2K1      |                1 | 9.09%                   |
| CD151:ITGA6      |                1 | 9.09%                   |
| CREBBP:EP300     |                1 | 9.09%                   |
| CTNNB1:TCF7L2    |                1 | 9.09%                   |
| DCP2:XRN1        |                1 | 9.09%                   |
| IFT122:WDR35     |                1 | 9.09%                   |
| IL2:IL2RG        |                1 | 9.09%                   |
| NRAS:SHOC2       |                1 | 9.09%                   |
| SMARCA2:SMARCA4  |                1 | 9.09%                   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Showing entire dataset content row footprint (11 rows total):

| omitted_family   |   n_remaining |   empirical_p_less |   observed_value |
|:-----------------|--------------:|-------------------:|-----------------:|
| AP3B2:AP3M2      |            10 |           0.085914 |        -0.642699 |
| APC:CTNNB1       |            10 |           0.050949 |        -0.534201 |
| BRAF:MAP2K1      |            10 |           0.041996 |        -0.551877 |
| CD151:ITGA6      |            10 |           0.061938 |        -0.554133 |
| CREBBP:EP300     |            10 |           0.055094 |        -0.530861 |
| CTNNB1:TCF7L2    |            10 |           0.039396 |        -0.539766 |
| DCP2:XRN1        |            10 |           0.046295 |        -0.556095 |
| IFT122:WDR35     |            10 |           0.006999 |        -0.651956 |
| IL2:IL2RG        |            10 |           0.020698 |        -0.574089 |
| NRAS:SHOC2       |            10 |           0.048195 |        -0.57198  |
| SMARCA2:SMARCA4  |            10 |           0.065934 |        -0.537665 |


---

## File: trrust_family_pair_summary.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/trrust_family_pair_summary.parquet`
- **Matrix Dimensions:** 260576 rows × 19 columns

### 1. Data Schema & Quality Audit

| Column Name               | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------------|:--------|-----------------:|-------------:|:---------|
| pair_key                  | object  |           260576 |            0 | 0.00%    |
| min_hfrc                  | float64 |           260576 |            0 | 0.00%    |
| median_hfrc               | float64 |           260576 |            0 | 0.00%    |
| mean_hfrc                 | float64 |           260576 |            0 | 0.00%    |
| min_hlrc                  | float64 |           260576 |            0 | 0.00%    |
| median_hlrc               | float64 |           260576 |            0 | 0.00%    |
| mean_hlrc                 | float64 |           260576 |            0 | 0.00%    |
| mean_hyperedge_size       | float64 |           260576 |            0 | 0.00%    |
| min_hlrc_hyperedge_size   | int64   |           260576 |            0 | 0.00%    |
| mean_edge_node_degree     | float64 |           260576 |            0 | 0.00%    |
| mean_pair_essentiality    | float64 |           260576 |            0 | 0.00%    |
| pair_max_node_degree      | int64   |           260576 |            0 | 0.00%    |
| pair_hyperedge_count      | int64   |           260576 |            0 | 0.00%    |
| is_systematic_candidate   | int64   |           260576 |            0 | 0.00%    |
| is_validated_candidate    | int64   |           260576 |            0 | 0.00%    |
| log_pair_hyperedge_count  | float64 |           260576 |            0 | 0.00%    |
| log_pair_max_node_degree  | float64 |           260576 |            0 | 0.00%    |
| log_mean_edge_node_degree | float64 |           260576 |            0 | 0.00%    |
| log_mean_hyperedge_size   | float64 |           260576 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                           |   count | unique   | top       | freq   | mean         | std        | min          | 25%          | 50%          | 75%         | max        |
|:--------------------------|--------:|:---------|:----------|:-------|:-------------|:-----------|:-------------|:-------------|:-------------|:------------|:-----------|
| pair_key                  |  260576 | 260576   | A2M:ABCA1 | 1      | —            | —          | —            | —            | —            | —           | —          |
| min_hfrc                  |  260576 | —        | —         | —      | -1685.764084 | 811.556368 | -2318.000000 | -2318.000000 | -2314.000000 | -793.000000 | 3.000000   |
| median_hfrc               |  260576 | —        | —         | —      | -1617.086583 | 805.319608 | -2318.000000 | -2318.000000 | -2263.000000 | -792.000000 | 3.000000   |
| mean_hfrc                 |  260576 | —        | —         | —      | -1610.928540 | 797.303459 | -2318.000000 | -2318.000000 | -2263.000000 | -792.000000 | 3.000000   |
| min_hlrc                  |  260576 | —        | —         | —      | 0.132332     | 0.285197   | -0.941066    | -0.116434    | 0.211056     | 0.448826    | 1.000000   |
| median_hlrc               |  260576 | —        | —         | —      | 0.163111     | 0.259880   | -0.941066    | -0.042965    | 0.218812     | 0.448826    | 1.000000   |
| mean_hlrc                 |  260576 | —        | —         | —      | 0.162492     | 0.259447   | -0.941066    | -0.042965    | 0.214827     | 0.448826    | 1.000000   |
| mean_hyperedge_size       |  260576 | —        | —         | —      | 266.261326   | 170.751669 | 2.000000     | 91.000000    | 299.000000   | 467.000000  | 467.000000 |
| min_hlrc_hyperedge_size   |  260576 | —        | —         | —      | 250.942124   | 178.771704 | 2.000000     | 82.000000    | 299.000000   | 467.000000  | 467.000000 |
| mean_edge_node_degree     |  260576 | —        | —         | —      | 9.340615     | 2.837653   | 1.000000     | 6.963597     | 9.537879     | 10.290123   | 63.666667  |
| mean_pair_essentiality    |  260576 | —        | —         | —      | -0.129573    | 0.282518   | -3.125135    | -0.140081    | -0.038382    | 0.018114    | 0.410825   |
| pair_max_node_degree      |  260576 | —        | —         | —      | 12.307611    | 14.449632  | 1.000000     | 4.000000     | 8.000000     | 14.000000   | 115.000000 |
| pair_hyperedge_count      |  260576 | —        | —         | —      | 1.336382     | 0.774436   | 1.000000     | 1.000000     | 1.000000     | 1.000000    | 32.000000  |
| is_systematic_candidate   |  260576 | —        | —         | —      | 0.000127     | 0.011253   | 0.000000     | 0.000000     | 0.000000     | 0.000000    | 1.000000   |
| is_validated_candidate    |  260576 | —        | —         | —      | 0.008358     | 0.091042   | 0.000000     | 0.000000     | 0.000000     | 0.000000    | 1.000000   |
| log_pair_hyperedge_count  |  260576 | —        | —         | —      | 0.814680     | 0.236859   | 0.693147     | 0.693147     | 0.693147     | 0.693147    | 3.496508   |
| log_pair_max_node_degree  |  260576 | —        | —         | —      | 2.239271     | 0.787161   | 0.693147     | 1.609438     | 2.197225     | 2.708050    | 4.753590   |
| log_mean_edge_node_degree |  260576 | —        | —         | —      | 2.303975     | 0.247251   | 0.693147     | 2.074881     | 2.354976     | 2.423928    | 4.169246   |
| log_mean_hyperedge_size   |  260576 | —        | —         | —      | 5.233386     | 1.005945   | 1.098612     | 4.521789     | 5.703782     | 6.148468    | 6.148468   |

### 4. Significant Signals & Key Highlights

*No default statistical signature triggers detected in this matrix header structure.*

### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| pair_key    |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| A2M:ABCA1   |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                 0.005114 |                     14 |                      2 |                         0 |                        0 |                   1.09861  |                    2.70805 |                     2.47325 |                   5.40042 |
| A2M:ABCB1   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.04344  |                     30 |                      1 |                         0 |                        0 |                   0.693147 |                    3.43399 |                     2.35074 |                   5.71043 |
| A2M:ABCG2   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.039342 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     2.35074 |                   5.71043 |
| A2M:ADORA1  |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.012003 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:ADORA2A |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.030482 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                    1.60944 |                     2.35074 |                   5.71043 |
| A2M:ADORA3  |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.073673 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:AGER    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.058888 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:AGT     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.004882 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.35074 |                   5.71043 |
| A2M:AKAP12  |      -1432 |       -1432   |     -1432   |  -0.00261  |     -0.00261  |   -0.00261  |                 140   |                       140 |                12.2286  |                -0.017125 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.58238 |                   4.94876 |
| A2M:AKT1    |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                -0.042651 |                      7 |                      2 |                         0 |                        0 |                   1.09861  |                    2.07944 |                     2.47325 |                   5.40042 |
| A2M:AKT2    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.036017 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                    1.60944 |                     2.35074 |                   5.71043 |
| A2M:ALOX5   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.051199 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.35074 |                   5.71043 |
| A2M:ALOX5AP |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.068939 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:AMH     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.010428 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.35074 |                   5.71043 |
| A2M:AR      |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                 0.048335 |                     46 |                      2 |                         0 |                        0 |                   1.09861  |                    3.85015 |                     2.47325 |                   5.40042 |
| A2M:ATF3    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.027578 |                     12 |                      1 |                         0 |                        0 |                   0.693147 |                    2.56495 |                     2.35074 |                   5.71043 |
| A2M:B2M     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.016957 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:BACE1   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.047361 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.35074 |                   5.71043 |
| A2M:BAX     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.045151 |                     26 |                      1 |                         0 |                        0 |                   0.693147 |                    3.29584 |                     2.35074 |                   5.71043 |
| A2M:BCL2    |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                -0.017454 |                     45 |                      2 |                         0 |                        0 |                   1.09861  |                    3.82864 |                     2.47325 |                   5.40042 |
| A2M:BCL2A1  |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.010626 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.35074 |                   5.71043 |
| A2M:BCL2L1  |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                -0.584964 |                     16 |                      2 |                         0 |                        0 |                   1.09861  |                    2.83321 |                     2.47325 |                   5.40042 |
| A2M:BCL2L11 |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.003927 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                    1.60944 |                     2.35074 |                   5.71043 |
| A2M:BCL3    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.033699 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                    1.60944 |                     2.35074 |                   5.71043 |
| A2M:BCL6    |      -1432 |       -1432   |     -1432   |  -0.00261  |     -0.00261  |   -0.00261  |                 140   |                       140 |                12.2286  |                -0.062351 |                     14 |                      1 |                         0 |                        0 |                   0.693147 |                    2.70805 |                     2.58238 |                   4.94876 |
| A2M:BDKRB1  |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.070662 |                     11 |                      1 |                         0 |                        0 |                   0.693147 |                    2.48491 |                     2.35074 |                   5.71043 |
| A2M:BGN     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.040296 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:BHMT    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.042791 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:BIRC2   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.113667 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:BIRC3   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.024029 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.35074 |                   5.71043 |
| A2M:BIRC5   |      -2263 |       -1847.5 |     -1847.5 |  -0.00261  |      0.111979 |    0.111979 |                 220.5 |                       140 |                10.861   |                -0.974945 |                     25 |                      2 |                         0 |                        0 |                   1.09861  |                    3.2581  |                     2.47325 |                   5.40042 |
| A2M:BMP2    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.014685 |                      4 |                      1 |                         0 |                        0 |                   0.693147 |                    1.60944 |                     2.35074 |                   5.71043 |
| A2M:BRCA2   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.258292 |                     13 |                      1 |                         0 |                        0 |                   0.693147 |                    2.63906 |                     2.35074 |                   5.71043 |
| A2M:BST1    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.056705 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:BTG2    |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.024503 |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.35074 |                   5.71043 |
| A2M:CARD8   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.038437 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:CARM1   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.16167  |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:CASP3   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.027134 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.35074 |                   5.71043 |
| A2M:CASP9   |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                -0.01102  |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.35074 |                   5.71043 |
| A2M:CCK     |      -2263 |       -2263   |     -2263   |   0.226568 |      0.226568 |    0.226568 |                 301   |                       301 |                 9.49338 |                 0.013745 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     2.35074 |                   5.71043 |


*... [Truncated 260496 standard row items inline] ...*

**Last 40 Structural Rows:**

| pair_key     |   min_hfrc |   median_hfrc |   mean_hfrc |   min_hlrc |   median_hlrc |   mean_hlrc |   mean_hyperedge_size |   min_hlrc_hyperedge_size |   mean_edge_node_degree |   mean_pair_essentiality |   pair_max_node_degree |   pair_hyperedge_count |   is_systematic_candidate |   is_validated_candidate |   log_pair_hyperedge_count |   log_pair_max_node_degree |   log_mean_edge_node_degree |   log_mean_hyperedge_size |
|:-------------|-----------:|--------------:|------------:|-----------:|--------------:|------------:|----------------------:|--------------------------:|------------------------:|-------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|---------------------------:|---------------------------:|----------------------------:|--------------------------:|
| WDFY4:ZNF175 |       -637 |        -637   |     -637    |  -0.042965 |     -0.042965 |   -0.042965 |                91     |                        91 |                 9       |                 0.044981 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.30259 |                   4.52179 |
| WEE1:WNT7B   |       -721 |        -721   |     -721    |   0.079064 |      0.079064 |    0.079064 |                92     |                        92 |                 9.83696 |                -1.28968  |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.38296 |                   4.5326  |
| WEE1:XIAP    |       -721 |        -721   |     -721    |   0.079064 |      0.079064 |    0.079064 |                92     |                        92 |                 9.83696 |                -1.30418  |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.38296 |                   4.5326  |
| WFS1:XBP1    |       -211 |        -211   |     -211    |  -0.226624 |     -0.226624 |   -0.226624 |                19     |                        19 |                13.1053  |                 0.062343 |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                    1.94591 |                     2.64655 |                   2.99573 |
| WFS1:ZHX2    |       -211 |        -211   |     -211    |  -0.226624 |     -0.226624 |   -0.226624 |                19     |                        19 |                13.1053  |                 0.102323 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     2.64655 |                   2.99573 |
| WIF1:WRN     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.10005  |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.07488 |                   6.14847 |
| WIF1:WT1     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                 0.031157 |                     17 |                      1 |                         0 |                        0 |                   0.693147 |                    2.89037 |                     2.07488 |                   6.14847 |
| WIF1:XIAP    |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.022611 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.07488 |                   6.14847 |
| WIF1:XPC     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                 0.027386 |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.07488 |                   6.14847 |
| WIF1:YY1     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.392879 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.07488 |                   6.14847 |
| WNT11:ZEB1   |       -149 |        -149   |     -149    |  -0.123905 |     -0.123905 |   -0.123905 |                26     |                        26 |                 7.51852 |                -0.037251 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     2.14224 |                   3.29584 |
| WNT2:WNT5A   |        -48 |         -48   |      -48    |   0.089682 |      0.089682 |    0.089682 |                12     |                        12 |                 6       |                 0.010445 |                      3 |                      1 |                         0 |                        0 |                   0.693147 |                    1.38629 |                     1.94591 |                   2.56495 |
| WNT7B:XIAP   |       -721 |        -721   |     -721    |   0.079064 |      0.079064 |    0.079064 |                92     |                        92 |                 9.83696 |                -0.010775 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.38296 |                   4.5326  |
| WRN:WT1      |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.048938 |                     17 |                      1 |                         0 |                        0 |                   0.693147 |                    2.89037 |                     2.07488 |                   6.14847 |
| WRN:XIAP     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.102706 |                      5 |                      1 |                         0 |                        0 |                   0.693147 |                    1.79176 |                     2.07488 |                   6.14847 |
| WRN:XPC      |      -2318 |       -1343   |    -1443.67 |  -0.167924 |      0.083392 |    0.121431 |               225.667 |                        49 |                10.9757  |                -0.052709 |                      8 |                      3 |                         0 |                        0 |                   1.38629  |                    2.19722 |                     2.48288 |                   5.42348 |
| WRN:XPO1     |      -1343 |       -1067.5 |    -1067.5  |  -0.011415 |      0.035989 |    0.035989 |               130     |                        99 |                10.1451  |                -1.16119  |                      5 |                      2 |                         0 |                        0 |                   1.09861  |                    1.79176 |                     2.411   |                   4.8752  |
| WRN:YY1      |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.472974 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.07488 |                   6.14847 |
| WT1:WTAP     |       -739 |        -739   |     -739    |  -0.179362 |     -0.179362 |   -0.179362 |                56     |                        56 |                15.1964  |                -0.264466 |                     17 |                      1 |                         0 |                        0 |                   0.693147 |                    2.89037 |                     2.78479 |                   4.04305 |
| WT1:XIAP     |      -2318 |       -2314   |    -2298.33 |   0.211056 |      0.226568 |    0.295483 |               355.667 |                       299 |                 8.73203 |                 0.028501 |                     17 |                      3 |                         0 |                        0 |                   1.38629  |                    2.89037 |                     2.27542 |                   5.8768  |
| WT1:XPC      |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                 0.078499 |                     17 |                      1 |                         0 |                        1 |                   0.693147 |                    2.89037 |                     2.07488 |                   6.14847 |
| WT1:YY1      |      -2318 |       -2263   |    -1574.2  |  -0.417897 |      0.211056 |    0.039138 |               226.6   |                        57 |                10.3995  |                -0.341767 |                     17 |                      5 |                         0 |                        0 |                   1.79176  |                    2.89037 |                     2.43357 |                   5.42759 |
| WT1:ZEB1     |       -926 |        -926   |     -926    |  -0.417897 |     -0.417897 |   -0.417897 |                57     |                        57 |                18.2456  |                 0.00681  |                     17 |                      1 |                         0 |                        0 |                   0.693147 |                    2.89037 |                     2.95728 |                   4.06044 |
| WT1:ZNF268   |       -174 |        -174   |     -174    |  -0.008815 |     -0.008815 |   -0.008815 |                53     |                        53 |                 5.22222 |                 0.104344 |                     17 |                      1 |                         0 |                        0 |                   0.693147 |                    2.89037 |                     1.82813 |                   3.98898 |
| WWOX:XRCC1   |       -995 |        -995   |     -995    |   0.132382 |      0.132382 |    0.132382 |               131     |                       131 |                 9.53788 |                -0.125629 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                    1.09861 |                     2.35498 |                   4.8828  |
| WWOX:ZNF350  |       -995 |        -995   |     -995    |   0.132382 |      0.132382 |    0.132382 |               131     |                       131 |                 9.53788 |                 0.05848  |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                    1.09861 |                     2.35498 |                   4.8828  |
| XBP1:ZHX2    |       -211 |        -211   |     -211    |  -0.226624 |     -0.226624 |   -0.226624 |                19     |                        19 |                13.1053  |                 0.02105  |                      6 |                      1 |                         0 |                        0 |                   0.693147 |                    1.94591 |                     2.64655 |                   2.99573 |
| XIAP:XPC     |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                 0.02473  |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.07488 |                   6.14847 |
| XIAP:YY1     |      -2318 |       -2314   |    -2298.33 |   0.211056 |      0.226568 |    0.295483 |               355.667 |                       299 |                 8.73203 |                -0.395535 |                     10 |                      3 |                         0 |                        0 |                   1.38629  |                    2.3979  |                     2.27542 |                   5.8768  |
| XPC:XPO1     |      -1343 |       -1343   |    -1343    |   0.083392 |      0.083392 |    0.083392 |               161     |                       161 |                10.2901  |                -1.03376  |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.42393 |                   5.0876  |
| XPC:YY1      |      -2318 |       -2318   |    -2318    |   0.448826 |      0.448826 |    0.448826 |               467     |                       467 |                 6.9636  |                -0.345538 |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.07488 |                   6.14847 |
| XPC:ZNF217   |       -632 |        -632   |     -632    |  -0.067713 |     -0.067713 |   -0.067713 |                82     |                        82 |                 9.61446 |                -0.196845 |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.36222 |                   4.41884 |
| XPC:ZNF750   |       -234 |        -234   |     -234    |  -0.337597 |     -0.337597 |   -0.337597 |                15     |                        15 |                17.6     |                 0.011051 |                      8 |                      1 |                         0 |                        0 |                   0.693147 |                    2.19722 |                     2.92316 |                   2.77259 |
| XRCC1:ZNF350 |       -995 |        -995   |     -995    |   0.132382 |      0.132382 |    0.132382 |               131     |                       131 |                 9.53788 |                -0.179955 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                    1.09861 |                     2.35498 |                   4.8828  |
| YWHAQ:ZEB1   |      -1034 |       -1034   |    -1034    |  -0.134149 |     -0.134149 |   -0.134149 |                76     |                        76 |                15.4286  |                 0.006736 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     2.79902 |                   4.3438  |
| YWHAQ:ZFHX3  |      -1034 |       -1034   |    -1034    |  -0.134149 |     -0.134149 |   -0.134149 |                76     |                        76 |                15.4286  |                 0.059722 |                      2 |                      1 |                         0 |                        0 |                   0.693147 |                    1.09861 |                     2.79902 |                   4.3438  |
| YY1:ZEB1     |       -926 |        -560.5 |     -560.5  |  -0.417897 |     -0.370548 |   -0.370548 |                35.5   |                        57 |                17.0871  |                -0.417226 |                     10 |                      2 |                         0 |                        0 |                   1.09861  |                    2.3979  |                     2.8952  |                   3.59731 |
| YY1:ZNF175   |       -637 |        -637   |     -637    |  -0.042965 |     -0.042965 |   -0.042965 |                91     |                        91 |                 9       |                -0.3586   |                     10 |                      1 |                         0 |                        0 |                   0.693147 |                    2.3979  |                     2.30259 |                   4.52179 |
| ZEB1:ZEB2    |         -6 |          -6   |       -6    |  -0.087607 |     -0.087607 |   -0.087607 |                 4     |                         4 |                 3.5     |                -0.213361 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     1.50408 |                   1.60944 |
| ZEB1:ZFHX3   |      -1034 |       -1034   |    -1034    |  -0.134149 |     -0.134149 |   -0.134149 |                76     |                        76 |                15.4286  |                -0.015663 |                      9 |                      1 |                         0 |                        0 |                   0.693147 |                    2.30259 |                     2.79902 |                   4.3438  |


---

## File: validation_candidate_dependency_pairs.parquet

- **Source Framework Category:** Parquet Table
- **Project Relative Path:** `results/tables/validation_candidate_dependency_pairs.parquet`
- **Matrix Dimensions:** 862 rows × 12 columns

### 1. Data Schema & Quality Audit

| Column Name               | Dtype   |   Non-Null Count |   Null Count | Null %   |
|:--------------------------|:--------|-----------------:|-------------:|:---------|
| mutation_gene             | object  |              862 |            0 | 0.00%    |
| partner_gene              | object  |              862 |            0 | 0.00%    |
| mutation_type             | object  |              862 |            0 | 0.00%    |
| validation_num_mutant     | int64   |              862 |            0 | 0.00%    |
| num_wildtype_models       | int64   |              862 |            0 | 0.00%    |
| validation_delta          | float64 |              862 |            0 | 0.00%    |
| validation_p_value        | float64 |              862 |            0 | 0.00%    |
| fdr                       | float64 |              862 |            0 | 0.00%    |
| passes_main_thresholds    | bool    |              862 |            0 | 0.00%    |
| topology                  | object  |              862 |            0 | 0.00%    |
| undirected_key            | object  |              862 |            0 | 0.00%    |
| passes_validation_nominal | bool    |              862 |            0 | 0.00%    |

### 2. Full Descriptive Summary Statistics

|                           |   count | unique   | top        | freq   | mean       | std       | min       | 25%        | 50%        | 75%        | max        |
|:--------------------------|--------:|:---------|:-----------|:-------|:-----------|:----------|:----------|:-----------|:-----------|:-----------|:-----------|
| mutation_gene             |     862 | 63       | TP53       | 81     | —          | —         | —         | —          | —          | —          | —          |
| partner_gene              |     862 | 507      | SMAD3      | 9      | —          | —         | —         | —          | —          | —          | —          |
| mutation_type             |     862 | 2        | damaging   | 726    | —          | —         | —         | —          | —          | —          | —          |
| validation_num_mutant     |     862 | —        | —          | —      | 37.454756  | 60.621000 | 10.000000 | 11.000000  | 16.000000  | 23.000000  | 246.000000 |
| num_wildtype_models       |     862 | —        | —          | —      | 402.943155 | 62.041818 | 13.000000 | 418.000000 | 425.000000 | 430.000000 | 431.000000 |
| validation_delta          |     862 | —        | —          | —      | -0.003862  | 0.095185  | -0.432496 | -0.044856  | -0.000026  | 0.034761   | 0.715264   |
| validation_p_value        |     862 | —        | —          | —      | 0.424631   | 0.304022  | 0.000000  | 0.140681   | 0.401600   | 0.681113   | 0.999126   |
| fdr                       |     862 | —        | —          | —      | 0.711836   | 0.254787  | 0.000000  | 0.560921   | 0.807134   | 0.907238   | 1.000000   |
| passes_main_thresholds    |     862 | 2        | False      | 854    | —          | —         | —         | —          | —          | —          | —          |
| topology                  |     862 | 1        | corum      | 862    | —          | —         | —         | —          | —          | —          | —          |
| undirected_key            |     862 | 764      | SMAD4:TP53 | 3      | —          | —         | —         | —          | —          | —          | —          |
| passes_validation_nominal |     862 | 2        | False      | 803    | —          | —         | —         | —          | —          | —          | —          |

### 3. Categorical Distribution Breakdown

**Column Grouping: `mutation_type`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| damaging         |              726 | 84.22%                  |
| hotspot          |              136 | 15.78%                  |

**Column Grouping: `passes_main_thresholds`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |              854 | 99.07%                  |
| True             |                8 | 0.93%                   |

**Column Grouping: `passes_validation_nominal`**

| Value Category   |   Absolute Count | Percentage Proportion   |
|:-----------------|-----------------:|:------------------------|
| False            |              803 | 93.16%                  |
| True             |               59 | 6.84%                   |

### 4. Significant Signals & Key Highlights

- 💡 **Significance Hit:** Column `validation_p_value` contains **109** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   validation_num_mutant |   num_wildtype_models |   validation_delta |   validation_p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|------------------------:|----------------------:|-------------------:|---------------------:|------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| TP53            | MDM2           | damaging        |                     246 |                   195 |           0.715264 |                    0 |     0 | False                    | corum      | MDM2:TP53        | False                       |
| TP53            | MDM2           | hotspot         |                     198 |                   243 |           0.601941 |                    0 |     0 | False                    | corum      | MDM2:TP53        | False                       |
| TP53            | MDM4           | hotspot         |                     198 |                   243 |           0.315305 |                    0 |     0 | False                    | corum      | MDM4:TP53        | False                       |
| TP53            | MDM4           | damaging        |                     246 |                   195 |           0.358618 |                    0 |     0 | False                    | corum      | MDM4:TP53        | False                       |
| TP53            | USP7           | damaging        |                     246 |                   195 |           0.398691 |                    0 |     0 | False                    | corum      | TP53:USP7        | False                       |

- 💡 **Significance Hit:** Column `fdr` contains **28** records with a nominal significance value ($P < 0.05$).

*Top localized significance indices:*

| mutation_gene   | partner_gene   | mutation_type   |   validation_num_mutant |   num_wildtype_models |   validation_delta |   validation_p_value |   fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|------------------------:|----------------------:|-------------------:|---------------------:|------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| TP53            | MDM2           | damaging        |                     246 |                   195 |           0.715264 |                    0 |     0 | False                    | corum      | MDM2:TP53        | False                       |
| TP53            | MDM2           | hotspot         |                     198 |                   243 |           0.601941 |                    0 |     0 | False                    | corum      | MDM2:TP53        | False                       |
| TP53            | MDM4           | hotspot         |                     198 |                   243 |           0.315305 |                    0 |     0 | False                    | corum      | MDM4:TP53        | False                       |
| TP53            | MDM4           | damaging        |                     246 |                   195 |           0.358618 |                    0 |     0 | False                    | corum      | MDM4:TP53        | False                       |
| TP53            | USP7           | damaging        |                     246 |                   195 |           0.398691 |                    0 |     0 | False                    | corum      | TP53:USP7        | False                       |


### 5. High-Fidelity Data Preview

Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):

**First 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   validation_num_mutant |   num_wildtype_models |   validation_delta |   validation_p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|------------------------:|----------------------:|-------------------:|---------------------:|---------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| ABCA12          | ABCA1          | damaging        |                      11 |                   430 |          -0.046231 |             0.23544  | 0.690303 | False                    | corum      | ABCA1:ABCA12     | False                       |
| ABCA12          | NR1H2          | damaging        |                      11 |                   430 |          -0.069802 |             0.098615 | 0.512084 | False                    | corum      | ABCA12:NR1H2     | False                       |
| AKAP9           | CAMSAP2        | damaging        |                      16 |                   425 |          -0.122922 |             0.023361 | 0.258173 | False                    | corum      | AKAP9:CAMSAP2    | True                        |
| AKAP9           | CDK5RAP2       | damaging        |                      16 |                   425 |          -0.011272 |             0.808799 | 0.945977 | False                    | corum      | AKAP9:CDK5RAP2   | False                       |
| AKAP9           | FYN            | damaging        |                      16 |                   425 |           0.008474 |             0.791966 | 0.942921 | False                    | corum      | AKAP9:FYN        | False                       |
| AKAP9           | KCNQ1          | damaging        |                      16 |                   425 |           0.011499 |             0.726711 | 0.91986  | False                    | corum      | AKAP9:KCNQ1      | False                       |
| AKAP9           | MAPRE1         | damaging        |                      16 |                   425 |           0.008986 |             0.860193 | 0.965477 | False                    | corum      | AKAP9:MAPRE1     | False                       |
| AKAP9           | MAPRE3         | damaging        |                      16 |                   425 |           0.029151 |             0.393032 | 0.806652 | False                    | corum      | AKAP9:MAPRE3     | False                       |
| AKAP9           | PDE4D          | damaging        |                      16 |                   425 |           0.04941  |             0.13631  | 0.554243 | False                    | corum      | AKAP9:PDE4D      | False                       |
| AKAP9           | PDE4DIP        | damaging        |                      16 |                   425 |           0.010876 |             0.826057 | 0.955786 | False                    | corum      | AKAP9:PDE4DIP    | False                       |
| AKAP9           | PPP1CA         | damaging        |                      16 |                   425 |           0.056766 |             0.394484 | 0.807709 | False                    | corum      | AKAP9:PPP1CA     | False                       |
| AKAP9           | PRKACA         | damaging        |                      16 |                   425 |          -0.010066 |             0.765107 | 0.926295 | False                    | corum      | AKAP9:PRKACA     | False                       |
| AKAP9           | PRKAR2A        | damaging        |                      16 |                   425 |           0.024647 |             0.432297 | 0.81899  | False                    | corum      | AKAP9:PRKAR2A    | False                       |
| AKAP9           | PRKAR2B        | damaging        |                      16 |                   425 |          -0.014066 |             0.71801  | 0.915569 | False                    | corum      | AKAP9:PRKAR2B    | False                       |
| ALK             | ERRFI1         | hotspot         |                      10 |                   431 |          -0.106799 |             0.018737 | 0.264781 | False                    | corum      | ALK:ERRFI1       | True                        |
| ALK             | GRB2           | hotspot         |                      10 |                   431 |          -0.311063 |             0.023458 | 0.255964 | False                    | corum      | ALK:GRB2         | True                        |
| ALK             | TNK2           | hotspot         |                      10 |                   431 |           0.059074 |             0.251838 | 0.700271 | False                    | corum      | ALK:TNK2         | False                       |
| ARID1A          | ACTB           | damaging        |                      59 |                   382 |          -0.100553 |             0.099297 | 0.512541 | False                    | corum      | ACTB:ARID1A      | False                       |
| ARID1A          | ACTL6A         | damaging        |                      59 |                   382 |          -0.003473 |             0.942744 | 0.987419 | False                    | corum      | ACTL6A:ARID1A    | False                       |
| ARID1A          | BRCA1          | damaging        |                      59 |                   382 |          -0.082871 |             0.01987  | 0.255635 | False                    | corum      | ARID1A:BRCA1     | True                        |
| ARID1A          | CARM1          | damaging        |                      59 |                   382 |          -0.035257 |             0.42367  | 0.820681 | False                    | corum      | ARID1A:CARM1     | False                       |
| ARID1A          | CREBBP         | damaging        |                      59 |                   382 |           0.050924 |             0.207554 | 0.665099 | False                    | corum      | ARID1A:CREBBP    | False                       |
| ARID1A          | EP300          | damaging        |                      59 |                   382 |           0.098902 |             0.087497 | 0.496197 | False                    | corum      | ARID1A:EP300     | False                       |
| ARID1A          | MLLT1          | damaging        |                      59 |                   382 |           0.029978 |             0.26809  | 0.704552 | False                    | corum      | ARID1A:MLLT1     | False                       |
| ARID1A          | PRMT5          | damaging        |                      59 |                   382 |           0.031736 |             0.559707 | 0.864637 | False                    | corum      | ARID1A:PRMT5     | False                       |
| ARID1A          | SCYL1          | damaging        |                      59 |                   382 |          -0.020368 |             0.546678 | 0.855239 | False                    | corum      | ARID1A:SCYL1     | False                       |
| ARID1A          | SMARCA2        | damaging        |                      59 |                   382 |           0.040279 |             0.054979 | 0.398248 | False                    | corum      | ARID1A:SMARCA2   | False                       |
| ARID1A          | SMARCA4        | damaging        |                      59 |                   382 |           0.057493 |             0.196617 | 0.649363 | False                    | corum      | ARID1A:SMARCA4   | False                       |
| ARID1A          | SMARCB1        | damaging        |                      59 |                   382 |           0.079459 |             0.100862 | 0.508441 | False                    | corum      | ARID1A:SMARCB1   | False                       |
| ARID1A          | SMARCC1        | damaging        |                      59 |                   382 |           0.085584 |             0.000341 | 0.014692 | False                    | corum      | ARID1A:SMARCC1   | False                       |
| ARID1A          | SMARCC2        | damaging        |                      59 |                   382 |           0.045191 |             0.026694 | 0.273932 | False                    | corum      | ARID1A:SMARCC2   | False                       |
| ARID1A          | SMARCD1        | damaging        |                      59 |                   382 |          -0.036036 |             0.367916 | 0.781143 | False                    | corum      | ARID1A:SMARCD1   | False                       |
| ARID1A          | SMARCD2        | damaging        |                      59 |                   382 |           0.035259 |             0.103406 | 0.518233 | False                    | corum      | ARID1A:SMARCD2   | False                       |
| ARID1A          | SMARCE1        | damaging        |                      59 |                   382 |           0.033958 |             0.442528 | 0.815083 | False                    | corum      | ARID1A:SMARCE1   | False                       |
| ARID1B          | ACTL6A         | damaging        |                      16 |                   425 |          -0.110515 |             0.292607 | 0.72898  | False                    | corum      | ACTL6A:ARID1B    | False                       |
| ARID1B          | CREBBP         | damaging        |                      16 |                   425 |           0.07181  |             0.307214 | 0.741788 | False                    | corum      | ARID1B:CREBBP    | False                       |
| ARID1B          | MLLT1          | damaging        |                      16 |                   425 |           0.005741 |             0.851822 | 0.958577 | False                    | corum      | ARID1B:MLLT1     | False                       |
| ARID1B          | NCOA3          | damaging        |                      16 |                   425 |          -0.010709 |             0.748927 | 0.92755  | False                    | corum      | ARID1B:NCOA3     | False                       |
| ARID1B          | SMAD2          | damaging        |                      16 |                   425 |          -0.006677 |             0.824195 | 0.954914 | False                    | corum      | ARID1B:SMAD2     | False                       |
| ARID1B          | SMAD3          | damaging        |                      16 |                   425 |           0.00675  |             0.84973  | 0.959983 | False                    | corum      | ARID1B:SMAD3     | False                       |


*... [Truncated 782 standard row items inline] ...*

**Last 40 Structural Rows:**

| mutation_gene   | partner_gene   | mutation_type   |   validation_num_mutant |   num_wildtype_models |   validation_delta |   validation_p_value |      fdr | passes_main_thresholds   | topology   | undirected_key   | passes_validation_nominal   |
|:----------------|:---------------|:----------------|------------------------:|----------------------:|-------------------:|---------------------:|---------:|:-------------------------|:-----------|:-----------------|:----------------------------|
| TP53BP1         | RIF1           | damaging        |                      12 |                   429 |          -0.066527 |             0.313956 | 0.749667 | False                    | corum      | RIF1:TP53BP1     | False                       |
| TP53BP1         | RPA1           | damaging        |                      12 |                   429 |          -0.071664 |             0.587576 | 0.864318 | False                    | corum      | RPA1:TP53BP1     | False                       |
| TP53BP1         | RPA2           | damaging        |                      12 |                   429 |          -0.002515 |             0.983783 | 1        | False                    | corum      | RPA2:TP53BP1     | False                       |
| TP53BP1         | SHLD2          | damaging        |                      12 |                   429 |           0.032062 |             0.704729 | 0.917638 | False                    | corum      | SHLD2:TP53BP1    | False                       |
| TP53BP1         | SMC1A          | damaging        |                      12 |                   429 |          -0.094381 |             0.287778 | 0.723219 | False                    | corum      | SMC1A:TP53BP1    | False                       |
| TP53BP1         | XRCC5          | damaging        |                      12 |                   429 |          -0.038446 |             0.580238 | 0.865338 | False                    | corum      | TP53BP1:XRCC5    | False                       |
| TP53BP1         | XRCC6          | damaging        |                      12 |                   429 |           0.131735 |             0.078791 | 0.465191 | False                    | corum      | TP53BP1:XRCC6    | False                       |
| TSC2            | AXIN1          | damaging        |                      10 |                   431 |           0.022873 |             0.725557 | 0.91975  | False                    | corum      | AXIN1:TSC2       | False                       |
| TSC2            | CDC37          | damaging        |                      10 |                   431 |           0.123121 |             0.309493 | 0.743128 | False                    | corum      | CDC37:TSC2       | False                       |
| TSC2            | DVL1           | damaging        |                      10 |                   431 |           0.047493 |             0.150305 | 0.573287 | False                    | corum      | DVL1:TSC2        | False                       |
| TSC2            | GSK3B          | damaging        |                      10 |                   431 |           0.009251 |             0.927795 | 0.989801 | False                    | corum      | GSK3B:TSC2       | False                       |
| TSC2            | HSP90AA1       | damaging        |                      10 |                   431 |          -0.02835  |             0.515114 | 0.842558 | False                    | corum      | HSP90AA1:TSC2    | False                       |
| TSC2            | PPP5C          | damaging        |                      10 |                   431 |          -0.051167 |             0.17271  | 0.612659 | False                    | corum      | PPP5C:TSC2       | False                       |
| TSC2            | TBC1D7         | damaging        |                      10 |                   431 |           0.025267 |             0.583766 | 0.864615 | False                    | corum      | TBC1D7:TSC2      | False                       |
| TSC2            | TSC1           | damaging        |                      10 |                   431 |          -0.015678 |             0.832657 | 0.957001 | False                    | corum      | TSC1:TSC2        | False                       |
| UNC79           | NALCN          | damaging        |                      14 |                   427 |           0.000269 |             0.994747 | 1        | False                    | corum      | NALCN:UNC79      | False                       |
| UNC79           | UNC80          | damaging        |                      14 |                   427 |           0.03884  |             0.439701 | 0.818622 | False                    | corum      | UNC79:UNC80      | False                       |
| USH2A           | ADGRV1         | damaging        |                      11 |                   430 |          -0.026459 |             0.440994 | 0.815744 | False                    | corum      | ADGRV1:USH2A     | False                       |
| USH2A           | PDZD7          | damaging        |                      11 |                   430 |          -0.043267 |             0.2927   | 0.727111 | False                    | corum      | PDZD7:USH2A      | False                       |
| USH2A           | USH1G          | damaging        |                      11 |                   430 |          -0.057479 |             0.128901 | 0.552801 | False                    | corum      | USH1G:USH2A      | False                       |
| USH2A           | WHRN           | damaging        |                      11 |                   430 |           0.010015 |             0.804001 | 0.946788 | False                    | corum      | USH2A:WHRN       | False                       |
| VHL             | AKAP6          | damaging        |                      22 |                   419 |          -0.053522 |             0.043589 | 0.357848 | False                    | corum      | AKAP6:VHL        | True                        |
| VHL             | CUL2           | damaging        |                      22 |                   419 |          -0.047438 |             0.566624 | 0.86601  | False                    | corum      | CUL2:VHL         | False                       |
| VHL             | EGLN1          | damaging        |                      22 |                   419 |           0.307101 |             1.6e-05  | 0.001225 | False                    | corum      | EGLN1:VHL        | False                       |
| VHL             | ELOB           | damaging        |                      22 |                   419 |           0.367515 |             0.003073 | 0.082776 | False                    | corum      | ELOB:VHL         | False                       |
| VHL             | ELOC           | damaging        |                      22 |                   419 |           0.097046 |             0.17948  | 0.621333 | False                    | corum      | ELOC:VHL         | False                       |
| VHL             | HIF1A          | damaging        |                      22 |                   419 |           0.274483 |             0.000161 | 0.00865  | False                    | corum      | HIF1A:VHL        | False                       |
| VHL             | LIMD1          | damaging        |                      22 |                   419 |           0.042212 |             0.121664 | 0.543388 | False                    | corum      | LIMD1:VHL        | False                       |
| VHL             | PLD1           | damaging        |                      22 |                   419 |          -0.029667 |             0.243509 | 0.699682 | False                    | corum      | PLD1:VHL         | False                       |
| VHL             | PSMC3          | damaging        |                      22 |                   419 |           0.020418 |             0.843161 | 0.962655 | False                    | corum      | PSMC3:VHL        | False                       |
| VHL             | RBX1           | damaging        |                      22 |                   419 |           0.075787 |             0.153714 | 0.576095 | False                    | corum      | RBX1:VHL         | False                       |
| VHL             | RHOBTB3        | damaging        |                      22 |                   419 |           0.060647 |             0.15772  | 0.583495 | False                    | corum      | RHOBTB3:VHL      | False                       |
| VHL             | USP33          | damaging        |                      22 |                   419 |          -0.051592 |             0.054636 | 0.399123 | False                    | corum      | USP33:VHL        | False                       |
| WRN             | BCAS2          | damaging        |                      14 |                   427 |          -0.067408 |             0.473584 | 0.816459 | False                    | corum      | BCAS2:WRN        | False                       |
| WRN             | CDC5L          | damaging        |                      14 |                   427 |           0.065505 |             0.568195 | 0.863817 | False                    | corum      | CDC5L:WRN        | False                       |
| WRN             | PARP1          | damaging        |                      14 |                   427 |           0.019333 |             0.73992  | 0.924364 | False                    | corum      | PARP1:WRN        | False                       |
| WRN             | PLRG1          | damaging        |                      14 |                   427 |           0.012771 |             0.843127 | 0.963894 | False                    | corum      | PLRG1:WRN        | False                       |
| WRN             | PRPF19         | damaging        |                      14 |                   427 |          -0.041206 |             0.697292 | 0.917658 | False                    | corum      | PRPF19:WRN       | False                       |
| WRN             | XRCC5          | damaging        |                      14 |                   427 |          -0.085351 |             0.462629 | 0.818863 | False                    | corum      | WRN:XRCC5        | False                       |
| WRN             | XRCC6          | damaging        |                      14 |                   427 |          -0.147678 |             0.140421 | 0.560385 | False                    | corum      | WRN:XRCC6        | False                       |


---

