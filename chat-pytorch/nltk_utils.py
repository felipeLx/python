import nltk
# nltk.download('punkt')

def tokenize(text):
    return nltk.word_tokenize(text)

def stem(word):
    return nltk.PorterStemmer().stem(word.lower())

def bag_of_words(tokenized_word, words):
    return dict([(word, True) for word in words])

"""
Check if works
a = "Quais os pontos turísticos da cidade?"
print(a)
a = tokenize(a)
print(a)
stem_w = [stem(w) for w in a]
print(stem_w)
"""