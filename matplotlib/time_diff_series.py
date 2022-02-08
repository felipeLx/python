# values of different variables, we might want to plot them on the same axes
import pandas as pd

climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

ax.plot(climate.index, climate['co2'])

ax.set_xlabel('Time')
ax.set_ylabel('CO2 / relative temp')

# will use the same x-axis, but different y-axis
ax2 = ax.twinx()

ax2.plot(climate.index, climate['relative_temp'])
ax2.set_ylabel('Relative temperature')
plt.show()

# to separate the variables, we'll encode each one with a different color
ax.plot(climate.index, climate['co2'], color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('CO2', color='blue')

ax2 = ax.twinx()

ax2.plot(climate.index, climate['relative_temp'], color='red')
ax2.set_ylabel('Relative temperature', color='red')
plt.show()

# color of the y-axis labels but also the y-axis ticks and the y-axis tick labels
ax.tick_params('y', colors='blue')
# take y or x as its first argument, pointing to the fact we are modifying the parameters of the
# y-axis ticks and tick labels
ax2.tick_params('y', colors='red')

# use a function to be reusable
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
