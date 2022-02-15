# scikit-learn
from sklearn.linear_model import LinearRegression
# initialize a general model
model = LinearRegression(fit_intercept=True)

# Load and shape the data
x_raw, y_raw = load_data()
x_data = x_raw.reshape(len(y_raw), 1)
y_data = y_raw.reshape(len(y_raw), 1)
# this reshape is needed because scikit-learn is designed for consistent use with more general modeling

# Fit the model to the data
model_fit = model.fit(x_data, y_data)
# finds optimal values for a0 and a1 so that the model fits the data

# Predictions and Parameters
    # extract the linear model parameters
intercept = model.intercept_[0]
slope = model.coef_[0,0]

# use the model to make prediction
future_x = 2100
future_y = model.predict(future_x)

# statsmodels
x, y = load_data()
df = pd.DataFrame(dict(times=x_data, distances=y_data))

fig = df.plot('times', 'distances')
model_fit = ols(formula="distances ~ times", data=df).fit()

# uncertainty
a0 = model_fit.params['Intercept']
a1 = model_fit.params['times']

e0 = model_fit.bse['Intercept']
e1 = model_fit.bse['times']

intercept = a0
slope = a1
uncertainty_in_intercept = e0
uncertainty_in_slope = e1

# import the sklearn class LinearRegression and initialize the model
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)

# Prepare the measured data arrays and fit the model to them
legs = legs.reshape(len(legs),1)
heights = heights.reshape(len(heights),1)
model.fit(legs, heights)

# Use the fitted model to make a prediction for the found femur
fossil_leg = 50.7
fossil_height = model.predict(fossil_leg)
print("Predicted fossil height = {:0.2f} cm".format(fossil_height[0,0]))
"""
Notice that we used the pre-loaded data to fit or "train" the model, and then applied that model to make a prediction about newly collected data that was not part of the data used to fit the model. Also notice that model.predict() returns the answer as an array of shape = (1,1), so we had to index into it with the [0,0] syntax when printing. This is an artifact of our overly simplified use of sklearn here: the details of this are beyond the scope of the current course, but relate to the number of samples and features that one might use in a more sophisticated, generalized model.
"""
# Import LinearRegression class, build a model, fit to the data
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(years, levels)

# Use model to make a prediction for one year, 2100
future_year = 2100
future_level = model.predict(future_year)
print("Prediction: year = {}, level = {:.02f}".format(future_year, future_level[0,0]))

# Use model to predict for many years, and over-plot with measured data
years_forecast = np.linspace(1970, 2100, 131).reshape(-1, 1)
levels_forecast = model.predict(years_forecast)
fig = plot_data_and_forecast(years, levels, years_forecast, levels_forecast)
"""
Note that with scikit-learn, although we could extract a0 = model.intercept_[0] and a1 = model.coef_[0,0], we do not need to do that in order to make predictions, we just call model.predict(). With more complex models, these parameters may not have easy physical interpretations. Notice also that although our model is linear, the actual data appears to have an up-turn that might be better modeled by adding a quadratic or even exponential term to our model. The linear model forecast may be underestimating the rate of increase in sea level.
"""
# Fit the model, based on the form of the formula
model_fit = ols(formula="velocities ~ distances", data=df).fit()

# Extract the model parameters and associated "errors" or uncertainties
a0 = model_fit.params['Intercept']
a1 = model_fit.params['distances']
e0 = model_fit.bse['Intercept']
e1 = model_fit.bse['distances']

# Print the results
print('For slope a1={:.02f}, the uncertainty in a1 is {:.02f}'.format(a1, e1))
print('For intercept a0={:.02f}, the uncertainty in a0 is {:.02f}'.format(a0, e0))