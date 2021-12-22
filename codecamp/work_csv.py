import pandas as pd
import numpy as np

with open('btc-market-price.csv', 'r') as fp:
    for index, line in enumerate(fp.readlines()):
        # read the first 10 lines
        if(index < 10):
            print(index, line)

with open('btc-market-price.csv', 'r') as fp:
    for index, line in enumerate(fp.readlines()):
        # read the first 10 lines
        if(index < 10):
            timestamp, price = line.split(',')
            print(f"{timestamp}: ${price}")

# read csv file functions
#filepath
#sep
#header
#index_col
#names
#skiprows
#na_values
#dtype
#parse_dates
#date_parser
#nrows
#skip_footer
#encoding
#squeeze
#thousands
#decimal
#skip_blank_lines

# pd.read_csv?
csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
pd.read_csv(csv_url).head()
df = pd.read_csv(csv_url, header=None, na_values=['', '?', '-'])
df.head()
