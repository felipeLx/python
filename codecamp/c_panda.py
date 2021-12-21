# the most important librart to Data Analyst
import pandas as pd
import numpy as np

g7pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7pop)

# like a list in Python, Series create index
g7pop[0] # to access specific index in the array

g7pop.name = "G7 population in Million"

# define value to index will looks more a Dictonary
g7pop.index = [
    "Canada",
    "France",
    "Germany",
    "Italy",
    "Japan",
    "United Kingdom",
    "United State",
]

print(g7pop["Japan"])

# can access the position by iloc
g7pop.iloc[0] # first
g7pop.iloc[-1] # last

g7pop[g7pop > 70] # filter values of the array

# ~ not  | or  & and