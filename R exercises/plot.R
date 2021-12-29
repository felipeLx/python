# plot - visualization
population_in_millions <- murders$population/10^6
total_gun_murders <- murders$total
plot(population_in_millions, total_gun_murders)

# histograms
hist(murders$rate)
# check the biggest number in hist
murders$state[which.max(murders$rate)]

# boxplot
boxplot(rate~region, data = murders)
