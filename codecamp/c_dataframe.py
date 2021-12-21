import pandas as pd
import numpy as np

# dataframe looks like excel table
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523],
    'GDP': [1785387, 2833687, 3874437, 2167744, 4602367, 2950039, 17348875],
    'Surface area': [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
    'HDI': [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
}, columns = ['Population', 'GDP', 'Surface area', 'HDI', 'Continent'])



df.index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']
df.info()

# !functions: info(), describe(), shape, dtypes, dtypes.value_counts()

# will transform the range of data in a Serie
df.loc['Canada'] # by index
df.iloc[-1] # by index position
df['Population'] # by column

df.loc['France': 'Italy'] # from France to Italy (included)
df.loc['France': 'Italy', 'Population']
df.iloc[1:3] # the row 3 is NOT included
df.iloc[1:3, 2]

df_pop = df.loc[df['Population'] > 70, ['Population', 'GDP']]

# function DROP will delete your Serie
df.drop(['Population', 'GDP'], axis = 1)

# modify DataFrame
# add new column
langs = pd.Series(
    ['French', 'German', 'Italian'],
    index = ['France', 'Germany', 'Italy'],
    name = 'Language'
)
df['Language'] = langs

# rename column
# saved in other variable because df is imutable
df_alter = df.rename(
    columns = {
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index= {
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    }
)

#radical index changes
# df.reset_index()
# df.set_index('Population')

# Create column from other column
df[['Population', 'GDP']]
# create a Serie that can be use in dataframe
df['GDP per capita'] = df['GDP'] / df['Population']

# Statical info
df.head()
df.describe()
population = df['Population']
population.min(), population.max()
population.sum()
population.sum() / len(population)
population.mean()
population.std()
population.median()
population.describe()
population.quantile(.25)
population.quantile(.2, .4, .6, .8, .11)