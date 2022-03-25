import pandas as pd
import os

df_list = []
for file in os.listdir('met'):
  if file.endswith('.CSV'):
    df_value = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=9, header=None, usecols=[0,1,2])
    df_value = df_value.rename(columns={0:'Date', 1: 'Hour', 2: 'Rain (mm)'})
    df_value.reset_index(drop=True, inplace=True)
   
    temp_df = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=2, nrows=5, header=None, usecols=[1])
    temp_df = pd.concat([temp_df.transpose()]*len(df_value), axis=0)
    temp_df = temp_df.rename(columns={0:'Region', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})
    temp_df.reset_index(drop=True, inplace=True)
    
    frames = [df_value, temp_df]
    df_join = pd.concat([df_value, temp_df], axis=1, ignore_index=True)
    df_join = df_join.rename(columns={0:'Date', 1: 'Time', 2: 'Rain (mm)', 3: 'Region', 4: 'Code', 5: 'Lat', 6: 'Lon', 7: 'Alt'})
    df_join['Rain (mm)'] = df_join['Rain (mm)'].replace('-9999', 0)
    df_join['Rain (mm)'] = df_join['Rain (mm)'].replace({',': '.'}, regex=True)
    df_join['Lat'] = df_join['Lat'].replace({',': '.'}, regex=True)
    df_join['Lon'] = df_join['Lon'].replace({',': '.'}, regex=True)
    df_join['Alt'] = df_join['Alt'].replace({',': '.'}, regex=True)
    df_join['Date'] = pd.to_datetime(df_join['Date'], yearfirst=True)
    df_join = df_join.set_index('Date')
    df_join['Year'] = df_join.index.year
    df_join['Month'] = df_join.index.month
    df_join['Rain (mm)'] = df_join['Rain (mm)'].astype('float')
    df_join.reset_index(inplace=True)
    df_join = df_join.groupby(['Region', 'Code', 'Lat', 'Lon', 'Alt', 'Year', 'Month'], as_index=False)['Rain (mm)'].sum()
    df_join.reset_index(drop=True, inplace=True)
    df_list.append(df_join.values)

flat_list = [item for sublist in df_list for item in sublist]

df = pd.DataFrame(flat_list, columns=['Region', 'Code', 'Lat', 'Lon', 'Alt', 'Year', 'Month', 'Rain (mm)'])
# print(df.head(15000))
df.to_csv('br_rain_2021.csv', sep=';', index=False)