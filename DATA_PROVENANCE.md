# Data Provenance & Acquisition

To reproduce the Curvature pipeline results, the following specific dataset versions must be acquired. Most are public and can be downloaded from their respective portals.

## 1. Cancer Dependency Map (DepMap)
*   **Release**: 24Q2 (Primary) and 25Q3 (External Validation)
*   **Portal**: [depmap.org](https://depmap.org/portal/download/all/)
*   **Files Required**:
    *   `Model.csv`
    *   `CRISPRGeneEffect.csv`
    *   `OmicsSomaticMutationsMatrixDamaging.csv`
    *   `OmicsSomaticMutationsMatrixHotspot.csv`

## 2. CORUM (Comprehensive Resource of Mammalian Protein Complexes)
*   **Version**: 4.1 (Human Complex set)
*   **Portal**: [mips.helmholtz-muenchen.de/corum/](http://mips.helmholtz-muenchen.de/corum/#download)
*   **File**: `corum_humanComplexes.txt` (Complete complexes)

## 3. STRING Database
*   **Version**: 12.0
*   **Portal**: [string-db.org](https://string-db.org/cgi/download?sessionId=b6Z1O1mZp1Z1)
*   **Organism**: *Homo sapiens* (9606)
*   **Files**:
    *   `protein.aliases.v12.0.txt.gz`
    *   `protein.physical.links.detailed.v12.0.txt.gz`

## 4. TRRUST (Transcriptional Regulatory Relationships Unraveled by Sentence-based Text mining)
*   **Version**: v2
*   **Portal**: [grnpedia.org/trrust/](https://www.grnpedia.org/trrust/download.php)
*   **File**: `trrust_rawdata.human.tsv`

## 5. TCGA (The Cancer Genome Atlas)
*   **Data Source**: GDC Data Portal / Pan-Cancer Atlas
*   **Files**:
    *   **Clinical**: `TCGA-CDR-SupplementalTableS1.xlsx` (Liu et al., *Cell* 2018)
    *   **Mutations**: `mc3.v0.2.8.PUBLIC.maf.gz` (Pan-Cancer MC3 Mutation Calling)

## 6. Sanger Project Score
*   **Version**: Project Score v2 (Combined Sanger/Broad)
*   **Portal**: [cellmodelpassports.sanger.ac.uk](https://cellmodelpassports.sanger.ac.uk/downloads)
*   **File**: `Project_score_combined_Sanger_v2_Broad_21Q2_fitness_scores_scaled_bayesian_factors_20250624.tsv`

## 7. PRISM Repurposing Screen
*   **Source**: DepMap PRISM Secondary Screen
*   **File**: `secondary-screen-dose-response-curve-parameters.csv`

---
**Note**: Ensure that all downloaded files are placed in the directory structure defined in `configs/pipeline_config.json`.
