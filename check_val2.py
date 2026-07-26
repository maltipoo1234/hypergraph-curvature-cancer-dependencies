import pandas as pd
d = pd.read_parquet("results/tables/phase13_external_depmap_25q3_validation.parquet")
print("=== DepMap 25Q3 Validation ===")
print(d[["undirected_key", "external_gene_available", "external_num_mutant", "external_num_wildtype", "external_delta_dependency"]].to_string())
