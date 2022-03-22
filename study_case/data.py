import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_expfunction.csv')

print(df.info())
# print(df.describe)

# fig, ax = plt.subplots()
sns.relplot(x="Year", y="Qty_barrel_per_avg_region", data=df, kind="line", style="sub_region", hue="sub_region")
# ax.bar(df["sub_region"], df["Qty_barrel_per_avg_region"])
# ax.set_xlabel("World by region")
# ax.set_ylabel("How much barrel can be bought by Average minimum wage")
# ax.bar("sub_region", df["Qty_barrel_per_avg_region"].mean(), yerr=df["Qty_barrel_per_avg_region"].std())
plt.show()

'''
# df_transf = df.melt(id_vars=["Country_code", "continent", "sub_region", "Unit_Code"], var_name="Year", value_name="Value")

# print(df_transf.info())

df_mean_region = df.pivot_table("Value", ["Year", "sub_region"]).reset_index()
df_mean_continent = df.pivot_table("Value", ["Year", "continent"]).reset_index()


df["mean_region"] = df.groupby(["Year", "sub_region"])["Value"].mean()
df["mean_continent"] = df.groupby(["Year", "continent"])["Value"].mean()

print(df.head(5))
'''