"""
i) Create a new column in the dataframe_stdev, called, 'Prediction'.     
ii) Use the regression equation you created in the previous step and apply the .predict() function to the independent variables in the dataframe_stdev dataset so you get a column full of your regressive predictions.
iii) Create a Dual-Axis Plot with the following axes items: <p>
        Axes One would contain: Volumetric Flow Meter 2, Pump Efficiency and Horse Power 
        Axes two would contain: Pump Failure (1 or 0) and Prediction
"""
import matplotlib.pyplot as plt 
import pandas as pd
import statsmodels.api as sm

df_std = pd.read_csv('./DF_Rolling_Stdev.csv')
print(df_std.info())
ind_var = df_std[["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", "Pump Speed (RPM)", "Ambient Temperature", "Horse Power", "Pump Efficiency"]]
dep_var = df_std["PUMP FAILURE (1 or 0)"]
ind_var = sm.add_constant(ind_var)

regression_model = sm.OLS(dep_var, ind_var).fit()
df_std["prediction"] = regression_model.predict(ind_var)
first_axis = df_std[["Volumetric Flow Meter 2", "Pump Efficiency", "Horse Power"]].plot(kind="line")
second_axis = first_axis.twinx()
second_axis.plot(df_std[["PUMP FAILURE (1 or 0)", "prediction"]], color="teal")
plt.xticks(range(len(df_std["TIMEFRAME (DD/MM/YYYY)"])), df_std["TIMEFRAME (DD/MM/YYYY)"])
plt.title("Regressive Equation Plot")
plt.show()