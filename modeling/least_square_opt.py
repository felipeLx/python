"""
Minima of RSS
    Setting RSS slope = zero, and some calculus yields:
    a1 = covariance(x,y)/variance(x)
the result is that you can compute the optimized slope as the ratio of the covariance and the variance
    a0 = mean(y) - a1 x mean(x)
we can compute the optimized intercept as the mean of y minus the slope times the mean of x
"""
# implement of Numpy
x_mean = np.mean(x)
y_mean = np.mean(y)

x_dev = x - x_mean
y_dev = y - y_mean

a1 = np.sum(x_dev * y_dev)/np.sum(x_dev**2)
a0 = y_mean - (a1*x_mean)

from scipy import optimize
# optimize module can solve more general optimization problems, not just least-squares
x_data, y_data = load_data()

def model_func(x, a0, a1):
    return a0 + (a1*x)

param_opt, param_cov = optimize.curve_fit(model_func, x_data, y_data)

a0 = param_opt[0] # intercept
a1 = param_opt[1] # slope

# optimized by statsmodels
from statsmodels.formula.api import ols

x_data, y_data = load_data()
df = pd.DataFrame(dict(x_name=x_data, y_name=y_data))

model_fit = ols(formula="y_name ~ n_name", data=df).fit()
# statement of the form 'y is proportional to x', using the column names from the DataFrame
y_model = model_fit.predict(df)
x_model = x_data

a0 = model_fit.params['Intercept']
a1 = model_fit.params['x_name']

# prepare the means and deviations of the two variables
x_mean = np.mean(x)
y_mean = np.mean(y)
x_dev = x - x_mean
y_dev = y - y_mean

# Complete least-squares formulae to find the optimal a0, a1
a1 = np.sum(x_dev * y_dev) / np.sum( np.square(x_dev) )
a0 = y_mean - (a1 * x_mean)

# Use the those optimal model parameters a0, a1 to build a model
y_model = model(x, a0, a1)

# plot to verify that the resulting y_model best fits the data y
fig, rss = compute_rss_and_plot_fit(a0, a1)

"""
Notice that the optimal slope a1, according to least-squares, is a ratio of the covariance to the variance. Also, note that the values of the parameters obtained here are NOT exactly the ones used to generate the pre-loaded data (a1=25 and a0=150), but they are close to those. Least-squares does not guarantee zero error; there is no perfect solution, but in this case, least-squares is the best we can do.
"""
# Define a model function needed as input to scipy
def model_func(x, a0, a1):
    return a0 + (a1*x)

# Load the measured data you want to model
x_data, y_data  = load_data()

# call curve_fit, passing in the model function and data; then unpack the results
param_opt, param_cov = optimize.curve_fit(model_func, x_data, y_data)
a0 = param_opt[0]  # a0 is the intercept in y = a0 + a1*x
a1 = param_opt[1]  # a1 is the slope     in y = a0 + a1*x

# test that these parameters result in a model that fits the data
fig, rss = compute_rss_and_plot_fit(a0, a1)

# Pass data and `formula` into ols(), use and `.fit()` the model to the data
model_fit = ols(formula="y_column ~ x_column", data=df).fit()

# Use .predict(df) to get y_model values, then over-plot y_data with y_model
y_model = model_fit.predict(df)
fig = plot_data_with_model(x_data, y_data, y_model)

# Extract the a0, a1 values from model_fit.params
a0 = model_fit.params['Intercept']
a1 = model_fit.params['x_column']

# Visually verify that these parameters a0, a1 give the minimum RSS
fig, rss = compute_rss_and_plot_fit(a0, a1)