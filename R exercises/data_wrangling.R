# data wrangling
# dplyr - functionality for working with tables
murders <- mutate(murders, rate = total/population * 100000)

filtered <- filter(murders, rate <= 0.71)

new_table <- select(murders, state, region, rate)
filter(new_table, rate <= 0.71)

murders %>% 
  select(state, region, rate) %>% 
  filter(rate <= 0.71)

# create data_frames
grades <- data.frame(names = c("John", "Juan", "Jean", "Yao"),
                     exam_1 = c(95, 80, 90, 85),
                     exam_2 = c(90, 85, 85, 90),
                     stringsAsFactors = FALSE)
grades

# The default settings in R have changed as of version 4.0, and it is no longer
# necessary to include the code stringsAsFactors = FALSE in order to keep strings as
# characters. Putting the entries in quotes, as in the example, is adequate to keep 
# strings as characters. The stringsAsFactors = FALSE code is useful in certain other 
# situations, but you do not need to include it when you create data frames in this manner.

