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

"""
# When PUMP FAILURE (1 or 0) is 1 the data of the variable is much more concentrated, almost is not possible to identify the median.
# When PUMP FAILURE (1 or 0) is 0 it's interisting to look the Pump Torque whithin perfect quartile and median.
# What call attention also is the Pump Speed that is very similar for both cases, that give us an understand that this variable don't is impacted.
"""

"""
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

def pct30(column):
    return column.quantile(0.3) # computes the thirtieth percentile of a DataFrame column.

# now we can subset the weight column and call dog-agg, passing in the name of your function, pct30
dogs["weight_kg"].agg(pct30)

# summarize multiple columns
dogs[["weight_kg", "height"]].agg(pct30)

def pct40(column):
    return column.quantile(0.4)

# will return thirtieth and fortieth percentiles of the dogs weights
dogs["weight_kg"].agg([pct30, pct40])
"""

"""
### Step 5: <span style="color:green">Create Quartiles</span> 

Create two new variables called Q1 and Q3 using the dataframe_raw dataset. 

i)  <b> Q1 should contain the 25th percentile for all columns in the DataFrame. Q3 should contain the 75th percentile  for all the columns in the DataFrame.</b>

You may want to use the .quantile() function explained <a href = https://www.geeksforgeeks.org/python-pandas-dataframe-quantile/> here. </a> 

ii) After defining Q1 and Q3, calculate the interquartile range **(IQR = Q3 - Q1)** for all columns in the DataFrame and print it to the screen.

Volumetric Flow Meter 1     2.09
Volumetric Flow Meter 2     2.13
Pump Speed (RPM)           12.00
Pump Torque                24.00
Ambient Temperature         5.00
Horse Power                 0.56
Pump Efficiency             3.91
PUMP FAILURE (1 or 0)       0.00
"""
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

"""
1. Define a list variable called ListOfVariables; this is to contain the column names of all the **numerical** variables you wish to iterate through in the dataframe_raw dataset <p>

2. Instantiate your for loop with the following syntax: 
       
    
    for item in ListOfVariables:
        first_axis = dataframe[___].plot #Looping through every item in the dataframe.
        second_axis = first_axis.twinx() #The Twinx function is used to ensure we share the X-Axis for both plots
        second_axis.plot(dataframe['ColumnOfInterest'], color='teal')
        plt.title(item)
        plt.show()
        
<b> i) Using the syntax provided, loop through the dataframe_raw dataset, plotting every variable individually, against the Pump Failure to better identify trends. </b>

**Note:** For each plot, ensure that you have a dual axis set up so you can see the Pump Failure (0 or 1) on the second Y-axis, and the attribute on the first Y-Axis. 

"""
listOfVariables = ["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Pump Torque", "Ambient Temperature", "Horse Power", "Pump Efficiency"]

for item in listOfVariables:
    first_axis = df_raw[item].plot(df_raw[df_raw["PUMP FAILURE (1 or 0)"] == 1])
    second_axis = first_axis.twinx()
    second_axis.plot(df_raw[df_raw["PUMP FAILURE (1 or 0)"] == 0], color="teal")
    plt.title(item)
    plt.show()