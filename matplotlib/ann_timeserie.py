# one important way to enhance a visualization is to add annotations
import matplotlib.pyplot as plt

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)

fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'],
                'blue', 'Time', 'CO2 (ppm)')
ax2 = ax.twinx()

plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'],
                'red', 'Time', 'Relative temperature (Celsius)')

# when we find a point out of the plot
ax2.annotate(">1 degree", xy=[pd.TimeStamp("2015-10-06"), 1])

# position the annotation
ax2.annotate(">1 degree", xy=(pd.TimeStamp("2015-10-06"), 1),
                xytext=(pd.TimeStamp("2008-10-06"), -0.2))

# adding arrows to annotation
ax2.annotate(">1 degree", xy=(pd.TimeStamp("2015-10-06"), 1),
                xytext=(pd.TimeStamp("2008-10-06"), -0.2),
                arrowprops={})

# if we pass an empty dictionary into the key-world argument, the arrow will have the default properties, as show here

# customize arrow properties
ax2.annotate(">1 degree", xy=(pd.TimeStamp("2015-10-06"), 1),
                xytext=(pd.TimeStamp("2008-10-06"), -0.2),
                arrowprops={"arrowstyle":"->", "color":"gray"})

# https://matplotlib.org/users/annotations.html

# exercise
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate('>1 degree', xy=(pd.Timestamp('2015-10-06'), 1))

plt.show()

fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temp (Celsius)")

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={"arrowstyle":"->", "color":"gray"})

plt.show()