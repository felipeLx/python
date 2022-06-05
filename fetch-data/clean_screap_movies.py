import json

def load_data(title):
    with open(title, 'r', encoding='utf-8') as f:
        return json.load(f)

movie_into_list = load_data('star_wars_movies.json')
# print(movie_into_list)

def minute_to_integer(running_time):
    if running_time == 'N/A':
        return None
    elif isinstance(running_time, list):
       return int(running_time.split(' ')[0])
    else:
        return int(running_time.split(' ')[0])

for movie in movie_into_list:
    movie['running_time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))

import re
amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"
word_re = rf"\${number}(-|\sto\s|–)?({number})?\s({amounts})"
amount_re = rf"\${number}"

def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict[word]

def parse_word_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(',', ''))
    word = re.search(amounts, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value * word_value

def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(',', ''))
    return value

def value_convert(money):
    if money == 'N/A':
        return None

    if isinstance(money, list):
        money = money[0]

    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(amount_re, money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())
    elif value_syntax:
        return parse_value_syntax(value_syntax.group())
    else:
        return None

for movie in movie_into_list:
    movie['budget (float)'] = value_convert(movie.get('Budget', 'N/A'))
    movie['box office (float)'] = value_convert(movie.get('Box office', 'N/A'))

"""
from datetime import datetime

dates = [movie.get('Release date', 'Release dates') for movie in movie_into_list]

def clean_date(date):
    return date.split("(")[0].strip()

def date_conversion(date):
    if isinstance(date, list):
        # print(date)
        date = date[0]
    if date == 'N/A':
        return None

    date_str = clean_date(date)
    # print(date_str)
    fmts = ["%B %d, %Y", "%d %B %Y"]
    for fmt in fmts:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    return date_str

for movie in movie_into_list:
    movie['Release date (fmt)'] = date_conversion(movie.get('Release date', 'Release dates'))

"""
import pickle

def save_data_to_pickle(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def load_data_from_pickle(name):
    with open(name, 'wb') as f:
        return pickle.load(f)

save_data_to_pickle('star_wars_movies_cleaned.pickle', movie_into_list)