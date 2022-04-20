from sklearn.linear_model import HuberRegressor
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
from PIL import Image
from bs4 import BeautifulSoup
import requests
import json
import time

st.set_page_config(layout= 'wide')

# header
image = Image.open('/home/felipelx/Documents/consulting/logo_brand.png')
st.image(image, width=150)
st.title('Crypto Price App')
st.markdown('Criptocurrency price for the top 100')

# page layout
col1 = st.sidebar
col2, col3 = st.columns((2,1)) # col2 2 times greater tham col3

# sidebar
col1.header('Input Options')
currency_prince_unit = col1.selectbox('Select Currency', ('USD', 'BTC', 'ETH'))

# fetch CoinMarketCap data
@st.cache
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    
    soup = BeautifulSoup(cmc.content, 'html.parser')

    data = soup.find('script', id='__NEXT_DATA__', type='application/json')

    coins = {}
    coin_data = json.loads(data.contents[0])
    # print(coin_data['props']['initialState'])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    attributes = listings[0]['keysArr']
    index_of_id = attributes.index('id')
    index_of_slug = attributes.index('slug')
    
    for i in listings[1:]:
        coins[str(i[index_of_id])] = i[index_of_slug]

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    index_of_slug = attributes.index("slug")
    index_of_symbol = attributes.index("symbol")

    index_of_quote_currency_price = attributes.index(
        f"quote.{currency_prince_unit}.price"
    )
    index_of_quote_currency_percent_change_1h = attributes.index(
        f"quote.{currency_prince_unit}.percentChange1h"
    )
    index_of_quote_currency_percent_change_24h = attributes.index(
        f"quote.{currency_prince_unit}.percentChange24h"
    )
    index_of_quote_currency_percent_change_7d = attributes.index(
        f"quote.{currency_prince_unit}.percentChange7d"
    )
    index_of_quote_currency_market_cap = attributes.index(
        f"quote.{currency_prince_unit}.marketCap"
    )
    index_of_quote_currency_volume_24h = attributes.index(
        f"quote.{currency_prince_unit}.volume24h"
    )

    for i in listings[1:]:
        coin_name.append(i[index_of_slug])
        coin_symbol.append(i[index_of_symbol])
        price.append(i[index_of_quote_currency_price])
        percent_change_1h.append(i[index_of_quote_currency_percent_change_1h])
        percent_change_24h.append(i[index_of_quote_currency_percent_change_24h])
        percent_change_7d.append(i[index_of_quote_currency_percent_change_7d])
        market_cap.append(i[index_of_quote_currency_market_cap])
        volume_24h.append(i[index_of_quote_currency_volume_24h])
    
    df = pd.DataFrame(columns=['coin_name', 'coin_symbol', 'price', '% Change 1h', '% Change 24h', '% Change 7d', 'Market Cap', 'Volume 24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['% Change 1h'] = percent_change_1h
    df['% Change 24h'] = percent_change_24h
    df['% Change 7d'] = percent_change_7d
    df['Market Cap'] = market_cap
    df['Volume 24h'] = volume_24h
    return df

df = load_data()

# Sidebar - Cripto selection
sorted_coin = sorted(df['coin_symbol'])
selected_coin = col1.multiselect('Select Coin', sorted_coin, sorted_coin)

df_selected_coin = df[df['coin_symbol'].isin(selected_coin)]

# Sidebar - number of cripto to display
num_coin = col1.slider('Display Top Coins', 1, 100, 100)
df_coins = df_selected_coin[:num_coin]

# Sidebar - Percent change timeframe
percent_timeframe = col1.selectbox('Percent Change Timeframe', ['1h', '24h', '7d'])
percent_dict = {'1h': '% Change 1h', '24h': '% Change 24h', '7d': '% Change 7d'}
selected_percent_timeframe = percent_dict[percent_timeframe]

# Sidebar - Sort by
sort_values = col1.selectbox('Sort Values?', ['YES', 'NO'])

# Page body
col2.subheader('Price Data of Selected Crypto')
col2.write('Data Dimension: ' + str(df_selected_coin.shape[0]) + ' rows and ' + str(df_selected_coin.shape[1]) + ' columns')

col2.dataframe(df_coins)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

col2.markdown(filedownload(df_selected_coin), unsafe_allow_html=True)

# preparing data to plot
col2.subheader('Table of % Price Change')
df_change = pd.concat([df_coins.coin_symbol, df_coins['% Change 1h'], df_coins['% Change 24h'], df_coins['% Change 7d']], axis=1)
df_change = pd.concat([
    df_coins.coin_symbol,
    df_coins['% Change 1h'],
    df_coins['% Change 24h'],
    df_coins['% Change 7d'],
], axis=1)

df_change = df_change.set_index('coin_symbol')
df_change['positive_percent_change_1h'] = df_change['% Change 1h'] > 0
df_change['positive_percent_change_24h'] = df_change['% Change 24h'] > 0
df_change['positive_percent_change_7d'] = df_change['% Change 7d'] > 0
col2.dataframe(df_change)

# Conditional creation of Bar plot (time frame)
col3.subheader('Bar plot of % Price Change')

if percent_timeframe == '7d':
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['% Change 7d'])
    col3.write('*7 days period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['% Change 7d'].plot(kind='barh', color=df_change.positive_percent_change_7d.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)
elif percent_timeframe == '24h':
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['% Change 7d'])
    col3.write('*24 hour period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['% Change 24h'].plot(kind='barh', color=df_change.positive_percent_change_24h.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)
else:
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['% Change 1h'])
    col3.write('*1 hour period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['% Change 1h'].plot(kind='barh', color=df_change.positive_percent_change_1h.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)