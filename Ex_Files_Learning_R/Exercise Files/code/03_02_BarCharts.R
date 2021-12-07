# File:     03_02_BarCharts.R
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
?barplot  # Get info on the "Bar Plots" function

# Shortest method to make a barplot
plot(diamonds$cut)

# Similar process using pipes
diamonds %>%
  select(color) %>%
  plot()

# Similar code using barplot(); doesn't work
diamonds %>%
  select(clarity) %>%
  barplot()  # Error: height must be a vector or a matrix

# Create frequency vector with table()
?table

# Try again with table()
diamonds %>%
  select(clarity) %>%
  table() %>%  # Put data in appropriate format
  barplot()

# Sort bars by decreasing values (not for ordinal X)
diamonds %>%
  select(clarity) %>%
  table() %>%
  sort(decreasing = T) %>%  # Sort table
  barplot()

# Add options to plot
diamonds %>%
  select(clarity) %>%
  table() %>%  # Put data in appropriate format
  barplot(
    main   = "Clarity of Diamonds",
    sub    = "(Source: ggplot2::diamonds)",
    horiz  = T,  # Draw horizontal bars
    ylab   = "Clarity of Diamonds",  # Flip axis labels
    xlab   = "Frequency",
    xlim   = c(0, 15000),  # Limits for X axis
    border = NA,  # No borders on bars
    col    = "#CD0000"  # red3
  )

# SIDE-BY-SIDE BARPLOT OF FREQUENCIES ######################

# 100% stacked bar
diamonds %>%
  select(color, clarity) %>%
  plot()

# Stacked bars: step 1: create table
df <- diamonds %>%
  select(color, clarity) %>%
  table() %>%
  print()  # Show table in Console

# Stacked bars: step 1: create graph
df %>%
  barplot(legend = rownames(.))  # Draw plot w/legend

# Side-by-side bar
df %>%
  barplot(
    legend = rownames(.),  # Dot is placeholder for pipe
    beside = T  # Put bars next to each other
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
