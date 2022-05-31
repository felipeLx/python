import nltk
import numpy as np
# nltk.download('punkt')

def tokenize(text):
    return nltk.word_tokenize(text)

def stem(word):
    return nltk.PorterStemmer().stem(word.lower())

def bag_of_words(tokenized_word, words):
    token_sentence = [stem(w) for w in tokenized_word]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in token_sentence:
            bag[idx] = 1.0
    return bag

"""
Check if works
a = "Quais os pontos turísticos da cidade?"
print(a)
a = tokenize(a)
print(a)
stem_w = [stem(w) for w in a]
print(stem_w)
"""