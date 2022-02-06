# one-to-one = every row in the left tables is related to one to one and only one row in the right table
# one-to-many = every row in left table in related to one or more rows in the right table
ward_licenses = wards.merge(licenses, on="ward", suffixes=('_ward', '_lic'))
ward_licenses.head()

print(wards_shape)
# (50, 4)

print(ward_licenses.shape)
(10000, 9)

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values("account", ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())