import pandas as pd

df_vic = pd.read_csv('/home/felipelx/Downloads/test/seg_publica/vitimas.csv', sep=';', encoding='latin-1')
print(df_vic.head())
df_agg = df_vic.groupby(['UF', 'Tipo Crime', 'Ano', 'Mês'], as_index=False).agg({'Vítimas': 'sum'})

df_cases = pd.read_csv('/home/felipelx/Downloads/test/seg_publica/seg_pub.csv', sep=';', encoding='latin-1')
print(df_cases.head())
print(df_agg.head())

df_join = df_cases.join(df_agg.set_index(['UF', 'Tipo Crime', 'Ano', 'Mês']), on=['UF', 'Tipo Crime', 'Ano', 'Mês'])
df_join = df_join.replace(['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])

df_states = pd.read_csv('states_uf.csv', sep=';')
print(df_states.head(23))
df_join = df_join.join(df_states.set_index('UF'), on='UF')
print(df_join.head())
df_join.to_csv('/home/felipelx/Downloads/test/seg_publica/seg_pub_join.csv', sep=';', encoding='latin-1', index=False)
"""
df_join = pd.concat(df_join, df_states, on=['UF'])
"""