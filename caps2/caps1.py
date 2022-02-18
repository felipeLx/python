import pandas as pd

df = pd.read_csv('../../../../Downloads/WDIData.csv')

brics_country_code = ["BRA", "RUS", "ZAF", "CHI", "IND"]

df_caps = pd.DataFrame()

df_caps = df[df["Country Code"].isin(["BRA", "RUS", "ZAF", "CHN", "IND"])]

df_caps = df_caps[["Country Name", "Country Code", "Indicator Name", "Indicator Code", "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]]

df_caps.to_csv('df_brics.csv', sep=';', encoding='utf-8')
print(df_caps.info())
print(df_caps.head(10))