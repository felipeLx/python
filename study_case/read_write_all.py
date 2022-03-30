import pandas as pd
import glob
import os

df = pd.DataFrame()

files = glob.glob("./csv_ready/*.csv")

df = [pd.read_csv(f, sep=';', encoding='latin1', header=0) for f in files]

df_join = pd.concat(df, ignore_index=True)
df_join.to_csv('br_rain_2010-2021.csv', sep=';', index=False)
