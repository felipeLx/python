from turtle import onclick
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_html("https://www.numbeo.com/cost-of-living/city-history/in/Rio-De-Janeiro", index_col=0)
url = "https://www.numbeo.com/cost-of-living/city-history/in/Rio-De-Janeiro"

dfs = pd.read_html(url, header=0, index_col=0)
df_all = pd.concat(dfs[1:], axis=1)
df_all.to_csv("rj_cost_life.csv")
print(df_all.head())
"""
for i in range(14):
    result = pd.concat([dfs[i], dfs[i+1]], axis=1)
    print(result)
# print(dfs)
"""
"""
print(len(df))
for table in df:
    df_all = pd.concat(table.iloc[0:len(table)])
"""