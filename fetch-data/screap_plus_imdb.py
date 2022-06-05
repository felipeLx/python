import pickle
from clean_screap_movies import save_data_to_pickle

def load_data_from_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

movies_list = load_data_from_pickle('star_wars_movies_cleaned.pickle')
# print(movies_list[1])

import requests
import urllib
import os
from dotenv import load_dotenv

load_dotenv()
# env = os.environ("OMDB_API_KEY")

def get_omdb_data(title):
    base_url = "http://www.omdbapi.com/?"
    parameters = {"apikey": os.getenv("OMDB_API_KEY"), "t": title}
    params_encode = urllib.parse.urlencode(parameters)
    full_url = base_url + params_encode
    return requests.get(full_url).json()

def get_rotten_tomato_score(omdb_info):
    ratings = omdb_info.get('Ratings', [])
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return rating['Value']
    return None

for movie in movies_list:
    title = movie['title']
    omdb_info = get_omdb_data(title)
    movie['imdb_score'] = omdb_info['imdbRating']
    movie['rotten_tomato_score'] = get_rotten_tomato_score(omdb_info)

print(movies_list[1])
save_data_to_pickle('star_wars_movies_with_omdb_data.pickle', movies_list)

import pandas as pd

df = pd.DataFrame(movies_list)
df.to_csv('star_wars_movies_with_omdb_data.csv')