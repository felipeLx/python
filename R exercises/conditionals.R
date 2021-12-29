# conditionals: if-else
a <- 2
if(a != 0) {
  print(a)
} else {
  print('its not zero')
}

library(dslabs)
data(murders)
murder_rate <- murders$total/murders$population*100000

ind <- which.min(murder_rate)
if(murder_rate[ind] < 0.5) {
  print(murders$state[ind])
} else {
  print("No state with more low rate")
}

# ifelse - 3 arguments: logical and 2 possible answers
a <- 0
ifelse(a > 0, 1/a, NA)

a <- c(0, 1, 2, -4.5)
result <- ifelse(a > 0, 1/a, NA)
result

data(na_example)
sum(ia.na(na_example))

no_nas <- ifelse(is.na(na_example), 0, na_example)
sum(ia.na(no_nas))

z <- c(TRUE, FALSE, FALSE)
any(z)
all(z)