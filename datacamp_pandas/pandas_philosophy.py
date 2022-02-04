""" 
There should be one -- and preferably only one -- obvious way to do it.
""" 
import pandas as pd

df = pd.DataFrame({"region": ["East", "Pacific","Mountain","West","Pacific"],
                 "state": ["Alabama","Alaska","Arizona","Arkansas","California"],
                 "individuals": [2570.0, 1434.0, 7259.0, 2280.0, 109008.0],
                 "family_members": [864.0, 582.0,2606.0,432.0,20964.0], 
                 "state_pop": [4887681, 735139, 7158024, 3009733, 39461588]})

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.values)
print(df.columns)
print(df.index)
