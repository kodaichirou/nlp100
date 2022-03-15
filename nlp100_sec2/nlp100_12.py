import pandas as pd

df = pd.read_csv('./popular-names.txt', header=None, sep='\t',
                 names=['name', 'sex', 'number', 'year'])

col1 = df['name']
col1.to_csv('./col1.txt', index=False)
print(col1.head())#ncol output. standart is 5

col1 = df['sex']
col1.to_csv('./col2.txt', index=False)
print(col1.head())#ncol output. standart is 5