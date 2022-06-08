
"""
res = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
soup = BeautifulSoup(res.content, 'lxml')
headlines = soup.find_all('title')
nlp = spacy.load('en_core_web_sm')
print(headlines[4].text)
spacy.explain('NSUBJ')
processed_hline = nlp(headlines[4].text) # to just take the text without tags


for token in processed_hline:
    print(token.text, "-", token.pos_, "-", token.dep_, "-", spacy.explain(token.pos_))
print(spacy.displacy.render(processed_hline, style='ent',options={'distance': 120}))
"""

"""
# extract the name and symbol from Brazil InfoMoney market
def extract_tables_from_infomoney():
    tables = pd.read_html('https://www.infomoney.com.br/cotacoes/empresas-b3/', header=0)
    tables_all = pd.concat(tables[1:], axis=0)
    tables_all = tables_all[['Empresas', 'Ativos']]
    df = pd.DataFrame(tables_all, index=None)
    df['Ativos'] = df['Ativos'] + '.SA'
    df.to_csv('stocks.csv')
    return df
"""

"""
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
figure.show()
"""