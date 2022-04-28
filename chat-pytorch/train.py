import json
from nltk_utils import tokenize, stem, bag_of_words

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['!', '?', ',', '. ', '.', ':', ';', '-', '_', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=', '{', '}', '[', ']', '"', '\'', '<', '>', '/', '\\', '|', '`', '~', '\n', '\t']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))