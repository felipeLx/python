# visualizing Linear Relationship

# some data stored as numpy arrays x and y that we want to plot
import matplotlib.pyplot as plt

plt.plot(x, y, 'r-o')
#'r-o' -> plot style: r to Red, - to solid line, o to round data point marker
plt.show()

# object interface
    # more customizable, and for complex plots, easier to use
fig, ax = plt.subplots()

# prepare initial style options
options = dict(marker = 'o', color='blue')

line = ax.plot(x, y, **options)
# ** -> unpacking to transform the dictionary key-value

# modify axis object with the set methods
_ = ax.set_ylabel('Times')
_ = ax.set_xlabel('Distances')
plt.show()

# visualizing linear data
    # two points:
    # (x1, y1) = (0,0)
    # (x2, y2) = (2,3)
dy = (y2 - y1) = 3 - 0
dx = (x2 - x1) = 2 - 0

    # slope = rise-over-run
slope = dy/dx = 3/2

    # intercept
    # when x = 0; y1 = 0

# Plot line using the axis.plot() method
line = axis.plot(times , distances , linestyle=" ", marker="o", color="red")

# Use the plt.show() method to display the figure
plt.show()

# Pass times and measured distances into model
model_distances = model(times, measured_distances)

# Create figure and axis objects and call axis.plot() twice to plot data and model distances versus times
fig, axis = plt.subplots()
axis.plot(times, measured_distances, linestyle=" ", marker="o", color="black", label="Measured")
axis.plot(times, model_distances, linestyle="-", marker=None, color="red", label="Modeled")

# Add grid lines and a legend to your plot, and then show to display
axis.grid(True)
axis.legend(loc="best")
plt.show()

# Look at the plot data and guess initial trial values
trial_slope = 1
trial_intercept = 2

# input thoses guesses into the model function to compute the model values.
xm, ym = model(trial_intercept, trial_slope)

# Compare your your model to the data with the plot function
fig = plot_data_and_model(xd, yd, xm, ym)
plt.show()

# Repeat the steps above until your slope and intercept guess makes the model line up with the data.
final_slope = 1
final_intercept = 2