# File:     03_03_Histograms.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# pacman must already be installed; then load contributed
# packages (including pacman) with pacman
pacman::p_load(pacman, tidyverse)

# LOAD DATA ################################################

# Using the diamonds dataset from ggplot2
?diamonds  # Get information about the diamonds dataset
diamonds   # Display the beginning of the dataset

# HISTOGRAM ################################################

?hist

# Histogram with defaults
hist(diamonds$price)

# Histogram with options
hist(diamonds$price,
  breaks = 7,  # Suggest number of breaks
  main   = "Histogram of Price of Diamonds",
  sub    = "(Source: ggplot2::diamonds)",
  ylab   = "Frequency",
  xlab   = "Price of Diamonds",
  border = NA,  # No borders on bars
  col    = "#CD0000"  # red3
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
