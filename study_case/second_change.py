import pandas as pd
import os
import numpy as np

df_list = []

for file in os.listdir('met'):
  if file.endswith('.CSV'):
    df_value = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=9, header=None, usecols=[0,1,2], index_col=None)
    df_value = df_value.rename(columns={0:'Date', 1: 'Hour', 2: 'Rain (mm)'})
    df_value.reset_index(drop=True, inplace=True)
   
    temp_df = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=1, nrows=6, header=None, usecols=[1], index_col=None)
    temp_df = pd.concat([temp_df.transpose()]*len(df_value), axis=0)
    temp_df = temp_df.rename(columns={0:'State', 1:'Region', 2: 'Cod', 3: 'Lat', 4: 'Lon', 5: 'Alt'})
    temp_df.reset_index(drop=True, inplace=True)
    
    frames = [df_value, temp_df]
    df_join = pd.concat([df_value, temp_df], axis=1, ignore_index=True)
    df_join = df_join.rename(columns={0:'Date', 1: 'Time', 2: 'Rain (mm)', 3: 'State', 4: 'Region', 5: 'Code', 6: 'Lat', 7: 'Lon', 8: 'Alt'})

    df_join['Rain (mm)'] = df_join['Rain (mm)'].replace({',': '.'}, regex=True)
    df_join['Rain (mm)'] = df_join['Rain (mm)'].astype('float')
    df_join['Rain (mm)'] = np.where(df_join['Rain (mm)'] < 0, 0, df_join['Rain (mm)'])

    df_join['Lat'] = df_join['Lat'].replace({',': '.'}, regex=True)
    df_join['Lon'] = df_join['Lon'].replace({',': '.'}, regex=True)
    df_join['Alt'] = df_join['Alt'].replace({',': '.'}, regex=True)
        
    df_join['Date'] = pd.to_datetime(df_join['Date'], yearfirst=True)
    df_join = df_join.set_index('Date')
    df_join['Year'] = df_join.index.year
    df_join['Month'] = df_join.index.month
    df_join['Rain (mm)'] = df_join['Rain (mm)'].astype('float')
    df_join.reset_index(inplace=True)
    df_join = df_join.groupby(['State', 'Region', 'Code', 'Lat', 'Lon', 'Alt', 'Year', 'Month'], as_index=False)['Rain (mm)'].sum()
    df_join.reset_index(drop=True, inplace=True)
    df_list.append(df_join.values)

flat_list = [item for sublist in df_list for item in sublist]

df = pd.DataFrame(flat_list, columns=['State', 'Region', 'Code', 'Lat', 'Lon', 'Alt', 'Year', 'Month', 'Rain (mm)'])
# print(df.head(15000))
df.to_csv('br_rain_2010-2021.csv', sep=';', index=False)