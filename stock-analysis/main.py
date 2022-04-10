import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=5000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

df = yf.download(tickers="AAPL", start=start_date, end=end_date, progress=False)
df['Date'] = df.index
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
df.reset_index(inplace=True, drop=True)
df_print1 = df.tail()
print(df_print1)

# candlestick chart to have a better view of the increase and decrease of the stock price
import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
figure.update_layout(title='AAPL Stock Price Analysis', xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=False)
# figure.show()

# correlation with the Close column
correl = df.corr()
print(correl['Close'].sort_values(ascending=False))

# trainning LSTM for stock price prediction
x = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']
x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from keras.models import Sequential
from keras.layers import Dense, LSTM

model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
summary = model.summary()
print(summary)

# train our neural network model for stock price prediction
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=1, epochs=30)

# Test giving input values according to the features that we have used to train this model and predicting the final result
import numpy as np
# features = [Open, High, Low, Volume]
features = np.array([[177.089996, 180.419998, 177.070007, 74919600]])
model.predict(features) # return the Close value