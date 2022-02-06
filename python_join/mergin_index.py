# merge tables using the index
"""
the DataFrame indexes are given a unique id that we can use when merging two tables together

"""
import pandas as pd
# create index to a column
movies = pd.read_csv('tmb_movies.csv', index_col=['id'])
print(movies.head())

# mergin on index
movies_tag = movies.merge(taglines, on="id", how="left")
print(movies_tag.head())

# multi index datasets
samuel = pd.read_csv("samuel.csv", index_col=["movie_id", "cast_id"])
print(samuel.head())

casts = pd.read_csv("casts.csv", index_col=["movie_id", "cast_id"])
print(casts.head())

samuel_casts = samuel.merge(casts, on=["movie_id", "cast_id"])
print(samuel_casts.head())
print(samuel_casts.shape)

# if the index level names are different between 2 tables that we want to merge, then we can use the left_on and right_on arguments of the merge method
movies_genres = movies.merge(movie_to_genres, left_on="id", left_index=True, right_on="movie_id", right_index=True)

# how we are merging on indexes, we need to set left_index and the right_index to True

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", ascending=False).head())