# functions
# to find average
x <- c(1, 4, 5, 7, 3)
avg <- sum(x)/length(x)
avg

y <- 1:100
avg2 <- function(x) {
  s <- sum(x)
  n <- length(x)
  s/n
}
avg2(y)
identical(mean(y), avg(y))

# Lexical scope
# the variables create inside the function its not global variable.
# my_function <- function(x, y, z) {
  # operations that operate on x,y,z which is defined by user of function
  # value final line is returned
#}
avg3 <- function(x, arithmetic = TRUE) {
  n <- length(x)
  ifelse(artithmetic, sum(x)/n, prod(x)^(1/n))
}