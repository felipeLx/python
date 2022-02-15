"""
Standard Error: how accurate are the model PARAMETERS, are there variations in those parameters
and how much of the variation is due to deterministic trends versus inherent randomness
"""
# model parameters and standard error:
    # parameter value as center
    # parameter standard error as spread
    # standard error, measures parameter uncertainty
"""
we now think of those "optimal"parameter values as not THE one true answer, but the "best estimate"
"""
df = pd.DataFrame(dict(times=x_data, distance=y_data))
model_fit = ols(formula="distances ~times", data=df).fit()

a1 = model_fit.params['times']
a0 = model_fit.params['Intercept']

slope = a1
intercept = a0

# computing standard errors
e0 = model_fit.bse['Intercept']
e1 = model_fit.bse['times']

standard_error_of_intercept = e0
standard_error_of_slope = e1

# Store x_data and y_data, as times and distances, in df, and use ols() to fit a model to it.
df = pd.DataFrame(dict(times=x_data, distances=y_data))
model_fit = ols(formula="distances ~ times", data=df).fit()

# Extact the model parameters and their uncertainties
a0 = model_fit.params['Intercept']
e0 = model_fit.bse['Intercept']
a1 = model_fit.params['times']
e1 = model_fit.bse['times']

# Print the results with more meaningful names
print('Estimate    of the intercept = {:0.2f}'.format(a0))
print('Uncertainty of the intercept = {:0.2f}'.format(e0))
print('Estimate    of the slope = {:0.2f}'.format(a1))
print('Uncertainty of the slope = {:0.2f}'.format(e1))
"""
The size of the parameters standard error only makes sense in comparison to the parameter value itself. In fact the units are the same! So a1 and e1 both have units of velocity (meters/second), and a0 and e0 both have units of distance (meters).
"""
# Build and fit two models, for columns distances1 and distances2 in df
model_1 = ols(formula="distances1 ~ times", data=df).fit()
model_2 = ols(formula="distances2 ~ times", data=df).fit()

# Extract R-squared for each model, and the standard error for each slope
se_1 = model_1.bse['times']
se_2 = model_2.bse['times']
rsquared_1 = model_1.rsquared
rsquared_2 = model_2.rsquared

# Print the results
print('Model 1: SE = {:0.3f}, R-squared = {:0.3f}'.format(se_1, rsquared_1))
print('Model 2: SE = {:0.3f}, R-squared = {:0.3f}'.format(se_2, rsquared_2))

"""
Notice that the standard error is the same for both models, but the r-squared changes. The uncertainty in the estimates of the model parameters is indepedent from R-squred because that uncertainty is being driven not by the linear trend, but by the inherent randomness in the data. This serves as a transition into looking at statistical inference in linear models.
"""