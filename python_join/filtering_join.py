# mutation join: combines data from 2 tables based on matching observations in both tables
# filtering join: filter observations from table based on whether or not they match an observation in another table

# semi joins
"""
. returns the intersection, similar to a inner join
. returns only columns from the left table and not the right
. no duplicates
"""

genres_tracks = genres.merge(top_tracks, on="gid")
print(genres_tracks.head())

gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
print(gid_list.head()

# anti joins
genres_tracks = genres.merge(top_tracks, on="gid", how="left", indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]

"""
steps:
merge the left and right tables on key column using an inner join
search if the key column in the left table is in the merged tables using the isin()method creating a boolean Series
subset the rows of the left table
"""

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

"""
You performed an anti join by first merging the tables with a left join, selecting the ID of those employees who did not support a top customer, and then subsetting the original employee's table. From that, we can see that there are five employees not supporting top customers. Anti joins are a powerful tool to filter a main table (i.e. employees) by another (i.e. customers).
"""