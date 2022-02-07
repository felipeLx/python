weather[['AWND', 'WSF2']].head()
weather[['AWND', 'WSF2']].describe()
weather[['AWND', 'WSF2']].plot(kind='box')
plt.show()
# box plot, repsents the 25% through 75% percentiles, and the lines below and above the box
# represent the minimum and maximum values, excluding the outliers represented by circles.

# out goal is to simply to validate that the data looks reasonable

# creating a histogram
weather['WDIFF'] = weather.WSF2 - weather.AWND
weather.WDIFF.plot(kind='hist')
plt.show()

# no value below zero -> good
# make the shape more clear by changing the number of histogram bins to 20
# normal distribution -> sign that the dataset is trustworthy
# Read 'weather.csv' into a DataFrame named 'weather'
weather = pd.read_csv('weather.csv')

# Describe the temperature columns
print(weather[['TMIN', 'TAVG', 'TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN', 'TAVG', 'TMAX']].plot(kind='box')

# Display the plot
plt.show()

# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF'] = weather['TMAX'] - weather['TMIN']

# Describe the 'TDIFF' column
print(weather.TDIFF.describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather.TDIFF.plot(kind='hist', bins=20)

# Display the plot
plt.show()