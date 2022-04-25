import pandas as pd

url = 'https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv'
df = pd.read_csv(url)

print(df.head())

X = df.drop(['logS'], axis=1)
Y = df.iloc[:, -1]

# build model
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

model = linear_model.LinearRegression()
# X_model, X_train, Y_model, Y_train = train_test_split(X, Y, test_size=0.2)
model.fit(X, Y)

# predict
Y_pred = model.predict(X)

# model performance
print('Coeficient: ', model.coef_)
print('Intercept: ', model.intercept_)
print('R2 score: ', r2_score(Y, Y_pred))
print('MSE: ', mean_squared_error(Y, Y_pred))

# model equation
print('LogS = %.2f %.2f LogP %4f MW + %4f RB %.2f AP' % (model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3]))

"""
# plot
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
plt.scatter(x=Y_train, y=Y_pred_train, color='blue', label='Data')
"""

# save model to pickle object
import pickle

pickle.dump(model, open('solubility_model.pkl', 'wb'))