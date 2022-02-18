import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./df_cleaned.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df_transf = df.melt(id_vars=["Country Name", "Country Code", "Indicator Name"], var_name="Year", value_name="Value")

df_ready = df_transf.pivot_table("Value", ["Country Name", "Country Code", "Year"], "Indicator Name").reset_index()

df_ready.to_csv('prepared_data.csv')
# print(df.head(5))
# print(df_transf.head(5))
print(df_ready.head(5))
print(df_ready.info())

df_chn = df_ready[df_ready["Country Code"] == "CHN"]
df_bra = df_ready[df_ready["Country Code"] == "BRA"]
df_ind = df_ready[df_ready["Country Code"] == "IND"]
df_rus = df_ready[df_ready["Country Code"] == "RUS"]
df_zaf = df_ready[df_ready["Country Code"] == "ZAF"]

df_chn.to_csv('chn_data.csv')
df_bra.to_csv('bra_data.csv')
df_ind.to_csv('ind_data.csv')
df_rus.to_csv('rus_data.csv')
df_zaf.to_csv('zaf_data.csv')

# plt.show()
"""
df_ready["GDP per capita growth (annual %)"].plot(kind="bar")
fig, ax = plt.subplots()
ax.plot(df_ready[["Country Code", "Year"]], df_ready["GDP per capita growth (annual %)"], color="blue")
ax2 = ax.twinx()
ax2.plot(df_ready[["Country Code", "Year"]], df_ready["Forest area (% of land area)"], color="red")
plt.show()

fig, ax = plt.subplots()
ax.plot(df_ready["Country Name"], df_ready["GDP per capita growth (annual %)"], color="blue")
ax2 = ax.twinx()
ax2.plot(df_ready.index, df_ready["Forest area (% of land area)"], color="red")
plt.show()

# index_col=("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"))
print(df.head(5))

# the 26 indicator selected
indicators = ["Access to electricity (% of population)",	"Adjusted net national income (annual % growth)",	"Age dependency ratio (% of working-age population)",	"Agricultural land (% of land area)",	"Air transport, passengers carried",	"Broad money (% of GDP)",	"Cereal production (metric tons)",	"CO2 emissions (kt)",	"Consumer price index (2010 = 100)",	"Current account balance (% of GDP)",	"Electric power consumption (kWh per capita)",	"Employers, total (% of total employment) (modeled ILO estimate)",	"Forest area (% of land area)",	"GDP per capita (current US$)",	"GDP per capita growth (annual %)",	"GNI per capita growth (annual %)",	"Gross capital formation (% of GDP)",	"Individuals using the Internet (% of population)",	"Inflation, consumer prices (annual %)",	"Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)",	"Mortality rate, under-5 (per 1,000 live births)",	"People using at least basic sanitation services, urban (% of urban population)",	"Population ages 15-64 (% of total population)",	"Population growth (annual %)",	"Unemployment, total (% of total labor force) (national estimate)",	"Urban population"
]

columns = ["China", "Brazil", "India", "South Africa", "Rusia"]

palette_color = {"China": "red", "Brazil": "green", "India": "white", "South Africa": "black", "Rusia": "blue"}

df.groupby("Country Name").plot(kind="bar")


fig, ax = plt.subplots()
ax.plot(df[df["Country Name"].isin(columns) ], df[df["Indicator Name"] == "GDP per capita (current US$)"], color="blue")
ax2 = ax.twinx()
ax2.plot(df.index, df[df["Indicator Name"] == "Forest area (% of land area)"], color="red")

plt.show()

df_plot = pd.DataFrame(years, index=df["Indicator Name"].index, columns=columns)
df_plot = df_plot.cumsum()
plt.figure(); df_plot.plot(); plt.legend(loc="best")
plt.show()


for name, data in df_transf.groupby("Country Name"):
    plt.plot(data["Year"], data[data["Indicator Name"] == "GDP per capita (current US$)"], label=name)

plt.xlabel("Years")
plt.ylabel("GDP per capita")
plt.legend()
plt.show()

for i in indicators:
    for year in years:
        sns.relplot(x=df[df[year]], y=df[df["Indicator Name"] == i], data=df, kind="bar", palette=palette_color)
        plt.show()

"""