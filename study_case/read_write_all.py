import pandas as pd
import glob
import os

df = pd.DataFrame()

for file in os.listdir('csv_ready'):
  if file.endswith('.csv'):
    df = pd.concat([df, pd.read_csv(os.path.join('csv_ready', file), sep=';', encoding='latin1', header=0)])
    df.to_csv('br_rain_2010-2021.csv', sep=';', index=False)
print(df.info())