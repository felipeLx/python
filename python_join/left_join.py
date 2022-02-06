# left join: return all data ftom the left table and only those rows from the right table where key columns match

# table A 3 rows, table B 4 rows, left join return C with 3 rows and all data that match
movies_tagline = movies.merge(taglines, on="id", how="left")
print(movies_tagline.head())

# wherever there isn't a matching ID in the taglines table, a null value is entered for the tag line
print(movies_tagline.shape)
# output: (4805, 5)

movies_financials = movies.merge(financials, on="id", how="left")
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# A left join will return all of the rows from the left table. If those rows in the left table match multiple rows in the right table, then all of those rows will be returned. Therefore, the returned rows must be equal to if not greater than the left table. Knowing what to expect is useful in troubleshooting any suspicious merges.

