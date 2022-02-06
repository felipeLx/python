# pandas .concat() method can concatenate both vertical and horizontal axis=0, vertical

"""
3 diff tables
same column names
table variable names:
    inv_jan (top)
    inv_feb (middle)
    inv_mar (botton)
"""

pd.concat([inv_jan, inv_feb, inv_mar])

# ignoring the index
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True)

# setting labels to original tables
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True, keys=['jan', 'fev', 'mar'])

# the concat method by default will include all of the columns in the diff tables it's combining
pd.concat([inv_jan, inv_feb], sort=True)

# if we only want the matching columns between tables, we set the join argument to "inner"

"""
.append()
. simplified version of the .concat()method
. supports ignore_index, and sort
. does not support keys and join => always join = outer
"""

"""
Append is a DataFrame method therefore , we list the "inv_jan" table first then call the method
"""
inv_jan.append([inv_feb, inv_mar], ignore_index=True, sort=True)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join="inner",
                               sort=True)
print(tracks_from_albums)