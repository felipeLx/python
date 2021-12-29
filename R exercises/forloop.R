# for loops
# 1 + 2 + ... + n = n(n+1)/2
compute_s_n = function(n) {
  x <- 1: n
  sum(x)
}

compute_s_n(3)

# for (i in range of values) {
  # operations that use i, which is changing across the range of values
#}
for(i in 1:5) {
  print(i)
}
i # the last value of range

m <- 25
s_n <- vector(length = m)
for(i in 1:m) {
  s_n[i] <- compute_s_n(i)
}
s_n

n <- 1:m
plot(n, s_n)
lines(n, n*(n+1)/2)

# functions used instead of for loops
apply()
sapply()
# tapply(vector, index, function)
mapply(function, ...)

split()
cut()
quantile()
reduce()
identical()
unique()