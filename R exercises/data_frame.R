# data.frames
# Most of the time when doing analysis in R you will be working with data.frames.
# data.frames are tabular, with column headings and rows of data, just like a CSV file.

mydata1 <- data.frame(site = c("A", "B", "C"),
                     temp = c(20, 30, 40))
mydata1
nrow(mydata1)

mydata <- read.csv("data.csv")
mydata

# We can return just one of the columns:
mydata$type
unique(mydata$type)
mydata[order(mydata$name),]

# We can access the individual cells of a data.frame with a new syntax element: [ and [:
mydata[1,] # First row
mydata[,1] # First column
mydata[1,1] # First row, first column
mydata[c(1,5),] # First and second row

?order # How to get help in R!
order(c(1, 2, 3))

# We can also return just certain rows, based upon criteria:
mydata[mydata$type == "fruit",]

# Another handy way to subset data.frame is with the subset function:
subset(mydata, type == "fruit") # Equivalent to mydata[mydata$type == "fruit",]

str(mydata)
summary(mydata)
