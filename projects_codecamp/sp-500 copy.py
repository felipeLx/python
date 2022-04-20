import streamlit as st
import pandas as pd
import yfinance as yf
import base64
import matplotlib.pyplot as plt
import numpy as np

st.title('SP 500 app')
st.markdown('Retrieve a list detailed from SP 500')

st.sidebar.header('User input features')

@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    df = df.drop(['Headquarters Location','SEC filings'], axis=1)
    print(df.head())
    return df

df = load_data()

# Select sector
sector_unique = df['GICS Sector'].unique()
sector = df.groupby('GICS Sector', as_index=False)

# Sidebar selection
sorted_sector_unique = sorted(sector_unique)
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique)
num_companies = st.sidebar.slider('Number of companies', min_value=1, max_value=5, step=1)

# Sidebar filter
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

# charter section
symbols = df_selected_sector['Symbol'].unique()
print(symbols)
# body section
st.header('Display Companies by Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns')
st.dataframe(df_selected_sector)

# code and decode for download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # string to bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="selected_sector.csv">Download csv file</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# get stock market data
def get_stock(symbols):
    tickers_list = []
    for symbol in symbols:
        tickers_list.append(symbol)
    
    stocks = yf.download(
        tickers = list(tickers_list),
        period = 'ytd',
        interval = '1d',
        group_by = 'ticker',
        auto_adjust = True,
        prepost=True,
        threads=True,
        proxy=None
    )
    data = pd.DataFrame(stocks).reset_index()
    data.columns = data.columns.map('_'.join)
    data_close = data.filter(like='Close')
    data_date = data.filter(like='Date')
    data_full = data_date.combine_first(data_close).set_index('Date_')

    return data_full

data = get_stock(symbols)

# chart function
def price_plot(symbol):
    df_plot = pd.DataFrame(data[symbol + '_Close'])
    df_plot['Date_'] = df_plot.index
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.fill_between(df_plot.index, df_plot, color='skyblue', alpha=0.2)
    plt.plot(df_plot.index, df_plot, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Close Price', fontweight='bold')
    plt.title(symbol, fontweight='bold')
    return st.pyplot(fig)

# plot section
st.header('Closing Stock Price')
for i in list(df_selected_sector['Symbol'])[:num_companies]:
    price_plot(i)