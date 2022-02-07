ri.reach_conducted.mean()
ri.groupby('driver_gender').search_conducted.mean()

ri.groupby(['violation', 'driver_gender']).search_conducted_mean()

search_rate = ri.groupby(['violation', 'driver_gender']).search_conducted.mean()

type(search_rate)
type(search_rate.index)

# DataFrame -> normally 2 dimensions
# MultiIndex -> adds a third index

search_rate.loc['Equipment']
search_rate.loc['Equipment', 'M']
# Equipment row, Male column, to select a particular value in the Series

# converting a multi-indexed Series to a DataFrame
# if you Unstack the search_rate Series, it actually results in a DataFrame
search_rate.unstack()
# pivot table can create the same DataFrame
ri.pivot_table(index='violation', columns='driver_gender', values='search_conducted')

# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())

# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())

# Calculate the arrest rate for each 'violation' and 'rating'
print(ri_weather.groupby(['violation', 'rating']).is_arrested.mean())

# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate.loc['Moving violation', 'bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate.loc['Speeding'])

# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))
