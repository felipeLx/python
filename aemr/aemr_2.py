import matplotlib as mpl
import matplotlib.pyplot as plt 
# %matplotlib inline
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df_std = pd.read_csv("./DF_Rolling_Stdev.csv")
# df_std.info()

df_std.set_index(['TIMEFRAME (DD/MM/YYYY)'], inplace=True)

listOfVariables = ["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Ambient Temperature", "Horse Power", "Pump Efficiency"]

for item in listOfVariables:
    first_axis = df_std[item].plot(kind="line")
    first_axis.xaxis.set_major_locator(plt.MaxNLocator(10))
    second_axis = first_axis.twinx()
    second_axis.plot(df_std["PUMP FAILURE (1 or 0)"], color="orange")
    second_axis.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.title(item)
#    plt.show()

df_time_filtered = df_std[(df_std.index >= "10/12/2014 12:00") & (df_std.index <= "10/12/2014 14:30")]

df_raw = pd.read_csv("./DF_Raw_Data.csv")
corr_df_raw = df_raw.corr()
# sns.heatmap(corr_df_raw, annot=True)
fig, ax = plt.subplots()

corr_desc_raw = corr_df_raw.sort_values('PUMP FAILURE (1 or 0)', ascending=False)
ax.bar(corr_desc_raw.index, corr_desc_raw['PUMP FAILURE (1 or 0)'])
ax.set_xticklabels(corr_desc_raw.index, rotation=90)
ax.set_facecolor("#CCCCCC")
ax.grid(visible=True, axis='both', color="w")
plt.title('Correlated Bar Plot (Raw Data)')
plt.show()