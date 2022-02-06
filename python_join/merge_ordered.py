# merge_ordered()
"""
this method can merge time-series and other ordered data

method comparison

.merge()
-> Column(s) to join: on, left_on, right_on
-> Type(s) of join: how (left, right, inner, outer)
-> default inner
-> Overlaping: suffixes
-> df1.merge(df2)

merge_ordered()
-> Column(s) to join: on, left_on, right_on
-> Type(s) of join: how (left, right, inner, outer)
-> default outer
-> Overlaping: suffixes
-> pd.merge_ordered(df1, df2)
"""

import pandas as pd

appl = pd.DataFrame({
    "date": ["2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01"],
    "close": [12.0871,13.2871,14.3871,17.0871,17.2871]
})

mcd = pd.DataFrame({
    "date": ["2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01"],
    "close": [44.0871,43.2871,45.3871,48.0871,50.2871]
})

appl_mcd = pd.merge_ordered(appl, mcd, on="date", suffixes=("_appl", "_mcd"))
print(appl_mcd)

# fill missing with previous value

appl_mcd = pd.merge_ordered(appl, mcd, on="date", suffixes=("_appl", "_mcd"), fill_method="ffill")
print(appl_mcd)


# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())

"""
You can see the different aspects of merge_ordered() and how you might use it on data that can be ordered. By using this function, you were able to fill in the missing data from 2019. Finally, the correlation of 0.21 between the GDP and S&P500 is low to moderate at best. You may want to find another predictor if you plan to play in the stock market.
"""