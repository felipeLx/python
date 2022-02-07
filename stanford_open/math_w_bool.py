# math with boolean values
ri.isnull().sum()
# to count the missing values in each column

# take the mean of a boolean series
ri.is_arrested.value_counts(normalize=True)

# numpy
ri.is_arrested.mean()

# comparing groups using groupby
    # study the arrest rate by police district
ri.district.unique()

ri[ri.district == 'Zone K1'].is_arrested.mean()

ri.groupby('district').is_arrested.mean()

# by multiple categories
ri.groupby(['district', 'driver_gender']).is_arrested.mean()
ri.groupby(['driver_gender', 'district']).is_arrested.mean()

# investing the order the calculation is the same but the presentation of the results will be diff
# Check the data type of 'search_conducted'
print(ri.search_conducted.dtype)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())

# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())

# Calculate the search rate for both groups simultaneously
print(ri.groupby(ri.driver_gender).search_conducted.mean())

# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation','driver_gender']).search_conducted.mean())

# does gender affect who is frisked during a search
ri.search_conducted.value_counts()
# output
    # False 83229
    # True 3307

ri.search_type.value_counts(dropna = False)
# .values_counts -> excludes missing values by default
# (dropna = False) -> display missing values

# multiple values are separated by commas
ri['inventory'] = ri.search_type.str.contains('Inventory', na = False)
# str.contains() return True if string is found, False if not found
# na = False -> returns False when its finds a missing value

# calculating the inventory rate
searched = ri[ri.search_conducted == True]
searched.inventory.mean()

# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())
