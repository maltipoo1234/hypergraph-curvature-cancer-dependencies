import pandas as pd
import numpy as np

s = pd.read_parquet("results/tables/phase13_external_cmp_sanger_validation.parquet")
print("=== Sanger Validation ===")
print(s[["undirected_key", "mutation_type", "external_gene_available", "external_num_mutant", "external_delta_dependency"]])
