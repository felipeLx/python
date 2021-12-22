import pandas as pd
import requests

html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
nba_tables = pd.read_html(html_url)
len(nba_tables)
nba = nba_tables[0]
print(nba.head())

html_url2 = "https://en.wikipedia.org/wiki/The_Simpsons"
r = requests.get(html_url2)
wiki_tables = pd.read_html(r.text, header=0)
len(wiki_tables)
simpsons = wiki_tables[1]
simpsons.head()

# clean row that repeat header
nba.drop(range(22, nba.shape[0] + 1, 20))

simpsons.drop([0,1], inplace=True)
simpsons.set_index('Season', inplace = True)
simpsons['No. ofepisodes'].unique()
simpsons = simpsons.loc[simpsons['No. ofepisodes'] != 'TBA']