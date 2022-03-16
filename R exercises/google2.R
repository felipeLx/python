# first calculation
quarter_1 <- 35657.98
quarter_2 <- 43810.55
midyear <- quarter_1 + quarter_2
midyear
year_sale <- midyear * 2

data('ToothGrowth')
View(ToothGrowth)

filtered_tg <- filter(ToothGrowth,dose==0.5)
View(filtered_tg)

arrange(filtered_tg, len)
arrange(filter(ToothGrowth, dose == 0.5), len)

filtered_toothgrow <- ToothGrowth %>%
  filter(dose == 0.5) %>%
  group_by(supp) %>%
  summarize(mean_len = mean(len, na.rm = T), .group="drop")
View(filtered_toothgrow)
