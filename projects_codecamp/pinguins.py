# raw dataset: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv
import pandas as pd

url = 'https://raw.githubusercontent.com/dataprofessor/streamlit_freecodecamp/main/app_8_classification_penguins/penguins_cleaned.csv'
df = pd.read_csv(url)
df = df.dropna()

target = 'species' # what will be predicted
encode = ['sex', 'island'] # parameters to find the prediction

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df_copy = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}

def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# split X and Y
X = df.iloc[:,:4].values
Y = df['species']

# build model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, Y)

# saving model
import pickle
pickle.dump(clf, open('model.pkl', 'wb'))