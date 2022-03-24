import pandas as pd
import numpy as np
import os

# df = pd.read_csv('./met/')
count_file_df = 0
count_file_df1 = 0
df = pd.DataFrame()
df1 = pd.DataFrame()
newdf = pd.DataFrame()

for file in os.listdir('met'):
    if file.endswith('.CSV'):
        df1 = pd.concat([df1.reset_index(drop=True, inplace=True), pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=8)])
        df1 = df1[['DATA (YYYY-MM-DD)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']].rename(columns={'DATA (YYYY-MM-DD)': 'Date', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'Rain (mm)'})
        
        df1['Rain (mm)'] = df1['Rain (mm)'].replace('-9999', 0)
        df1['Rain (mm)'] = df1['Rain (mm)'].replace({',': '.'}, regex=True)
        
        df1['Date'] = pd.to_datetime(df1['Date'], yearfirst=True)
        df1 = df1.set_index('Date')
        df1['Year'] = df1.index.year
        df1['Month'] = df1.index.month
        
        df1['Rain (mm)'] = df1['Rain (mm)'].astype('float')
        df1.reset_index(drop=True, inplace=True)
        count_file_df1 += 1
        print('df1', count_file_df1)

        df = pd.concat([df.reset_index(drop=True, inplace=True), pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=1, nrows=5)]).transpose()
        df.reset_index(drop=True, inplace=True)
        count_file_df += 1
        print('df', count_file_df)

        df = pd.DataFrame(np.repeat(df.values[1:], len(df1), axis=0))
        df = df.rename(columns={0:'Região', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})

frames = [df, df1]
df_join = pd.concat(frames, axis = 1, join='inner') 
df_join = df_join.groupby(['Região', 'Lat', 'Lon', 'Alt', 'Year', 'Month'])['Rain (mm)'].sum()


# print(len(df1))
print(df_join.info())
# print(df1.head(10))
