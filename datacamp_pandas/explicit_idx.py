# Numpy array for the data, two indexes to store the row and columns details
dogs.columns dogs.index

# index object of column names, and .index contains an Index object of row numbers
# you can move a column from the body of the DataFrame to the index

dogs_int = dogs.set_index("name")
# name is now in the index is that the index values are left-aligned rather than right-aligned
dogs_int.reset_index()
dogs_int.reset_index(drop = True)

dogs[dogs["name"].isin(["Bella", "Stella"])]
# index make subsetting simpler
# equivalent
dogs_ind.loc[["Bella", "Stella"]]

# multiple columns: multi-levels indexes, hierarchical indexes
dogs.set_index(["breed", "color"])

# subset the outer level with a list
dogs_ind3.loc[["Labrador", "Chichaua"]]

# subset inner levels with a list of tuples
dogs_ind3.loc[[("Labrador", "Brown"), ("Chichaua", "Tan")]]
# the resulting rows have to match all conditions from a tuple

# you can sort by index
dogs_ind3.sort_index()

# control the sort passing list
dogs_ind3.sort_index(level = ["color", "breed"], ascending = [True, False])

# in pandas, the syntax for workingwith indexes is different from the syntax for working with columns
"""
. index values are just data
. indexes violate "tidy data" principles
. you need to learn two syntaxes
"""