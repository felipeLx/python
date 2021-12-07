2+2
1:100

a <- 1
2 -> b
c <- d <- e <- 3

print("Hello WOrld")
x <- c(1,2,5,9) # c combine
x

0:10
10:0
seq(10)
seq(30, 0, by=-3)

(y <- c(5,1,0,10))
is.vector(y)

# in R every single value is a vector

sqrt(64)
log(100)
log10(100)

# multidimencional matrix
m1 <- matrix(c(T, T, F, F, T, F), nrow = 2)
m1

m2 <- matrix(c("a", "b",
               "c", "d"),
                nrow=2,
                byrow=T)
m2

a1 <- array(c(1:24), c(8,3,1)) #dimensional (rows, columns, tables)
a1

vNumeric <- c(1,2,3)
vCharacter <- c("a", "b", "c")
vLogical <- c(T, F, T)

df1 <- cbind(vNumeric, vCharacter, vLogical) # will transform all to the same data type
df1

df2 <- as.data.frame(cbind(vNumeric, vCharacter, vLogical))
df2

o1 <- c(1,2,3)
o2 <- c("a", "b", "c", "d", "e")
o3 <- c(T, F, T, T, F)

list1 <- list(o1, o2, o3)
list1

list2 <- list(o1, o2, o3, list1)
list2

(coerce1 <- c(1, "a", TRUE))
typeof(coerce1)

(coerce2 <- 5)
typeof(coerce2)

(coerce3 <- as.integer(5))
typeof(coerce3)

# matrix to data frame
(coerce4 <- matrix(1:9, nrow = 3))
is.matrix(coerce4)

(coerce5 <- as.data.frame(matrix(1:9, nrow = 3)))
is.data.frame(coerce5)
