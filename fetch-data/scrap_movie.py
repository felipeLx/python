from bs4 import BeautifulSoup
import requests

star_wars_movies = requests.get('https://en.wikipedia.org/wiki/Rogue_One')
soup = BeautifulSoup(star_wars_movies.content, 'lxml')

contents = soup.prettify()
info_box = soup.find(class_="infobox vevent")
info_rows = info_box.find_all('tr')
movie_info = {}

def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(' ', strip=True).replace('\xa0', '') for li in row_data.find_all('li')]
    else:
        return row_data.get_text(' ', strip=True).replace('\xa0', '')

for index, row in enumerate(info_rows):
    if index == 0:
        movie_info['title'] = row.find('th').get_text(' ', strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find('th').get_text(' ', strip=True)
        content_value = get_content_value(row.find('td'))
        movie_info[content_key] = content_value
