# mergin datasets
apple
apple.reset_index(inplace=True)

high_low
high = high_low[['DATE', 'HIGH']]
high

apple_high = pd.merge(left=apple, right=high, left_on='date',right_on='DATE', how='left')
# left=apple -> Left DataFrame
# right=high -> Righ DataFrame
# left_on='date' -> Key column in left DataFrame
# right_on='DATE' -> Key column in right DataFrame
# how='left' -> type of join

# Reset the index of 'ri'
ri.reset_index(inplace=True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE', 'rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())

# Examine the shape of 'ri'
print(ri.shape)

# Merge 'ri' and 'weather_rating' using a left join
ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

# Examine the shape of 'ri_weather'
print(ri_weather.shape)

# Set 'stop_datetime' as the index of 'ri_weather'
ri_weather.set_index('stop_datetime', inplace=True)
