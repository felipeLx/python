from bs4 import BeautifulSoup
import requests
from torch import NoneType

def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(' ', strip=True).replace('\xa0', '') for li in row_data.find_all('li')]
    elif row_data.find('br'):
        return [text for text in row_data.stripped_strings]
    else:
        return row_data.get_text(' ', strip=True).replace('\xa0', '')


def clean_tag(soup):
    for tag in soup.find_all(['sup', 'span']):
        tag.decompose()

def get_info_box(url):
    movie_info = {}
    star_wars_movies = requests.get(url)
    soup = BeautifulSoup(star_wars_movies.content, 'lxml')
    
    info_box = soup.find(class_="infobox vevent")
    info_rows = info_box.find_all('tr')
    clean_tag(info_box)

    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info['title'] = row.find('th').get_text(' ', strip=True)
        # elif index == 1:
          #  continue
        else:
            header = row.find('th')
            if header:
                content_key = row.find('th').get_text(' ', strip=True)
                content_value = get_content_value(row.find('td'))
                movie_info[content_key] = content_value
    return movie_info

star_wars_movies = requests.get('https://en.wikipedia.org/wiki/Star_Wars')
soup = BeautifulSoup(star_wars_movies.content, 'lxml')

movies = soup.select(".wikitable.plainrowheaders i a")

base_path = "https://en.wikipedia.org/"

movie_into_list = []
for index, movie in enumerate(movies):
    try:
        relative_path = movie['href']
        full_path = base_path + relative_path
        # print(relative_path)
        movie_into_list.append(get_info_box(full_path))
    except Exception as e:
        print(movie.get_text())
        print(e)

import json

def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data(title):
    with open(title, 'r', encoding='utf-8') as f:
        return json.load(f)

save_data('star_wars_movies.json', movie_into_list)