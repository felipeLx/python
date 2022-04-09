import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/home/felipelx/Downloads/budget_2022.csv', encoding='latin-1')

# process to clean and transform the data
df.columns = map(str.lower, df.columns)
df.columns = map(str.capitalize, df.columns)

df_clean = df.drop(['Nome unidade orçamentária', 'Nome ação', 'Nome programa orçamentário', 'Nome órgão subordinado', 'Nome subfunção', 'Nome categoria econômica', 'Código órgão superior', 'Código órgão subordinado', 'Código unidade orçamentária', 'Código função', 'Código subfunção', 'Código programa orçamentário', 'Código ação', 'Código categoria econômica', 'Código grupo de despesa', 'Código elemento de despesa', 'Orçamento inicial (r$)', 'Nome função', 'Nome elemento de despesa', 'Nome grupo de despesa', 'Orçamento empenhado (r$)', 'Orçamento realizado (r$)'], axis=1)

df_clean = df_clean.rename(columns={'Exercício': 'Year', 'Nome órgão superior': 'Ministry', 'Orçamento atualizado (r$)': 'Budget'})
# print(df_clean.columns)
data_group_df = df_clean.groupby(['Year', 'Ministry'], as_index=False)['Budget'].sum().round(2)
# data_group_df.to_csv('data_group_by_ministry.csv', index=False)
data_group_df['Ministry'] = data_group_df['Ministry'].replace({'Advocacia-Geral da União': 'AGU', 'Banco Central do Brasil - Orçamento Fiscal e Seguridade Social': 'Banco Central', 'Controladoria-Geral da União': 'CGU', 'Ministério da Agricultura, Pecuária e Abastecimento': 'Agricultura', 'Ministério da Cidadania': 'Cidadania', 'Ministério da Ciência, Tecnologia, Inovações e Comunicações': 'Ciência', 'Ministério da Defesa': 'Defesa', 'Ministério da Economia': 'Economia', 'Ministério da Educação': 'Educação', 'Ministério da Infraestrutura': 'Infraestrutura', 'Ministério da Justiça e Segurança Pública': 'Justiça', 'Ministério da Mulher, Família e Direitos Humanos': 'Direitos Humanos', 'Ministério da Saúde': 'Saúde', 'Ministério das Comunicações': 'Comunicações', 'Ministério das Relações Exteriores': 'Relações Exteriores', 'Ministério de Minas e Energia': 'Minas e Energia', 'Ministério do Desenvolvimento Regional': 'Desenv.Regional', 'Ministério do Meio Ambiente': 'Meio Ambiente', 'Ministério do Trabalho': 'Trabalho', 'Ministério do Turismo': 'Turismo', 'Presidência da República': 'Presidência'})
data_group_df.plot.bar(x='Ministry', y='Budget')
plt.show()