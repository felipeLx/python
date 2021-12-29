library(dslabs)
data(heights)
options(digits = 3) 

avg <- mean(heights$height)
ind <- heights$height > avg 
sum(ind) # 532

heights$sex

ind2 <- heights %>% filter(height > avg & sex == "Female")
nrow(ind2) # 31

ind3 <- heights$sex == "Female"
mean(ind3) # 0.227

heights$height[which.min(heights$height)] # 50

match(c(heights$height[which.min(heights$height)]), heights$height) # 1032

# Subset the sex column of the dataset by the index in 4b 
 # to determine the individual’s sex.
heights$sex[1032]

# Using the heights dataset, create a new column of heights in centimeters named ht_cm.
# Recall that 1 inch = 2.54 centimeters. Save the resulting dataset as heights2.
heights2 = mutate(heights, ht_cm = height * 2.54)
heights2$ht_cm[18] # 163
mean(heights2$ht_cm) # 174

females = filter(heights2, sex == "Female")
nrow(females) # 238
mean(females$ht_cm) # 165

data(olive)
head(olive)

plot(olive$palmitic, olive$palmitoleic)
# There is a positive linear relationship between palmitic and palmitoleic.

hist(olive$eicosenoic)
# The most common value of eicosenoic acid is below 0.05%.

boxplot(palmitic~region, data=olive)
# Which region has the highest median palmitic acid percentage?
# Southern Italy
# Which region has the most variable palmitic acid percentage?
# Southern Italy
