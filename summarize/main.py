from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import PyPDF2
import textwrap
# import io
# import requests


# Generate clean sentences
def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        # sentence = "".join([s for s in sentence.strip().splitlines(True) if s.strip()])
        print(sentence)
        # "".join([s for s in sentences.strip().splitlines(True) if s.strip()])
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()
        
    return sentences

# Similarity matrix using cosime to find similarity between sentences
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    
    sent1 = [[word.lower() for word in text.split()] for text in sent1]
    sent2 = [[word.lower() for word in text.split()] for text in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # first vector
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    
    # second vector
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words): 
    # create empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)), shape=None)

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

# Generate Summary Method
def create_summary(filename, top_n=5):
    stop_words = stopwords.words('portuguese')
    summarize_text = []

    # Step 1 - Read text and split it
    sentences = read_article(filename)
    # Step 2 - Generate Similary Martix across sentences
    similarity_matrix = sentence_similarity(sentences, stop_words)
    # Step 3 - Rank sentences in similarity martix
    rank_similarity = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(rank_similarity)
    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    print('Indexes of top ranked_sentence order are ', ranked_sentence)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))
    
    # Step 5 - Offcourse, output the summarize texr
    print("Summarize Text: \n", ". ".join(summarize_text))

"""
# was receiving to many warnings: no solution found to "PdfReadWarning: Superfluous whitespace found in object header"
pdf_url = 'https://elevensiteassets.s3.amazonaws.com/wp-content/uploads/2021/02/Petrobras-Mudanca-CEO-1.pdf'
r = requests.get(pdf_url)
f = io.BytesIO(r.content)
pdf_text = PyPDF2.PdfFileReader(f, strict=False).getPage(0).extractText().split('\n')
print(pdf_text)
"""

create_summary('economia.txt', 5)