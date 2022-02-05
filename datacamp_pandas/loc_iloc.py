# slicing is a technique for selecting consecutive elements from objects

# list
breeds = ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"]

# to slice the list you pass first and last positions separated by a colon into square brackets
print(breeds[2:5])

# if you want to slite to start from the biginning of the list, you can omit the zero
breeds[:3]

# slicing with colon on its own returns the whole list
breeds[:]

# slice DataFrame, you need to sort the list
dogs_str = dogs.set_index(["breed", "color"]).sort_index()

# to slice rows at the outer level of an index, you call loc, passing the first and last values separated by a colon
dogs_str.loc["Chow Chow": "Poodle"] # the final value Poodle is included

# there are two differences compared to slicing lists
# rather than specifying row numbers, you specify index values
dogs_str[("Labrador", "Brown"):("Schnauzer", "Grey")]
# pass the first and last positions as tuples

# since DataFrames are 2D objects, you can also slice columns
dogs_str.loc[: "name": "height_cm"] 
# -> subset columns, but keeping all rows

# you can slice row and columns at the same time
dogs_str.loc[
    ("Labrador", "Brown"):("Schnauzer", "Grey"),
    "name": "height_cm"]

# important use case: subset DataFrames by a range of dates
dogs = dogs.set_index("data_of_birth").sort_index()
dogs.loc["2014-08-25": "2016-09-16"]

# slicing by partial dates
dogs.loc["2014":"2016"]
# all dates in 2014, 2015, 2016

# subsetting by row/column number
print(dogs_iloc[2:5, 1:4])
# -> syntax to slicing lists, except that thereare two arguments: one for rows and one for columns
# the 5 row and 4 column are not included