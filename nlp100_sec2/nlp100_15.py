import pandas as pd

df = pd.read_csv('./popular-names.txt', header=None, sep='\t',
                 names=['name', 'sex', 'number', 'year'])

def output_tail(N):
  print(df.tail(N))

output_tail(5)
