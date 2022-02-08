# .yplot used for convention
import matplotlib.pyplot as plt

# subplots create 2 plots
fig, ax = plt.subplots()

# Figure object is a container that holds everything that you see on the page
# Axis is the part of the page that holds the data
    # its is the canvas on which we will draw with our data, to visualize it
ax.plot(s_weather["MONTH"], s_weather["MLY-TAVG-NORMAL"])
plt.show()

# can add other curve adding other plot to ax
ax.plot(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"])

# marker which indicate that you are interested in adding markets to the plot
ax.plot(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"], marker='o')
# marker='v' -> ger markers shaped like triangles pointing downwards
# all options: https://marplotlib.org/api/markers_api.html

# linestyle
ax.plot(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"], marker='o', linestyle='--')
# linestyle = 'None' -> will show just the points, no line

# color
ax.plot(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"], marker='o', linestyle='--', color='r')
# to red line

# other customize: axis labels
ax.set_xlabel("Time (months)")

# plot have many methods that start with set: can use to change certain properties of the object
ax.set_ylabel("Average temperature (Fahrenheit degrees")
ax.set_title("Weather in Seattle")

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], marker='o', color='b', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], marker='v', color='r', linestyle='--')

# Call show to display the resulting plot
plt.show()