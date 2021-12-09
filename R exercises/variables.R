# Types of variables
# Vectors
# When we run a line of code like this:
x <- 2
x
# We’re assigning 2 to a variable x.
# x is a variable but it is also a “numeric vector” of length 1.

class(x) ## [1] "numeric"
length(x) ## [1] 1

fruit <- "apple"
class(fruit) ## [1] "character"
length(fruit) ## [1] 1
nchar("apple") ## [1] 5

# Smushing character vectors together can be done with paste:
paste("key", "lime", "pie") ## [1] "key lime pie"


#Lists
# Vectors and lists look similar in R sometimes but they have very different uses:
a2 <- c(1, "apple", 3)
list(a2)
list(1, "apple", 3)
