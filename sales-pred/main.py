import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/felipelx/Downloads/marketing.csv')

print(df.head())
print(df.isnull().sum())

sns.set_style('darkgrid')
"""
f_tv = sns.scatterplot(y='TV', x='Sales', data=df, hue='TV', size='TV')
sns.regplot(data=df, y='TV', x='Sales', scatter=False, fit_reg=True, ax=f_tv)
f_tv.set(xlabel='TV', ylabel='Sales')

f_news = sns.scatterplot(y='Newspaper', x='Sales', data=df, hue='Newspaper', size='Newspaper')
sns.regplot(data=df, y='Newspaper', x='Sales', scatter=False, fit_reg=True, ax=f_news)
f_news.set(ylabel='Newspaper', xlabel='Sales')

f_radio = sns.scatterplot(y='Radio', x='Sales', data=df, hue='Radio', size='Radio')
sns.regplot(data=df, y='Radio', x='Sales', scatter=False, fit_reg=True, ax=f_radio)
f_radio.set(ylabel='Radio', xlabel='Sales')

plt.show()
"""
correl = df.corr()
print(correl.Sales.sort_values(ascending=False))

x = np.array(df.drop( ['Sales'], 1 ))
y = np.array(df['Sales'])
x_train, xtest, y_train, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)
print(model.score(xtest, ytest))
# features = ['TV', 'Radio', 'Newspaper']
features = np.array([[500.1, 10.8, 8.4]])
print(model.predict(features))