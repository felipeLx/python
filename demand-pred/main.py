import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/demand.csv")
print(df.head())
df.dropna(inplace=True)
"""
data checked before to work on
print(df.isnull().sum())
"""

"""
analysis of data before to work on
fig = px.scatter(df, x="Units Sold", y="Total Price", color="Units Sold", size="Units Sold")
fig.show()

print(df.corr())
correl = df.corr(method='pearson')
plt.figure(figsize=(10, 10))
sns.heatmap(correl, annot=True, cmap="YlGnBu")
plt.show()
=> result: Base Price is the most correlated with Total Price
"""
# data preprocessing
x = df[['Total Price', 'Base Price']].values
y = df['Units Sold']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=100)
model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)

# probability of prediction
score = model.score(xtest, ytest)
print(score)
# features = [["Total Price", "Base Price"]]
features = np.array([[133.00, 140.00]])
result = model.predict(features)
print(result)