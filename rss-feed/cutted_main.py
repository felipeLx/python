
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

