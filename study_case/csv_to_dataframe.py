import pandas as pd
import glob
import os
import numpy as np

path = './met' # use your path
all_files = glob.glob(os.path.join(path, "*.CSV")) 

df_value = (pd.read_csv(f, sep=';', encoding='latin1', skiprows=8, header=0, usecols=[0,1,2], index_col=False) for f in all_files)
c_df_value = pd.concat(df_value, ignore_index=True, axis=0, join='outer')

for i in range(0,len(c_df_value)):
    c_df_value['index'] = i
    
c_df_value = c_df_value[['DATA (YYYY-MM-DD)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']].rename(columns={'DATA (YYYY-MM-DD)': 'Date', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'Rain (mm)'})
        
c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].replace('-9999', 0)
c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].replace({',': '.'}, regex=True)
        
c_df_value['Date'] = pd.to_datetime(c_df_value['Date'], yearfirst=True)
c_df_value = c_df_value.set_index('Date')
c_df_value['Year'] = c_df_value.index.year
c_df_value['Month'] = c_df_value.index.month

c_df_value['Rain (mm)'] = c_df_value['Rain (mm)'].astype('float')
c_df_value.reset_index(drop=True, inplace=True)
# print(c_df_value.head(15000))

df = pd.DataFrame()
df = (pd.read_csv(f, sep=';', encoding='latin1', skiprows=2, nrows=5, header=None, index_col=False, usecols=[1]) for f in all_files)
df2 = pd.concat(df, ignore_index=True, axis=0, join='outer')
df2 = df2.transpose()
df2 = pd.DataFrame(np.repeat(df2.values[0:], repeats=8760, axis=0), index=None)
df2 = pd.DataFrame(df2.values.reshape(-1, 5))

print(df2.head(10))
df2 = df2.rename(columns={0:'Region', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})
unique_cols = df2.columns.unique().tolist()
new_df = pd.DataFrame(
        df2.values.reshape((-1, len(unique_cols)), order='C'),
        columns=unique_cols
    )
# print(new_df.head(15000))
# df_new = pd.wide_to_long(df2, i=-1, j='index', stubnames=[0,1,2,3,4])

#print(df_new.head(15000))

# df1 = pd.concat(pd.DataFrame(np.repeat(df, repeats=8760, axis=0)), ignore_index=True, axis=0, join='outer')

"""
for i in range(0,len(df1)):
    df1['index'] = i
    
print(df1.head(10))
df_sum = (pd.read_csv(f, sep=';', encoding='latin1', skiprows=2, header=None, nrows=5, usecols=[1]) for f in all_files)
df_t_sum = list(df_sum)

for i in range(0, len(df_t_sum)):
    df_t_sum[i] = df_t_sum[i].transpose()
    new_df = pd.DataFrame(np.repeat(df_t_sum[i], 8760, axis=0), index=None)
    print(new_df.head(10))

c_df_sum = pd.concat([df_sum]*8760, ignore_index=True, axis=0, join='outer')
print(c_df_sum.head(10))
c_df_sum = pd.DataFrame(c_df_sum.values.reshape(len(c_df_value), 5))
# df = pd.concat([df_sum]*8760)
# print(c_df_sum.head())
df = df.rename(columns={0:'Region', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt'})
unique_cols = df.columns.unique().tolist()
new_df = pd.DataFrame(
        df.values.reshape((-1, len(unique_cols))),
        columns=unique_cols
    ).sort_values(by=df.index , ascending=True)


# df_new = df_new.rename(columns={'Region':'Region', 'Cod': 'Lat', 2: 'Lat', 3: 'Lon', 4: 'Alt'})
# print(new_df.head(5))


for i in range(0,len(df)):
    df['index'] = i


# print(new_df.values)

new_df.reset_index(drop=True, inplace=True)
# print(new_df.head())
frames = [new_df, c_df_value]

df_join = pd.concat(frames, ignore_index=True, sort=False, axis=1) 
df_join = df_join.rename(columns={0:'Region', 1: 'Cod', 2: 'Lat', 3: 'Lon', 4: 'Alt', 5: 'Rain (mm)', 6: 'Year', 7: 'Month'})
df_join = df_join.groupby(['Region', 'Cod', 'Lat', 'Lon', 'Alt', 'Year', 'Month'], as_index=False)['Rain (mm)'].sum()


# print(df_join)
# print(df_agg)
"""