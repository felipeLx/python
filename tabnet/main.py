import pandas as pd

df = pd.read_csv('assets/equipamentos.csv', sep=';', encoding='utf-8').rename(columns={'Região/Unidade da Federação': 'Estado'}, inplace=False)
df = pd.melt(df, id_vars=['Estado'], value_name='Qtde Equipamentos', var_name = 'Equipamentos')
df['Estado'] = df['Estado'].map(lambda x: x.lstrip('..').strip())
df['Equipamentos'] = df['Equipamentos'].map(lambda x: x.lstrip('..').strip())

df1 = pd.read_csv('assets/equipes.csv', sep=';', encoding='utf-8').rename(columns={'Região/Unidade da Federação': 'Estado'}, inplace=False)
df1 = pd.melt(df1, id_vars=['Estado'], value_name='Qtde Equipes', var_name = 'Equipes')
df1['Estado'] = df1['Estado'].map(lambda x: x.lstrip('..').strip())
df1['Equipes'] = df1['Equipes'].map(lambda x: x.lstrip('..').strip())

df2 = pd.read_csv('assets/estabelecimentos.csv', sep=';', encoding='utf-8').rename(columns={'Região/Unidade da Federação': 'Estado'}, inplace=False)
df2 = pd.melt(df2, id_vars=['Estado'], value_name='Qtde Estabelecimentos', var_name = 'Estabelecimentos')
df2['Estado'] = df2['Estado'].map(lambda x: x.lstrip('..').strip())
df2['Estabelecimentos'] = df2['Estabelecimentos'].map(lambda x: x.lstrip('..').strip())

df3 = pd.read_csv('assets/procedimentos.csv', sep=';', encoding='utf-8').rename(columns={'Região/Unidade da Federação': 'Estado'}, inplace=False)
df3 = pd.melt(df3, id_vars=['Estado'], value_name='Qtde Procedimentos', var_name = 'Procedimentos')
df3['Estado'] = df3['Estado'].map(lambda x: x.lstrip('..').strip())
df3['Procedimentos'] = df3['Procedimentos'].map(lambda x: x.lstrip('..').strip())

df.to_csv('equipamentos.csv', sep=';', encoding='utf-8', index=False)
df1.to_csv('equipes.csv', sep=';', encoding='utf-8', index=False)
df2.to_csv('estabelecimentos.csv', sep=';', encoding='utf-8', index=False)
df3.to_csv('procedimentos.csv', sep=';', encoding='utf-8', index=False)