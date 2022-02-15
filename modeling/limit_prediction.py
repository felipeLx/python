# errors that inevitably arise when making predictions
"""
Domain of validity
    zoom in: data looks linear
    model assumption: a2*x**2 + a3*x**3 + .... = zero
    build a linear model: a0 + a1*x
    zoom out: your model breaks
"""

# build and fit a model to the df_monthly data
model_fit = ols('Close ~ DayCount', data=df_monthly).fit()

# Use the model FIT to the MONTHLY data to make a predictions for both monthly and daily data
df_monthly['Model'] = model_fit.predict(df_monthly.DayCount)
df_daily['Model'] = model_fit.predict(df_daily.DayCount)

# Plot the monthly and daily data and model, compare the RSS values seen on the figures
fig_monthly = plot_model_with_data(df_monthly)
fig_daily = plot_model_with_data(df_daily)
"""
Notice the monthly data looked linear, but the daily data clearly has additional, nonlinear trends. Under-sampled data often misses real-world features in the data on smaller time or spatial scales. Using the model from the under-sampled data to make interpolations to the daily data can result is large residuals. Notice that the RSS value for the daily plot is more than 30 times worse than the monthly plot
"""
# Compute the residuals, "data - model", and determine where [residuals < tolerance]
residuals = np.abs(y_data - y_model)
tolerance = 100
x_good = x_data[residuals < tolerance]

# Find the min and max of the "good" values, and plot y_data, y_model, and the tolerance range
print('Minimum good x value = {}'.format(np.min(x_good)))
print('Maximum good x value = {}'.format(np.max(x_good)))
fig = plot_data_model_tolerance(x_data, y_data, y_model, tolerance)
"""
Notice the range of good values, which extends a little out into the new data, is marked in green on the plot. By comparing the residuals to a tolerance threshold, we can quantify how far out out extrapolation can go before the difference between model and data gets too large.
"""
