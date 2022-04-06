import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('/home/felipelx/Downloads/news.csv')
# print(df.shape)
# print(df.head())

labels = df.label
# print(labels.head())

# trainning and testing data
x_train, x_test, y_train, y_test = train_test_split(df['text'], labels, test_size=0.2, random_state=7)

# initialize the TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

# Initialize a PassiveAggressiveClassifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score*100, 2)}%')

# Build confusion matrix
res_matrix = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])

print(res_matrix)
# test1: 583 true positive, 586 true negative, 43 false positive, 55 false negative
# test2: 589 true positive, 585 true negative, 44 false positive, 49 false negative
# test3: 586 true positive, 586 true negative, 43 false positive, 52 false negative