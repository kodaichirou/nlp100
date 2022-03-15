import pandas as pd

df = pd.read_csv('./popular-names.txt', header=None, sep='\t',
                 names=['name', 'sex', 'number', 'year'])
print(len(df))
print(df)
