from xml.dom import UserDataHandler
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('/home/felipelx/Downloads/fake_or_real_news.csv')

x = np.array(df["title"])
y = np.array(df["label"])

cv = CountVectorizer()
x = cv.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(x_train, y_train)

import streamlit as st
st.title("Fake News Detector")

def fakenews_detector():
    user = st.text_area("Coloque o texto aqui: ")
    if len(user) < 1:
        st.write("  ")
    else:
        sample = user
        data = cv.transform([sample]).toarray()
        a = model.predict(data)
        st.title(a)

fakenews_detector()