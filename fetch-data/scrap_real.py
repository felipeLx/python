from bs4 import BeautifulSoup
import pandas as pd
import requests

html_text = requests.get('https://dados.antt.gov.br/dataset/volume-trafego-equivalente-praca-pedagio').text

soup = BeautifulSoup(html_text, 'lxml')
csv_files = soup.find_all('li', class_='resource-item')
csv_file = soup.find_all('li', class_='resource-item')[-2]
csv_last = csv_file.find('a', class_='resource-url-analytics')
url_csv = csv_last['href']
# df = pd.read_html(url_csv)[0]
# print(df.head())
print(url_csv)
# print(csv_last)