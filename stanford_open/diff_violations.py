# counting unique values
"""
.value_counts() : counts the unique values in a Serie

. best suited for categorical data
    ri.stop_outcome.value_counts()
"""
# to sum of a series by simply adding the sum() method on the end
ri.stop_outcome.value_counts().sum()
# outcome: 86536

# the sum() of the value_counts() is actually equal to the number of rows in the DataFrame
# which will be the case for any Series that has no missing values

ri.shape
# outcome: (86536, 3)

ri.stop_outcome.value_counts()

# express counts as proportions
ri.stop_outcome.value_counts(normalize=True)

white = ri[ri.driver_race == 'White']

# comparing stop outcomes for 2 groups
white.stop_outcome.value_counts(normalize=True)

# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))

# Create a DataFrame of female drivers
female = ri[ri['driver_gender'] == 'F']

# Create a DataFrame of male drivers
male = ri[ri['driver_gender'] == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize=True))
