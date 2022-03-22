import pandas as pd
import os

# df = pd.read_csv('./met/')

df = pd.DataFrame()

for file in os.listdir('met'):
    if file.endswith('.CSV'):
        df = pd.concat([df, pd.read_csv(os.path.join('met', file), sep=';', encoding='latin1', skiprows=1, nrows=5)])

df.reset_index(drop=True, inplace=True)

print(df.head(10))