# File:     03_04_BoxPlots.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# pacman must already be installed; then load contributed
# packages (including pacman) with pacman
pacman::p_load(pacman, tidyverse)

# LOAD DATA ################################################

# Using the diamonds dataset from ggplot2
?diamonds  # Get information about the diamonds dataset
diamonds   # Display the beginning of the dataset

# BARPLOT OF FREQUENCIES ###################################

?plot     # Get info on "Generic X-Y Plotting
?boxplot  # Get info on the "Bar Plots" function

# Boxplot with defaults
boxplot(diamonds$price)

# Similar process using pipes
diamonds %>%
  select(price) %>%
  boxplot()

# Boxplot with options
diamonds %>%
  select(price) %>%
  boxplot(
    horizontal = T,  # Horizontal
    notch  = T,      # Confidence interval for median
    main   = "Boxplot of Price of Diamonds",
    sub    = "(Source: ggplot2::diamonds)",
    xlab   = "Price of Diamonds",
    col    = "#CD0000"  # red3
  )

# BOXPLOTS BY GROUP ########################################

# Boxplots by group using plot()
diamonds %>%
  select(color, price) %>%
  plot()

# Boxplots by group using boxplot()
diamonds %>%
  select(color, price) %>%
  boxplot(
    price ~ color,  # Tilde indicates formula
    data  = . ,     # Dot is placeholder for pipe
    col   = "#CD0000"
  )

# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons

# Clear plots
dev.off()  # But only if there IS a plot

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)
