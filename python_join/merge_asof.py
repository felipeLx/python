# merge_asof : its similar to merge_ordered() left join
# will match on the nearest value columns rather than equal values
    # merged "on" columns must be sorted

pd.merge_asof(visa, ibm, on="date_time", suffixes=('_visa', '_ibm'))

pd.merge_asof(visa, ibm, on=["date_time"], suffixes=('_visa', '_ibm'), direction="forward")

"""
data sampled from a process
developing a training set (no data leakage)
"""
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', 
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', 
                              suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()

"""
merge_asof() function is very useful in performing the fuzzy matching between the timestamps of all the tables
"""
# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()

"""
merge_asof() allowed you to quickly add a flag to the gdp dataset by matching between two different dates, in one line of code! If you were to perform the same task using subsetting, it would have taken a lot more code.
"""