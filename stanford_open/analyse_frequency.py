# computing a frequency table
# crosstab()

pd.crosstab(ri.driver_race, ri.driver_gender)
# frequency table as a tally of how many times each combination of values ocurrs in the dataset
# case above, tells us how many rows contain each combination of race and gender

ri[(ri.driver_race == 'Asian') & (ri.driver_gender == 'F')].shape
# driver_race along index
# driver_gender along the columns

table = pd.crosstab(ri.driver_race, ri.driver_gender)

# .loc[] -> accessor allows you to select portions of a DataFrameby label
n_table = table.loc['Asian': 'Hispanic']
n_table.plot(kind="bar")
plt.show()

# sckater bar plot:
n_table.plot(kind="bar", stacked=True)

# Create a frequency table of districts and violations
print(pd.crosstab(ri.district, ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district, ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc["Zone K1":"Zone K3"])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc["Zone K1":"Zone K3"]

# Create a bar plot of 'k_zones'
k_zones.plot(kind="bar")

# Display the plot
plt.show()

# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind="bar", stacked=True)

# Display the plot
plt.show()