import yfinance as yf
import spacy
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(page_title="Finance Market", page_icon="📊")

# rss_feeds = {'news': 'https://gadgets360.com/rss/news', 'market': 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms', 'technology': 'https://www.computerweekly.com/rss/Latest-IT-news.xml'}

    st.title("Grupo de Notícias :zap:")
    nlp = spacy.load('pt_core_news_sm')

    def extracting_text_rss(rss_link):
        r_client = requests.get(rss_link)
        soup_client = BeautifulSoup(r_client.content, 'lxml')
        headings_client = soup_client.find_all('title')
        return headings_client

    stock_info_dict = {
        'Org': [],
        'Symbol': [],
        'regularMarketPrice': [],
        'previousClose': [],
        'bidPrice': [],
        'askPrice': [],
        'DailyChange': []
    }

    @st.cache
    def convert_df(df):
        return df.to_csv('./data/rss.csv')

    def stock_info_from_yfinance(headings):
        stocks_df = pd.read_csv('./data/stocks.csv')
        for title in headings:
            doc = nlp(title.text)
            for token in doc.ents:
                try:
                    if stocks_df['Empresas'].str.contains(token.text).sum():
                        symbol = stocks_df[stocks_df['Empresas'].str.contains(token.text)]['Ativos'].values[0]
                        business = stocks_df[stocks_df['Empresas'].str.contains(token.text)]['Empresas'].values[0]
                        stock_info = yf.Ticker(symbol).info
                        if not stock_info['bid']:
                            print('not bid')
                        else:
                            dailyChange = str(round((stock_info['regularMarketPrice'] - stock_info['previousClose']) / stock_info['previousClose'] * 100, 2)) + '%'
                            stock_info_dict['Org'].append(business)
                            stock_info_dict['Symbol'].append(symbol)
                            stock_info_dict['regularMarketPrice'].append(stock_info['regularMarketPrice'])
                            stock_info_dict['bidPrice'].append(stock_info['bid'])
                            stock_info_dict['previousClose'].append(stock_info['previousClose'])
                            stock_info_dict['askPrice'].append(stock_info['ask'])
                            stock_info_dict['DailyChange'].append(dailyChange)
                    else: # company name not match
                        pass
                except Exception as e:
                    print('error message: ', e)
        output_df = pd.DataFrame(stock_info_dict)
        convert_df(output_df)
        return output_df

    # streamlit client input
    usr_input = st.text_input("Coloque o link do rss:", "http://pox.globo.com/rss/valor")

    # get the headlines
    fin_headings = extracting_text_rss(usr_input)
    output_fin = stock_info_from_yfinance(fin_headings)
    # print('output_fin: ', output_fin)
    output_fin.drop_duplicates(inplace=True, subset=['Symbol'])
    # streamlit df output
    st.dataframe(output_fin)

    # streamlit expander
    with st.expander('Expandir para ver o título das notícias!'):
        for heading in fin_headings:
            st.markdown(heading.text)

    def Rss_Market():
        st.sidebar.markdown("# Indicadores do rss-feed")

    def Rss_Chart():
        st.markdown("# Gráfico das empresas SA do rss-feed")
        st.sidebar.markdown("# Gráfico do rss-feed")

    page_names_to_funcs = {
        "Rss Market": Rss_Market,
        "Rss_Chart": Rss_Chart
    }

    selected_page = st.sidebar.selectbox("Selecione a Página", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

if __name__ == '__main__':
    run()