# build a DatetimeIndex
"""
date    stop_time
"2005-01-04 16:00

date -> object
stop_time -> object
"""
apple.date.str.replace('/','-')

# concat
combined = apple.date.str.cat(apple.time, ' ')
apple['date_and_time'] = pd.to_datetime(combined)
apple.set_index('date_and_time', inplace=True)

print(apple.index)

# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, ' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)