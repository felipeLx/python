import numpy as np
import pandas as pd
import requests
# mport xlswriter
import math

df = pd.read_csv('/home/felipelx/Downloads/supermarket_sales.csv')
print(df.head())
print(df.columns)
df_fact = df[["Invoice ID", "Unit price", "Quantity", "Tax 5%", "Total", "cogs", "gross income"]]
df_dimension = df[["Invoice ID", "Branch", "City", "Customer type", "Gender", "Product line", "Date", "Time", "Payment", "gross margin percentage", "Rating"]]
print(df_fact.head())
print(df_dimension.head())
