import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('//home/felipelx/Downloads/lotto_sum.csv', sep=',', header=0)
# print(df.head())
corr = df.corr()
print(corr)

# data processing
x = df[['Num', 'Qty']].values
y = df['Prop']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = DecisionTreeRegressor()
model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print(score)

features = np.array([[1, 2, 4, 5, 8, 9, 11, 13, 15, 16, 19, 20, 22, 24,25], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
result = model.predict(features)
print(result)