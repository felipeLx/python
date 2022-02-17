"""
### Step 13: <span style="color:purple">Use OLS Regression</span> 
<b> i) Using the OLS Regression Model in the statsmodel.api library, create a regression equation that models the Pump Failure (Y-Variable) against all your independent variables in the dataframe_raw dataset. </b>

<b> Don't forget to reimport the DataFrames you've previously imported in Step 2 before starting these steps </b> 

    1. Establish two DataFrames named, independent_variables and dependent_variables. The independent variables are known as explanatory variables - they help EXPLAIN what you are trying to model. Dependent Variable on the other hand is the variable of interest that you want to MODEL. In this case, the Dependent Variable is Pump Failure (1 or 0).
    
    2. Add a constant to your Independent Dataframe via the following syntax:
    independent_variables = sm.add_constant(independent_variables). This will simply add a constant stream of 1's in a column to your dataframe. This constant is used to account for bias in the model.  
    
    3. Store and Fit your model with the below syntax:
    regression_model = sm.OLS(dependent_variable,independent_variable).fit() 
    
    4. Print the regression_model.summary() to view the Regression Statistics 


<b> ii) Repeat i) but this time use the dataframe_stdev you imported previously.</b>

You will repeat the same steps as you have done in i) only you will be changing the dataset from dataset_raw to dataset_stdev. 
"""
import matplotlib as mpl
import matplotlib.pyplot as plt 
# %matplotlib inline
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df_raw = pd.read_csv('./DF_Raw_Data.csv')
df_std = pd.read_csv('./DF_Rolling_Stdev.csv')

ind_var = df_std[["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Ambient Temperature", "Horse Power", "Pump Efficiency""]]
dep_var = df_std["PUMP FAILURE (1 or 0)"]
ind_var = sm.add_constant(ind_var)

regression_model = sm.OLS(dep_var, ind_var).fit()
regression_model.params[0:].plot(x=ind_var, y=dep_var, kind="bar", title='Regressive coeficient for Pump Failure')
plt.show()