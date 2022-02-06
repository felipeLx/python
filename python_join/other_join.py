# table A 3 rows, table B 4 rows, right join -> table C 4 rows
tv_genre = movie_to_genres[movie_to_genres["genre"] == "TV movie"]
print(tv_genre)

# filtering the data
m = movie_to_genres["genre"] == "TV Movie"
tv_genre = movie_to_genres[m]
print(tv_genre)

# subsetting to develop a table of movies from the TV Movie genre
tv_movie = movies.merge(tv_genre, how="right", left_on="id", right_on="movie_id")
print(tv_movies.head())

# outer join will return all of the rows from both tables regardless if there is a match between the tables
m = movie_to_genres["genre"] == "Family"
family = movie_to_genres[m].head(3)

m = movie_to_genres["genre"] == "Comedy"
comedy = movie_to_genres[m].head(3)

family_comedy = family.merge(comedy, on="movie_id", how="outer", suffixer=("_fam", "_com"))
print(family_comedy)

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on="movie_id", how="right")
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right', suffixes=["_act", "_sci"])
# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi["genre_act"].isna()]

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, left_on="id", right_on="movie_id")

genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on="movie_id", 
                                      right_on="id")

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on="id",
                                     how="outer",
                                     suffixes=['_1','_2'])

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isna()) | 
     (iron_1_and_2['name_2'].isna()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
