"""
ECDF = empirical cumulative distribution function

x-axis = quantity, percent of
y-axis = fraction of data points that have a value smaller than the corresponding x-value
"""

# x-axis is the sorted data
# numpy sorted
import numpy as np
x = np.sort(df_swing['dem_share'])
y = np.arange(1, len(x) + 1 ) / len(x)
_ = plt.plot(x, y, market='.', linestyle='none')
_ = plt.xlabel('percent of vote to Obama')
_ = plt.ylabel('ECDF')

plt.margins(0.02)
# choosing a value of point 0.02 gives a 2% buffer all around the plot
plt.show()

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Label the axes
_ = plt.ylabel('ECDF')
_ = plt.xlabel('percent of petals')

# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()