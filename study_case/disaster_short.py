import pandas as pd
import os

df_value = []
for file in os.listdir('disasters'):
  if file.endswith('.csv'):
    df = pd.read_csv(os.path.join('disasters', file), sep=';', engine='python', encoding='latin1', skiprows=4, header=None, usecols=[1,2,11])    
    df.dropna(axis=0, inplace=True)
    print(df.head(3))
    df = df.rename(columns={1:'State', 2: 'Disasters', 11: 'Date'})
    df['Date'] = df['Date'].astype('str')
    df.reset_index(drop=True, inplace=True)
    
    df['Year'] = df['Date'].str.split('/').str[2].astype('str')
    df['Month'] = df['Date'].str.split('/').str[1].astype('str')
    df['period'] = df[['Month', 'Year']].agg('-'.join, axis=1)
    df = df.groupby(['State', 'period', 'Year', 'Month'], as_index=False)['Disasters'].count()
    df.reset_index(drop=True, inplace=True)
    df_value.append(df.values)

flat_list = [item for sublist in df_value for item in sublist]

df = pd.DataFrame(flat_list, columns=[ 'State', 'Period', 'Year', 'Month', 'Disasters'])

df.to_csv('disasters_2013-2021.csv', sep=';', index=False)