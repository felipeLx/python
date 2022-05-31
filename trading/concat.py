import pandas as pd

df = pd.read_csv("/home/felipelx/Downloads/voters.csv")

df = df.groupby(["Estado", "Sexo", "Grupo"], as_index=False)["Quantidade"].sum()
df.to_csv("/home/felipelx/Downloads/voters_agg.csv")
"""
df0 = pd.read_csv("/home/felipelx/Downloads/part0.csv", header=None)
df1 = pd.read_csv("/home/felipelx/Downloads/part1.csv", header=None)
df2 = pd.read_csv("/home/felipelx/Downloads/part2.csv", header=None)
df3 = pd.read_csv("/home/felipelx/Downloads/part3.csv", header=None)
df4 = pd.read_csv("/home/felipelx/Downloads/part4.csv", header=None)
df = pd.concat([df0, df1, df2, df3, df4], ignore_index=True)
df.columns = ['Estado', 'Sexo', 'Grupo', 'Quantidade']
df.to_csv("/home/felipelx/Downloads/voters.csv")
"""