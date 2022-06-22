"""
Recommendation of movie based on MovieLens 100k dataset from GroupLens

you will need the answers to these questions:

How do you determine which users or items are similar to one another?
Given that you know which users are similar, how do you determine the rating that a user would give to an item based on the ratings of similar users?
How do you measure the accuracy of the ratings you calculate?
"""
from cgi import print_directory
import pandas as pd

df = pd.read_csv("/home/felipelx/Downloads/uitem.csv", sep="|", header=None)
print(df.head())

from scipy import spatial

a = [1,2]
b = [2,4]
c = [2.5, 4]
d = [4.5, 5]

# euclidean to calculate distance
print(spatial.distance.euclidean(c,a))
print(spatial.distance.euclidean(c,b))
print(spatial.distance.euclidean(c,d))

from surprise import Dataset, Reader, KNNWithMeans, SVD

rating_dict = {
    "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
}

df = pd.DataFrame(rating_dict)
reader = Reader(rating_scale = (1,5))
#data_raw = pd.read_csv("/home/felipelx/Downloads/movie_data.csv", header=None)
#data_df = pd.DataFrame(data_raw)
data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
movielens = Dataset.load_builtin('ml-100k')

"""
cosine similarity and to find similar items using the item-based approach
To find the similarity, you simply have to configure the function by passing a dictionary as an argument to the recommender function.
"""
sim_options = {'name': 'cosine', 'user_based': False}
algo = KNNWithMeans(sim_options=sim_options)

trainingSet = data.build_full_trainset()
algo.fit(trainingSet)

prediction = algo.predict('E', 2)
print(prediction.est)

# Surprise provides a GridSearchCV class analogous to GridSearchCV from scikit-learn.
from surprise.model_selection import GridSearchCV

n_sim_options = {
    "name": ["msd", "cosine"],
    "min_support": [3,4,5],
    "user_based": [False, True],
}
param_grid = {"sim_options": n_sim_options}
gs = GridSearchCV(KNNWithMeans, param_grid, measures=['rmse', 'mae'], cv=3)
gs.fit(movielens)

#print(gs.best_score['rmse'])
#print(gs.best_params['rmse'])

n_param_grid = {
    "n_epochs": [5, 10],
    "lr_all": [0.002, 0.005],
    "reg_all": [0.4, 0.6],
}
n_gs = GridSearchCV(SVD, n_param_grid, measures=['rmse', 'mae'], cv=3)
n_gs.fit(movielens)

print(n_gs.best_score["rmse"])
print(n_gs.best_params["rmse"])