# vectors

# each column of a table is a Vector
# At 4:26 in the video, the code should read: codes[c("egypt","italy")]
# We may create vectors of class numeric or character with the concatenate function
codes <- c(380, 124, 818)
country <- c("italy", "canada", "egypt")

# We can also name the elements of a numeric vector
# Note that the two lines of code below have the same result
codes <- c(italy = 380, canada = 124, egypt = 818)
codes <- c("italy" = 380, "canada" = 124, "egypt" = 818)

# We can also name the elements of a numeric vector using the names() function
codes <- c(380, 124, 818)
country <- c("italy","canada","egypt")
names(codes) <- country

# Using square brackets is useful for subsetting to access specific elements of a vector
codes[2]
codes[c(1,3)]
codes[1:2]

# If the entries of a vector are named, they may be accessed by referring to their name
codes["canada"]
codes[c("egypt","italy")]

# to create a sequence
seq(1,10) # 1 2 3 .... 10
seq(1,10,2) # 1 3 5 ... 9

# subsetting: allow to access specific part of a vector
codes[2]
codes[c(1,3)]
