# File:     03_06_LineCharts.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# pacman must already be installed; then load contributed
# packages (including pacman) with pacman
pacman::p_load(pacman, tidyverse)

# Load base packages manually
library(datasets)  # For example datasets

# SINGLE TIME SERIES #######################################

# uspop
?uspop  # Get info about data
uspop   # Display data

?ts  # Get info about time-series objects

# Plot with default plot()
plot(uspop)

# Plot with options
uspop %>% 
  plot(
    main = "US Population 1790–1970 ",
    sub  = "(Source: datasets::uspop)",
    xlab = "Year",
    ylab = "Population (in millions)",
  )
abline(v = 1930, col = "lightgray")
text(1930, 10, "1930", col = "red3") 
abline(v = 1940, col = "lightgray")
text(1940, 2, "1940", col = "red3") 

# Plot with ts.plot()
?ts.plot
# Although this can be used for a single time series, plot
# is easier to use and is preferred.
ts.plot(uspop)

# Plot with plot.ts()
# More powerful alternative
?plot.ts
plot.ts(uspop)

# MULTIPLE TIME SERIES #####################################

# EuStockMarkets
?EuStockMarkets
EuStockMarkets

# Three different plot functions
plot(EuStockMarkets)     # Stacked windows
plot.ts(EuStockMarkets)  # Identical
ts.plot(EuStockMarkets)  # One window

# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons
detach("package:datasets", unload = TRUE)  # For base

# Clear plots
dev.off()  # But only if there IS a plot

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)
