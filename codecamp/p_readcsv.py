import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

df = pd.read_csv('./sales_data.csv', header=0)
df.head()
df.index
df.tail(3) # the last 3 rows of the DataFrame

df.plot()
grph = plt.plot(df.index, df['Profit'])
# the first parameters is the value of X and Y axis
grph

df_btc = pd.read_csv(
    './btc-market-price.csv',
    header = None,
    names = ['Timestamp', 'Price'],
    index_col = 0,
    parse_dates = True
)

prices = pd.DataFrame(index = df_btc.index)
plt.plot(df_btc.index, df_btc['Price'])

df_btc.plot(figsize=(16, 9), title='BTC price 2017-2018')
# print(n_prices)