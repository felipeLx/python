# special attribute .dt

"""
apple.dtypes
apple.date_and_time.dt.month

* other similar attrib available, such as week, dayofweek, hour, minute
"""
apple.set_index('date_and_time', inplace=True)
apple.index
        # to access date attributes
apple.index.month

# calculating the monthly mean price
apple.price.mean()
monthly_price = apple.groupby(apple.index.month).price.mean()

# plot the monthly_price
import matplotlib.pyplot as plt
monthly_price.plot()
"""
    Line plot: Series index on x-axis, Series value on y-axis
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.title("Monthly mean stock price for Apple")
"""

import matplotlib.pyplot as plt


# Create a line plot of 'hourly_arrest_rate'
hourly_arrest_rate.plot(kind="line")

# Add the xlabel, ylabel, and title
plt.xlabel("Hour")
plt.ylabel("Arrest Rate")
plt.title("Arrest Rate by Time of Day")

# Display the plot
plt.show()
