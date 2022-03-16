data(quartet)
head(quartet)

quartet %>%
  group_by(set) %>%
  summarize(mean(x), sd(x), mean(y), sd(y),cor(x,y))

df = read_csv("hotel_bookings.csv")
head(df)