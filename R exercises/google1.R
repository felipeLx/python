View(penguins)
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(color=species))

#my comment to print
print("coding in R")

first_variable <- "this is my variable"
second <- 12.5

# vector, a group of data elements of the same type stored in a sequence in R
vec_1 <- c(13, 48.6, 17, 2, 101)
vec_1

# pipe, a tool in R expressing a sequence of multiple operations, represented with "%>%"
# its used to apply the output of a function into another function

ToothGrowth %>%
  filter(dose == 0.5) %>%
  arrange(len)

