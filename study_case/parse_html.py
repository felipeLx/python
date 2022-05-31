import pandas as pd

# df = pd.read_html("https://www.contextures.com/xlsampledata01.html#data")
df = pd.read_html("https://en.unesco.org/themes/safety-journalists/observatory/country/223729"+"?max_rows=10000")
print(df[1].head(5))
print(df[1].info())
print(df[1].describe())

df = df[1]

# df.to_csv("file2.csv", sep=';')