import pandas as pd
import numpy as np
import glob

count_file_df = 0
count_file_df1 = 0

path = './met'
all_files = glob.glob(path + "/*.CSV")

li = []
li1 = []

for file in all_files:
    df1_temp = pd.read_csv(file, sep=';', encoding='latin1', skiprows=9)
    df1_temp = df1_temp[['DATA (YYYY-MM-DD)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']].rename(columns={'DATA (YYYY-MM-DD)': 'Date', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'Rain (mm)'})
        
    df1_temp['Rain (mm)'] = df1_temp['Rain (mm)'].replace('-9999', 0)
    df1_temp['Rain (mm)'] = df1_temp['Rain (mm)'].replace({',': '.'}, regex=True)
        
    df1_temp['Date'] = pd.to_datetime(df1_temp['Date'], yearfirst=True)
    df1_temp = df1_temp.set_index('Date')
    df1_temp['Year'] = df1_temp.index.year
    df1_temp['Month'] = df1_temp.index.month
        
    df1_temp['Rain (mm)'] = df1_temp['Rain (mm)'].astype('float')
    df1_temp.reset_index(drop=True, inplace=True)
    print(df1_temp.head())
    df1 = pd.concat([df1_temp])
    count_file_df1 += 1
    print('df1', count_file_df1)

    df_temp = pd.DataFrame()
    df_temp = pd.read_csv(file, sep=';', encoding='latin1', skiprows=1, nrows=5).transpose()
    df_temp.reset_index(drop=True, inplace=True)
    count_file_df += 1
    print('df', count_file_df)

    df_temp = pd.DataFrame(np.repeat(df_temp.values[1:], len(df1_temp), axis=0))
    df_temp = df_temp.rename(columns={0:'Região', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})
    print(df_temp.head())
    df = pd.concat([df_temp])

frames = [df, df1]
df_join = pd.DataFrame(pd.concat(frames, axis = 1, join='inner'))
print(df.head(19))
df_join = df_join.groupby(['Região', 'Lat', 'Lon', 'Alt', 'Year', 'Month'])['Rain (mm)'].sum()


print(len(df1))
# print(df_join.info())
print(df.head(20))
print(df_join.head(20))
