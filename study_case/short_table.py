import pandas as pd
import glob
import os
import numpy as np

path = './met' # use your path
all_files = glob.glob(os.path.join(path, "*.CSV")) 

df_value = (pd.read_csv(f, sep=';', encoding='latin1', skiprows=8, header=0, usecols=[0,1,2], index_col=False) for f in all_files)
c_df_value = pd.concat(df_value, ignore_index=True, axis=0, join='outer')

c_df_value = c_df_value[['DATA (YYYY-MM-DD)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']].rename(columns={'DATA (YYYY-MM-DD)': 'Date', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'Rain (mm)'})
        
c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].replace('-9999', 0)
c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].replace({',': '.'}, regex=True)
        
c_df_value['Date'] = pd.to_datetime(c_df_value['Date'], yearfirst=True)
c_df_value = c_df_value.set_index('Date')
c_df_value['Year'] = c_df_value.index.year
c_df_value['Month'] = c_df_value.index.month

c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].astype('float')
c_df_value.reset_index(inplace=True)
print(c_df_value.index)
df_list = []
for file in os.listdir('met'):
  if file.endswith('.CSV'):
    temp_df = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=2, nrows=5, header=None, usecols=[1])
    temp_df = pd.concat([temp_df.transpose()]*8760, axis=0, join='outer')
    
    df_list.append(temp_df)
new_df = pd.DataFrame(pd.concat(df_list, axis=0, join='outer'))
new_df[2] = new_df[2].replace({',': '.'}, regex=True)
new_df[3] = new_df[3].replace({',': '.'}, regex=True)
new_df[4] = new_df[4].replace({',': '.'}, regex=True)

print(new_df.index)
frames = [new_df, c_df_value]

# df_join = pd.concat(frames, axis=1, ignore_index=False) 
# df_join = pd.merge(c_df_value, new_df, on=c_df_value.index, kind="left")
df_join = new_df.join(c_df_value, how='outer')

df_join = df_join.rename(columns={0:'Region', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt', 5: 'Rain (mm)', 6: 'Year', 7: 'Month'})
df_join = df_join.groupby(['Region', 'Cod', 'Lat', 'Lon', 'Alt', 'Year', 'Month'], as_index=False)['Rain (mm)'].sum()

df_join.to_csv('brazil_rain_2010.csv', sep=';', encoding='utf-8')
print(df_join.head(48))