import pandas as pd
import os

df_list = []

for file in os.listdir('places'):
  if file.endswith('.csv'):
    df = pd.read_csv(os.path.join('places', file), sep=';', encoding='utf-8').rename(columns={'Região/Unidade da Federação': 'Estado'}, inplace=False)
    df['mes'] = str(os.path.basename(file)).split('s')[2][:6]
    df = pd.melt(df, id_vars=['Estado', 'mes'], value_name='Qtde', var_name = 'Estabelecimentos')
    df_list.append(df.values)
 
flat_list = [item for sublist in df_list for item in sublist]
df = pd.DataFrame(flat_list, columns=['Estado', 'Mês', 'Estabelecimentos', 'Qtde'])
df.to_csv('places.csv', index=False)
print(df.head())