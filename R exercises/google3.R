penguins %>%
  select(-species)

penguins %>%
  rename(island_new=island)

rename_with(penguins, tolower)
clean_names(penguins)

penguins %>% group_by(island) %>% drop_na() %>% summarise(mean_bill_length_mm = mean(bill_length_mm))

penguins %>% group_by(species, island) %>% drop_na() %>% summarise(max_bl = max(bill_length_mm), mean_bl = mean(bill_length_mm)) 
