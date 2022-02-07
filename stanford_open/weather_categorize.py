weather.shape
weather.columns

temp = weather.loc[:, 'TAVG':'TMAX']
temp.shape
temp.columns
temp.head()
temp.sum()
temp.sum(axis='columns').head()

ri.stop_duration.unique()
mapping = {
    '0-15 Min': 'short',
    '16-30 Min': 'medium',
    '30+ Min': 'long'
}

ri['stop_length'] = ri.stop_duration.map(mapping)
ri.stop_length.unique()

# category type stores the data more efficiently
# allows you to specify a logical order for the categories

ri.stop_length.memory_usage(depp=True)

# change data type from object to category
cats = ['short', 'medium', 'long']
ri['stop_length'] = ri.stop_length.astype('category', ordered=True, categories=cats)

# after categorizing can sort the data
ri[ri.stop_length > 'short'].shape
ri.groupby('stop_length').is_arrested.mean() 

# Copy 'WT01' through 'WT22' to a new DataFrame
WT = weather.loc[:,'WT01':'WT22']

# Calculate the sum of each row in 'WT'
weather['bad_conditions'] = WT.sum(axis='columns')

# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# Create a histogram to visualize 'bad_conditions'
weather['bad_conditions'].plot(kind='hist')

# Display the plot
plt.show()

# Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad', 
        5:'worse', 6:'worse', 7:'worse', 8:'worse', 9:'worse',}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())

# Create a list of weather ratings in logical order
cats = ['good', 'bad', 'worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category', ordered=True, categories=cats)

# Examine the head of 'rating'
print(weather.rating.head())