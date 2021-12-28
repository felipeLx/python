# vector arithmetric
murders$state[which.max(murders$population)]

heights <- c(69, 62, 66, 70, 70, 73, 67, 73, 67, 70)
# convert to cm
heights * 2.54

murder_rate <- murders$total/murders$population * 100000

murders$state[order(murder_rate, decreasing = TRUE)]

# Calculate the average murder rate in the US 
mean(murder_rate)

# Assign city names to `city` 
city <- c("Beijing", "Lagos", "Paris", "Rio de Janeiro", "San Juan", "Toronto")

# Store temperature values in `temp`
temp <- c(35, 88, 42, 84, 81, 30)

# Convert temperature into Celsius and overwrite the original values of 'temp' with these Celsius values
temp <- (5/9) * (temp -32)
print(temp)
# Create a data frame `city_temps` 
city_temps <- data.frame(name = city, temperature=temp)
print(city_temps)

# Define an object `x` with the numbers 1 through 100
x <- seq(1:100)
# Compute the sum 
sum(1/(x^2))