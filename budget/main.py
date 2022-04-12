import pandas as pd

df = pd.read_csv('/home/felipelx/Downloads/budget_2022.csv', encoding='latin-1')

# process to clean and transform the data
df.columns = map(str.lower, df.columns)
df.columns = map(str.capitalize, df.columns)

df_clean = df.drop(['Nome órgão subordinado', 'Nome subfunção', 'Nome categoria econômica', 'Código órgão superior', 'Código órgão subordinado', 'Código unidade orçamentária', 'Código função', 'Código subfunção', 'Código programa orçamentário', 'Código ação', 'Código categoria econômica', 'Código grupo de despesa', 'Código elemento de despesa', 'Orçamento inicial (r$)', 'Nome função', 'Nome elemento de despesa', 'Nome grupo de despesa', 'Orçamento empenhado (r$)', 'Orçamento realizado (r$)'], axis=1)

df_clean['Nome unidade orçamentária'] = df['Nome unidade orçamentária'].str.lower()
df_clean['Nome programa orçamentário'] = df['Nome programa orçamentário'].str.lower()
df_clean['Nome ação'] = df['Nome ação'].str.lower()
df_clean = df_clean.rename(columns={'Exercício': 'Year', 'Nome órgão superior': 'Ministry', 'Nome unidade orçamentária': 'Unit', 'Nome programa orçamentário': 'Program_name', 'Nome ação': 'Action', 'Orçamento atualizado (r$)': 'Budget'})
df_clean['Ministry'] = df_clean['Ministry'].replace({'Advocacia-Geral da União': 'AGU', 'Banco Central do Brasil - Orçamento Fiscal e Seguridade Social': 'Banco Central', 'Controladoria-Geral da União': 'CGU', 'Ministério da Agricultura, Pecuária e Abastecimento': 'Agricultura', 'Ministério da Cidadania': 'Cidadania', 'Ministério da Ciência, Tecnologia, Inovações e Comunicações': 'Ciência', 'Ministério da Defesa': 'Defesa', 'Ministério da Economia': 'Economia', 'Ministério da Educação': 'Educação', 'Ministério da Infraestrutura': 'Infraestrutura', 'Ministério da Justiça e Segurança Pública': 'Justiça', 'Ministério da Mulher, Família e Direitos Humanos': 'Direitos Humanos', 'Ministério da Saúde': 'Saúde', 'Ministério das Comunicações': 'Comunicações', 'Ministério das Relações Exteriores': 'Relações Exteriores', 'Ministério de Minas e Energia': 'Minas e Energia', 'Ministério do Desenvolvimento Regional': 'Desenv.Regional', 'Ministério do Meio Ambiente': 'Meio Ambiente', 'Ministério do Trabalho': 'Trabalho', 'Ministério do Turismo': 'Turismo', 'Presidência da República': 'Presidência'})

# dataset group
df_group = df_clean.groupby(['Ministry', 'Unit'], as_index=False)['Budget'].sum().round(2)
df_group_action = df_clean.groupby(['Ministry', 'Action'], as_index=False)['Budget'].sum().round(2)
print(df_group.head())
df_group.to_csv('data_group.csv', index=False)
df_group_action.to_csv('data_group_action.csv', index=False)