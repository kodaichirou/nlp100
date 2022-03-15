import pandas as pd

col1 = pd.read_table('./col1.txt')
col2 = pd.read_table('./col2.txt')
merged_1_2 = pd.concat([col1, col2], axis=1)
merged_1_2.to_csv('./merged_1_2.txt', sep='\t', index=False)
print(merged_1_2.head())