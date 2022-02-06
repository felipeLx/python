# pandas method for selection data from the table called the query() method
"""
.query('SOME SELECTION STATEMENT')

1) accepts an input string
    input string used to determine what rows are returned
    input string similar to statement after WHERE clause in SQL statement
        a. prior knowledge of SQL is not necessary
"""
stock.query('nike > 90')
stock.query('nike > 90  and disney < 140')

stock.query('nike > 90  or disney < 140')

stock.query('stock=="disney"or (stock === "nike" and close < 90)')

social_fin.query('financial == "net_income" and value < 0')

##############
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()