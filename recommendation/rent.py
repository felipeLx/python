from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

r = requests.get('https://sa.aqar.fm/', headers={'User-Agent': 'Custom'})
soup = bs(r.content, 'lxml')
tables = soup.find('div', attrs= {'class': 'listing_LinkedListingCard__5SRvZ'})

directions = tables.find_all('a')
prices = tables.find_all('div', attrs={'class': 'listingCard-module_price__xxySC'})
bathroom_leaving_beds_mets = tables.find_all('div', attrs={'class':'listingCard-module_specs__rGBlZ'})

my_dict2 = {
    'directions': [],
    'price': [],
    'bathroom': [],
    'leaving': [],
    'beds': [],
    'mets': []
}

for i in bathroom_leaving_beds_mets:
    if bathroom_leaving_beds_mets.find('img', attrs={'alt': 'Bed'}):
        my_dict2['bedroom'].append(i.get_text())

    #bathrooms = np.array(str(i.get_text()).split(' '))
    #print(bathrooms)

print(my_dict2)

my_dict3 = {
    'directions': [],
    'price': [],
    'bathroom': [],
    'leaving': [],
    'beds': [],
    'mets': []
}

for i in directions:
    my_dict2['directions'].append(i.get_text())

for i in prices:
    my_dict2['price'].append(i.get_text())

#for i in bathroom_leaving_beds_mets:
 #   my_dict2['bathroom_leaving_beds_mets'].append(i.get_text())
# print(my_dict2)

df = pd.DataFrame(my_dict2)
print(df.head())
# df = pd.read_html(str(tables.get_text()))[0]

# print(df.head())