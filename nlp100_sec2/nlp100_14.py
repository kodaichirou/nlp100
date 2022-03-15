import pandas as pd

df = pd.read_csv('./popular-names.txt', header=None, sep='\t',
                 names=['name', 'sex', 'number', 'year'])

def output_head(N):
  print(df.head(N))

output_head(5)
