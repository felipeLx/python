pacman::p_load(pacman, rio, tidyverse)
df <- import("StateData.csv") %>%
  as_tibble() %>%
  select(state_code, 
         psychRegions,
         instagram.modernDance)  %>%
  mutate(psychRegions = as.factor(psychRegions))  %>%
  print()
