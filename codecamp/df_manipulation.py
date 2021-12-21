import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 30, np.nan],
    'B': [2, 8, 31, np.nan],
    'C': [np.nan, 9, 32, 100],
    'D': [5, 8, 34, 110],
})

df.shape

df.isnull()
df.dropna()
df.dropna(axis = 1)

df2 = pd.DataFrame({
    'A': [1, np.nan, 30],
    'B': [2, np.nan, 31],
    'C': [np.nan, np.nan, 100],
})

# df2.dropna(how = 'all') #(how = 'any')
df_notna = df2.dropna(thresh=1, axis='columns')
print(df_notna)

# filling the null values
s = pd.Series([1,2,3, np.nan, np.nan, 4])
s_notNa = s.fillna(0)
print(s_notNa)

s.fillna(s.mean())

# fill with other values close to that null value
s.fillna(method='ffill') # (method='bfill')

# works with DataFrame
df_nota = df2.fillna(method='ffill', axis=0) # 0 to column 1 to row
print(df_nota)