# to know a class
a <- 1
class(a)
class(ls)

# dataset
library(dslabs)
#data("murders")

# str - structure of an object
str(murders)

# $ to access the variable(column)
pop <- murders$population
length(pop)

# function names() is specifically designed to extract the column names
names(murders)

# characther vector
class(murders$state)

z <- 3 == 2
class(z)

# factor
class(murders$region)
levels(murders$region) # to see the values

# Use square brackets to extract `abb` from `murders` and assign it to b
b <- murders[["abb"]]

# Check if `a` and `b` are identical 
identical(a, b)

# The function table takes a vector as input and returns the frequency of each unique element in the vector.
table(murders$region)

library(dslabs)
data("movielens")
str(movielens)
class(movielens$title)
class(movielens$genres)
nlevels(movielens[["genres"]])
