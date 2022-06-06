from sqlalchemy import exists
import yfinance as yf
import spacy
from spacy.lang.pt.examples import sentences
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

# rss_feeds = {'news': 'https://gadgets360.com/rss/news', 'market': 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms', 'technology': 'https://www.computerweekly.com/rss/Latest-IT-news.xml'}
# print(yf.Ticker('PETR4.SA').info)
nlp = spacy.load('pt_core_news_sm')
st.title("News Aggregator :zap:")

def extracting_text_rss(rss_link):
    headings = []
    # r = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    r_client = requests.get(rss_link)
    print(r_client.status_code)
    # soup = BeautifulSoup(r.content, 'lxml')
    soup_client = BeautifulSoup(r_client.content, 'lxml')
    # headings = soup.find_all('title')
    headings_client = soup_client.find_all('title')
    return headings_client

stock_info_dict = {
    'Org': [],
    'Symbol': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'divYield': [],
    'marketCap': [],
}

def stock_info_from_yfinance(headings):
    stocks_df = pd.read_csv('stocks.csv')
    for title in headings:
        doc = nlp(title.text)
        for token in doc.ents:
            try:
                if stocks_df['Empresas'].str.contains(token.text).sum():
                    symbol = stocks_df[stocks_df['Empresas'].str.contains(token.text)]['Ativos'].values[0]
                    business = stocks_df[stocks_df['Empresas'].str.contains(token.text)]['Empresas'].values[0]
                    print('symbol: ', symbol)
                    # get the info from yfinance
                    stock_info = yf.Ticker(symbol).info
                    # print('stock: ', stock_info)
                    if not stock_info['dayHigh']:
                        print('not dayHigh')
                    else:
                        stock_info_dict['Org'].append(business)
                        stock_info_dict['Symbol'].append(symbol)
                        stock_info_dict['currentPrice'].append(stock_info['regularMarketPrice'])
                        stock_info_dict['dayHigh'].append(stock_info['dayHigh'])
                        stock_info_dict['dayLow'].append(stock_info['dayLow'])
                        stock_info_dict['forwardPE'].append(stock_info['forwardPE'])
                        stock_info_dict['divYield'].append(stock_info['dividendYield'])
                        stock_info_dict['marketCap'].append(stock_info['marketCap'])
                else: # company name not match
                    pass
            except Exception as e:
                print('error message: ', e)
    print(len(stock_info_dict))
    output_df = pd.DataFrame(stock_info_dict)
    print(len(output_df))
    return output_df

# streamlit client input
usr_input = st.text_input("Enter your RSS news headline:", "http://pox.globo.com/rss/valor")

# get the headlines
fin_headings = extracting_text_rss(usr_input)
output_fin = stock_info_from_yfinance(fin_headings)
print(output_fin)
output_fin.drop_duplicates(inplace=True)

# streamlit df output
st.dataframe(output_fin)

# streamlit expander
with st.expander('Expand for financial stock news!'):
    for heading in fin_headings:
        st.markdown(heading.text[2:])                                                                                                                       

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()