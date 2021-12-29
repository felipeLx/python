x <- c(1,2,-3,4)
if(all(x>0)){
  print("All Positives")
} else{
  print("Not All Positives")
}

y <- c(FALSE, FALSE, TRUE, TRUE, FALSE)
all(!y)

# Assign the state abbreviation when the state name is longer than 8 characters 
new_names <- ifelse(nchar(murders$state) > 8, murders$abb, murders$state)
new_names

# Create function called `sum_n`
sum_n <- function(n) {
  m <- sum(1:n)
  m
}
# Use the function to determine the sum of integers from 1 to 5000
sum_n(5000)

# Create `altman_plot` 
altman_plot <- function(x, y) {
  plot(x+y, y-x)
}

altman_plot(5, 10)

# Run this code 
x <- 3
my_func <- function(y){
  x <- 5
  y+5
}

# Print the value of x 
print(x)

# Write a function compute_s_n with argument n that for any given n computes the sum of 1 + 2^2 + ...+ n^2
compute_s_n <- function(n) {
  mysum <- 0
  myrange <- 1:n
  for(i in myrange) {
    mysum <- mysum + i^2
  }
  mysum
}

# Report the value of the sum when n=10
compute_s_n(10)

# Define a function and store it in `compute_s_n`
compute_s_n <- function(n){
  x <- 1:n
  sum(x^2)
}

# Create a vector for storing results
s_n <- vector("numeric", 25)

# Assign values to `n` and `s_n`
for(i in 1:25){
  s_n[i] <- compute_s_n(i)
}

#  Create the plot 
plot(n, s_n)

# Check that s_n is identical to the formula given in the instructions.
identical(s_n, (n*(n+1)*((2*n)+1))/6)