import pandas as pd
df = pd.read_excel("/Users/jiyunlee/Desktop/project/curvature/data_external/tcga/TCGA-CDR-SupplementalTableS1.xlsx", sheet_name="TCGA-CDR")
print(df.columns.tolist()[:30])
