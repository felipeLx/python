# translate string to analyzed numerically

# analyse an object column 
# ex. how ofter the price go up
# -> create boolean column that is True if the price went up and False otherwise
"""
when we need to map one set of values to another, you can use Series map() method
Dictonary maps the values you have to the values you want
"""
mapping = {'up': True, 'down': False}
apple['is_up'] = apple.change.map(mapping)

apple.is_up.mean()

#visualize how often searches were done after each violation
ri.groupby('violation').search_conducted.mean()
# -> return a Series that is sorted in alphabetical order by violation
search_rate = ri.groupby('violation').search_conducted.mean()
# Print the unique values in 'stop_duration'
print(ri.stop_duration.unique())

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min': 8, '16-30 Min': 23, '30+ Min': 45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Print the unique values in 'stop_minutes'
print(ri.stop_minutes.unique())
search_rate.plot(kind='bar')
plt.show()

# ordering the bars -> from left to right
search_rate.sort_values()
search_rate.sort_values().plot(kind='bar')
search_rate.sort_values().plot(kind='barh')

# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()