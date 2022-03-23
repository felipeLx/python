import pandas as pd
import numpy as np
import os

# df = pd.read_csv('./met/')

df = pd.DataFrame()
df1 = pd.DataFrame()

for file in os.listdir('met'):
    if file.endswith('.CSV'):
        df1 = pd.concat([df1, pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=8)])
        df1 = df1[['DATA (YYYY-MM-DD)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']].rename(columns={'DATA (YYYY-MM-DD)': 'Date', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'Rain (mm)'})
        
        df1['Rain (mm)'] = df1['Rain (mm)'].replace('-9999', 0)
        df1['Rain (mm)'] = df1['Rain (mm)'].replace({',': '.'}, regex=True)
        
        df1['Date'] = pd.to_datetime(df1['Date'], yearfirst=True)
        df1 = df1.set_index('Date')
        df1['Year'] = df1.index.year
        df1['Month'] = df1.index.month
        
        df1['Rain (mm)'] = df1['Rain (mm)'].astype('float')
        df1.reset_index(drop=True, inplace=True)

        df = pd.concat([df, pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=1, nrows=5)]).transpose()
        newdf = pd.DataFrame(np.repeat(df.values[1:], len(df1), axis=0))
        newdf = newdf.rename(columns={0:'Região', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})

        frames = [newdf, df1]
        df_join = pd.concat(frames, axis = 1, join='inner') 
        df_join = df_join.groupby(['Região', 'Lat', 'Lon', 'Alt', 'Year', 'Month'])['Rain (mm)'].sum().reset_index()
        

# print(len(df1))
print(df_join.head(12))
# print(df1.head(10))
