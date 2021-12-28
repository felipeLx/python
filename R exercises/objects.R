# object
x <- 1
y <- 0
w <- -1

# can just the variable, most common: print(x)
ls()  # to show all the name of objects saved

# quadratic function
a <- 2
b <- -1
c <- -4
(-b + sqrt(b^2- 4*a*c)) / (2*a)
(-b - sqrt(b^2- 4*a*c)) / (2*a)
# in general do evaluate a function we use parentheses
log(8) # the argument is 8
log(1024, base=4)
# nested functions
log(exp(1))

help("log")

# to specific arguments, we use =
log(8, base=2)

# dataset avaliable in R
data()

# other pre-builds
pi
Inf