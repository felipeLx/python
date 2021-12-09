?diamonds
diamonds %>%
  select(color, price) %>%
  boxplot(
    price ~ color,
    data = . ,
    main = "Diamonds Price",
    sub = "(Source:ggplot2::diamonds)",
    xlab = "Price",
    col = "#CD0000"
  )
