import pandas as pd

df = pd.read_csv("./df_brics.csv", sep=";")

# 1) Data Cleanning
df.fillna(0)


# 1.a) Data Check
df_indicator = df.groupby("Indicator Code")["Indicator Name"]

df_chn = df[df["Country Code"] == "CHN"]
"""
Used before, will not be considerate before the Data Transformation
df_bra = df[df["Country Code"] == "BRA"]
df_zaf = df[df["Country Code"] == "ZAF"]
df_ind = df[df["Country Code"] == "IND"]
df_rus = df[df["Country Code"] == "RUS"]
"""
# to check the indicators
ch_ind = df_chn["Indicator Name"].unique()

# check Length of the Indicator for each country
print('china ', len(ch_ind))

# extract the indicator to csv to check one by one the most relevants
df_chn.to_csv("china.csv")

"""
After check the china.csv file in Excel was considered the most relavant Indicators, also that have values,
was missing information about Education where at least in china.csv have to many empty values.

From 1443 Indicators was selected 26
"""

# 2) Data Transformation
indicator_selected = pd.read_csv("./column_selected.csv")

df = df[df["Indicator Name"].isin(indicator_selected)]

indicators = df["Indicator Name"]
# print(indicators)

df_cleaned = df[["Country Name", "Country Code", "Indicator Name", "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]]
print(df_cleaned.info())
# df_cleaned.to_csv("df_cleaned.csv")