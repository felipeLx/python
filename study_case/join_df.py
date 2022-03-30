import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df_rain = pd.read_csv('br_rain_2010-2021.csv', sep=';', encoding='latin1')

df_disaster = pd.read_csv('disasters_2013-2021.csv', sep=';', encoding='latin1')

# filter the months with the highest rain insident
months_rain = [1,2, 3, 12]
df_rain = df_rain.loc[df_rain['Month'].isin(months_rain)] 
df_disaster = df_disaster.loc[df_disaster['Month'].isin(months_rain)]

df = pd.merge(df_rain, df_disaster, on=['State', 'Year', 'Month'], how='inner')
print(df.head())
df['Disasters'] = df['Disasters'].astype('float')

df.to_csv('df_rain_disaster.csv', sep=';', index=False)

# df_cov = df['Rain (mm)'] + df['Disasters']
cov_matrix = np.cov(df['Rain (mm)'], df['Disasters'], rowvar=True)
print(cov_matrix)



def pearson_r(x, y):
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0, 1]

r = pearson_r(df['Rain (mm)'], df['Disasters'])
print(r)


ind_var = df['Rain (mm)']
dep_var = df['Disasters']
ind_var = sm.add_constant(ind_var)

regression_model = sm.OLS(dep_var, ind_var).fit()
regression_model.params[0:].plot(x=ind_var, y=dep_var, kind='bar', title='Regressive coeficient for Disasters')
plt.show()

# pearson considering all months of the Rain dataser: 0.1224
# pearson considering only the months with the highest rain insident: 0.13688