
a3 <- paste("apple", "orange")
a3

a4 <- max(abs(c(-5, 0, 5)))
a4

# which of the following expressions would be a correct way to combine them into one data.frame

z1 <- data.frame(z = 1:2)
z2 <- data.frame(z = 3)
rbind(z1, z2)

# Which expression(s) return a data.frame with rows where y is greater than 5

z3 <- data.frame(y = 1:10)
a5 <- subset(z3, y > 5)
a5

# R as a calculator: + - * / > >= %% %/% etc
# comparison
2 == 1
2 == 2
"apple" == "apple"
"orange" == "apple"
