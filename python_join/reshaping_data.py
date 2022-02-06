# melt -> the method will unpivot table from wide to long format
"""
first / last / height / weight
John    Doe     5.5      130
Mary    Bo      6.0      150
to

first / last / variable / value
John     Doe    height     5.5
Mary     Bo     height     6.0
John     Doe    weight     130
Mary     Bo     weight     150

"""
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'])
print(social_fin_tall.head(10))

# id_vars : columns to be used as identifier variables
    # columns in our original dataset that we do not want to change

"""
melting with value_vars
"""
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'])

# melting with column names
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'], var_name=['year'], value_name='dollars')

# var name will allow us to set the name of the year column in the output

inflation.melt(id_vars=['country', 'indicator'], value_vars=['2017', '2018', '2019'],var_name='year', value_name='annual')

# unpivot everything besides the year column
print(ur_wide.head(10))

ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')


# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values("date")

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate', kind='scatter')
plt.show()

"""
This increase is likely the effect of the COVID-19 pandemic and its impact on shutting down most of the US economy. In general, data is often provided (especially by governments) in a format that is easily read by people but not by machines. The .melt() method is a handy tool for reshaping data into a useful form.
"""

print(ten_yr.head(10))

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on="date", how="inner", suffixes=('_dow', '_bond'))


# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow','close_bond'], x='date', kind='bar', rot=90)
plt.show()
