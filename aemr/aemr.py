import matplotlib as mpl
import matplotlib.pyplot as plt 
# %matplotlib inline
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf


sns.set_style("darkgrid")
mpl.rcParams['figure.figsize'] = (20,5)

df_raw = pd.read_csv('./DF_Raw_Data.csv')
df_std = pd.read_csv('./DF_Rolling_Stdev.csv')

# print(df_raw.describe())
# df_raw.info()
# print(df_std.describe())
# df_std.info()

df_raw.plot(kind='box')
df_std.plot(kind = 'box')
plt.title('Raw Dataframe Box Plot')

df_raw.plot(kind='line')
df_std.plot(kind='line')
_ = plt.title('Raw Dataframe Line Plot')

"""
. Dataframa Stdev have to much outliers with few registers inside the quartiles, while the Raw Dataframe is more  consistent with a perceptive median of the data. 
. Line plot show that while the variables is more descritive (more splited) the Std Dataframe the variations of the variables are more concentrated. 
"""

no_fail = df_raw["PUMP FAILURE (1 or 0)"] == 1
y_fail = df_raw["PUMP FAILURE (1 or 0)"] == 0
df_nofail = df_raw[no_fail]
df_yfail = df_raw[y_fail]

df_yfail.plot(kind='box')
df_nofail.plot(kind='box')
plt.title('Pump Failure Plot')

def pct25(column):
    return column.quantile(0.25)

def pct75(column):
    return column.quantile(0.75)

def iqr(f_quantile, t_quantile):
    return t_quantile - f_quantile

df_raw.reset_index(inplace=True)
df_pct25 = df_raw[["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Ambient Temperature", "Horse Power", "Pump Efficiency", "PUMP FAILURE (1 or 0)"]].agg(pct25)
df_pct75 = df_raw[["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Ambient Temperature", "Horse Power", "Pump Efficiency", "PUMP FAILURE (1 or 0)"]].agg(pct75)

df_iqr = iqr(df_pct25, df_pct75)
# print(df_iqr)

lower_Limit = df_pct25 - 1.5 * df_iqr
upper_Limit = df_pct75 + 1.5 * df_iqr

# Outliers = some_dataframe [ ((some_dataframe < Lower_Limit) | ((dataframe_raw > Upper_Limit))).any(axis=1) ]
outliers = df_raw[(( df_raw < lower_Limit) | (( df_raw > upper_Limit))).any(axis=1)]
insiders = df_raw[(~( df_raw < lower_Limit) | (~( df_raw > upper_Limit))).any(axis=1)]
# print(outliers.info())
# print(df_raw.info())

print('percentage remain:', (2453-95)/2453 * 100)
# print(df_iqr.info())
# df_wout_outlier = df_raw[~((outliers))]
insiders_one = insiders[insiders["PUMP FAILURE (1 or 0)"] == 1]
insiders_one.plot(kind="box")
insiders_zero = insiders[insiders["PUMP FAILURE (1 or 0)"] == 0]
insiders_zero.plot(kind="box")

listOfVariables = ["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Pump Torque", "Ambient Temperature", "Horse Power", "Pump Efficiency"]

for item in listOfVariables:
    first_axis = df_raw[item].plot(kind="line")
    second_axis = first_axis.twinx()
    second_axis.plot(df_raw[df_raw["PUMP FAILURE (1 or 0)"] == 0], color="teal")
    plt.title(item)
    plt.show()