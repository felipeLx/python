# handle missing data with Pandas
import pandas as pd
import numpy as np

# identify null values (4 functions)
pd.isnull(np.nan) #pd.notnull(None)
pd.isnull(None) #pd.notnull(3)
pd.isna(np.nan) #pd.notnull(np.man)
pd.isna(None) #pd.notna(3)

# with Serie and DataFrame
pd.isnull(pd.Series([1, np.nan, 7]))

s = pd.Series([1,2,3, np.nan, np.nan, 4])
pd.notnull(s)
pd.notnull(s).sum()
s[pd.notnull(s)]

# different aproach that return the value notnull
s[s.notnull()]
s.dropna()
