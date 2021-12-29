
# Add the necessary columns
murders <- mutate(murders, rate = total/population * 100000, rank = rank(-rate))

# Filter to show the top 5 states with the highest murder rates
filter(murders, rank <= 5)

# Use filter to create a new data frame no_south
no_south <- filter(murders, region != 'South')
# Use nrow() to calculate the number of rows
nrow(no_south)

# Create a new data frame called murders_nw with only the states from the northeast and the west
murders_nw <- filter(murders, region %in% c('Northeast', 'West'))
# Number of states (rows) in this category 
nrow(murders_nw)

# add the rate column
murders <- mutate(murders, rate =  total / population * 100000, rank = rank(-rate))

# Create a table, call it my_states, that satisfies both the conditions 
my_states = filter(murders, rate <= 1 & region %in% c('Northeast','West'))
# Use select to show only the state name, the murder rate and the rank
select(my_states, state, rate, rank)

# show the result and only include the state, rate, and rank columns, all in one line, in that order
murders %>% 
  select(state, rate, rank) %>% 
  filter(rate <= 1 & murders$region %in% c('Northeast','West')) 

# Create new data frame called my_states (with specifications in the instructions)
my_states <- murders %>% 
  mutate(rate =  total / population * 100000, rank = rank(-rate)) %>% 
  filter(region %in% c('Northeast', 'West') & rate < 1) %>%
  select(state, rate, rank)

population_in_millions <- murders$population/10^6
total_gun_murders <- murders$total

plot(population_in_millions, total_gun_murders)

# Transform population (not population in millions) using the log10 transformation and save to object log10_population
log10_population <- log10(murders$population)
log10_population
# Transform total gun murders using log10 transformation and save to object log10_total_gun_murders
log10_total_gun_murders = log10(total_gun_murders)
# Create a scatterplot with the log scale transformed population and murders 
plot(log10_population, log10_total_gun_murders)

# Store the population in millions and save to population_in_millions 
population_in_millions <- murders$population/10^6

# Create a histogram of this variable
hist(population_in_millions)

# Create a boxplot of state populations by region for the murders dataset
boxplot(population~region, data = murders)