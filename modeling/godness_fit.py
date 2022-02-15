# goodness-of-fit: show how they are different than but related to RSS
"""
3 Different R's:
    Building models: RSS
    Evaluating models: RMSE, R-squared

RSS: used to find the optimal values for model parameters and thus, the best model

2 common ways to quantify the goodness -of-fit for a linear model
RMSE: most common
"""
residuals = y_model - y_data
RSS = np.sum(np.square(residuals))

mean_squared_residuals = np.sum(np.square(residuals)) / len(residuals)

MSE = np.mean(np.square(residuals))
RMSE = np.sqrt(np.mean(np.square(residuals)))
RMSE = np.std(residuals)
# RMSE as providing a measure of how much the model "deviates" from the data

"""
R-squared: how much the variation of the data is due to he linear trend and how much is not
    is a quantitative measure of just that ratio
"""
deviations = np.mean(y_data) - y_data
VAR = np.sum(np.square(deviations))

residuals = y_model - y_data
RSS = np.sum(np.square(residuals))

r_squared = 1 - (RSS/VAR)
r = correlation(y_data, y_model)

# when the variation due to linear trend is larger than the variation due to residuals, the model is better
# RMSE: how much variation is residual
# R-squared: what fraction of variation is linear

# Build the model and compute the residuals "model - data"
y_model = model_fit_and_predict(x_data, y_data)
residuals = y_model - y_data

# Compute the RSS, MSE, and RMSE and print the results
RSS = np.sum(np.square(residuals))
MSE = RSS/len(residuals)
RMSE = np.sqrt(MSE)
print('RMSE = {:0.2f}, MSE = {:0.2f}, RSS = {:0.2f}'.format(RMSE, MSE, RSS))

# Compute the residuals and the deviations
residuals = y_model - y_data
deviations = np.mean(y_data) - y_data

# Compute the variance of the residuals and deviations
var_residuals = np.mean(np.square(residuals))
var_deviations = np.mean(np.square(deviations))

# Compute r_squared as 1 - the ratio of RSS/Variance
r_squared = 1 - (var_residuals / var_deviations)
print('R-squared is {:0.2f}'.format(r_squared))
"""
Notice that R-squared varies from 0 to 1, where a value of 1 means that the model and the data are perfectly correlated and all variation in the data is predicted by the model. A value of zero would mean none of the variation in the data is predicted by the model. Here, the data points are close to the line, so R-squared is closer to 1.0
"""