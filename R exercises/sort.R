# sort: function in incremental order
library(dslabs)
data(murders)
sort(murders$total)

# order: return the indices that sort the vector parameter
x <- c(31, 4, 15, 92, 65)
sort(x)

index <- order(x)
x[index]

# order the dataset
index <- order(murders$total)
murders$abb[index]

max(murders$total)
i_max <- which.max(murders$total)
i_max # give us the index of the max(murders$total)

murders$state[i_max] # same to which_min

# rank - for any given list, it gives you a vector of index
  # with the rank of the first entry, second entry, etc
rank(x)

str(murders)

# Define a variable states to be the state names from the murders data frame
states <- murders$state

# Define a variable ranks to determine the population size ranks 
ranks = rank(murders$population)

# Define a variable ind to store the indexes needed to order the population values
ind  = order(murders$population)
print(ind)
# Create a data frame my_df with the state name and its rank and ordered from least opulous to most 
my_df = data.frame(state = states[ind], rank = ranks[ind])
print(my_df)

# Using new dataset 
library(dslabs)
data(na_example)

# Checking the structure 
str(na_example)

# Find out the mean of the entire dataset 
print(mean(na_example))

# Use is.na to create a logical index ind that tells which entries are NA
ind <- is.na(na_example)
print(ind)
# Determine how many NA ind has using the sum function
sum(ind)

# Note what we can do with the ! operator
x <- c(1, 2, 3)
ind <- c(FALSE, TRUE, FALSE)
x[!ind]

# Create the ind vector
library(dslabs)
data(na_example)
ind <- is.na(na_example)

# We saw that this gives an NA
mean(na_example)

# Compute the average, for entries of na_example that are not NA 
mean(na_example[!ind])