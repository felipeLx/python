import pandas as pd

df = pd.read_csv('/home/felipelx/Downloads/real_state.csv', header=0)
print(df.head())
print(df.info())

print(df['Included'].values)