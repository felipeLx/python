import pandas as pd
import os
import numpy as np

df_list = []

for file in os.listdir('met'):
  if file.endswith('.CSV'):
    df_value = pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=9, header=None, usecols=[0,1,2,3,6,7,15,17], index_col=None)
    df_value = df_value.rename(columns={0:'Data', 1: 'Hora', 2: 'Chuva (mm)', 3: 'Pres.Atm (hPa)', 6: 'Radiação (W/m2)', 7: 'Temp.Ar (°C)', 15: 'Humidade (%)', 17: 'Vel.Vento (m/s)'})

    df_value['Chuva (mm)'] = df_value['Chuva (mm)'].replace({',': '.'}, regex=True)
    df_value['Chuva (mm)'] = df_value['Chuva (mm)'].astype('float')
    df_value['Chuva (mm)'] = np.where(df_value['Chuva (mm)'] < 0, 0, df_value['Chuva (mm)'])

    df_value['Radiação (W/m2)'] = df_value['Radiação (W/m2)'].replace({',': '.'}, regex=True)
    df_value['Radiação (W/m2)'] = df_value['Radiação (W/m2)'].astype('float')
    df_value['Radiação (W/m2)'] = np.where(df_value['Radiação (W/m2)'] < 0, 0, df_value['Radiação (W/m2)'])

    df_value['Pres.Atm (hPa)'] = df_value['Pres.Atm (hPa)'].replace({',': '.'}, regex=True)
    df_value['Pres.Atm (hPa)'] = df_value['Pres.Atm (hPa)'].astype('float')
    df_value['Pres.Atm (hPa)'] = np.where(df_value['Pres.Atm (hPa)'] < 0, 0, df_value['Pres.Atm (hPa)'])

    df_value['Temp.Ar (°C)'] = df_value['Temp.Ar (°C)'].replace({',': '.'}, regex=True)
    df_value['Temp.Ar (°C)'] = df_value['Temp.Ar (°C)'].astype('float')
    df_value['Temp.Ar (°C)'] = np.where(df_value['Temp.Ar (°C)'] < 0, 0, df_value['Temp.Ar (°C)'])

    df_value['Humidade (%)'] = df_value['Humidade (%)'].replace({',': '.'}, regex=True)
    df_value['Humidade (%)'] = df_value['Humidade (%)'].astype('float')
    df_value['Humidade (%)'] = np.where(df_value['Humidade (%)'] == '', 0, df_value['Humidade (%)'])
    df_value['Humidade (%)'] = np.where(df_value['Humidade (%)'] < 0, 0, df_value['Humidade (%)'])

    df_value['Vel.Vento (m/s)'] = df_value['Vel.Vento (m/s)'].replace({',': '.'}, regex=True)
    df_value['Vel.Vento (m/s)'] = df_value['Vel.Vento (m/s)'].astype('float')
    df_value['Vel.Vento (m/s)'] = np.where(df_value['Vel.Vento (m/s)'] < 0, 0, df_value['Vel.Vento (m/s)'])

    df_value['Data'] = pd.to_datetime(df_value['Data'], yearfirst=True)
    df_value = df_value.set_index('Data')
    df_value['Data'] = df_value.index.strftime('%Y-%m-%d')
    df_value['Year'] = df_value.index.year
    df_value['Month'] = df_value.index.month

    df_value.reset_index(drop=True, inplace=True)
    df_list.append(df_value.values)

flat_list = [item for sublist in df_list for item in sublist]
df = pd.DataFrame(flat_list, columns=['Hora', 'Chuva (mm)', 'Pres.Atm (hPa)', 'Radiacao (W/m2)', 'Temp.Ar (C)', 'Humidade (%)', 'Vel.Vento (m/s)', 'Data', 'Ano', 'Mes'])

df.to_csv('RJ-rain-2010-2021.csv', sep=';', index=False)
print(df.head())