# indexing
# using logical operators to index vectors
index <- murder_rate < 0.71
index <- murder_rate <= 0.71
murders$state[index]

# sum will some: 1 TRUE 0 FALSE
sum(index)

west <- murders$region == "West"
safe <- murder_rate <= 1
index_2 <- safe & west
index_2
murders$state[index_2]

# which, match, %in%
x <- c(FALSE, TRUE, FALSE, TRUE, TRUE, FALSE)
# which is useful when a logical vector is long and we only want indexing
which(x)

index_3 <- which(murders$state == "Massachusetts")
murder_rate[index_3]

# match looks for entries in vector and return the index needed to access them
index_4 <- match(c("New York", "Florida", "Texas"), murders$state)
index_4
murder_rate[index_4]
murders$state[index_4]

# %in% when we want to know whether or not each element of a first
  # vector is in a second vector
z <- c("a", "b", "c", "d", "e")
y <- c("a", "d", "f")
y %in% z
c("Boston", "Dakota", "Washington") %in% murders$state
