library(tidyverse)
library(dslabs)
library(dplyr)
data(murders)

murders %>%
  ggplot(aes(population, total, label=abb, color=region)) +
  geom_label()


  