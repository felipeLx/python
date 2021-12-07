# File:     03_05_Scatterplots.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# pacman must already be installed; then load contributed
# packages (including pacman) with pacman
pacman::p_load(pacman, rio, tidyverse)

# LOAD AND PREPARE DATA ####################################

df <- import("data/StateData.xlsx") %>%
  as_tibble() %>%
  select(state_code, 
    psychRegions,
    instagram:modernDance) %>% 
  mutate(psychRegions = as.factor(psychRegions)) %>%
  print()

# SCATTERPLOTS #############################################

df %>%
  select(instagram:modernDance) %>% 
  plot()  # Plot all associations

# Bivariate scatterplot with defaults
df %>%
  select(scrapbook:modernDance) %>% 
  plot()

# Bivariate scatterplot with options
df %>%
  select(scrapbook:modernDance) %>% 
  plot(
    main = "Scatterplot of Google Searches by State",
    xlab = "Searches for \"scrapbook\"",
    ylab = "Searches for \"modern dance\"",
    col  = "gray",  # Color of points
    pch  = 20,      # "Plotting character" (small circle)
  )

?pch  # See plotting characters

# Add fit linear regression line (y ~ x) 
df %>%
  lm(modernDance ~ scrapbook, data = .) %>%
  abline()

# REMOVE OUTLIER ###########################################

# Identify outlier
df %>%
  select(state_code, scrapbook) %>%
  filter(scrapbook > 4) %>%  # Select outlier
  print()

# Bivariate scatterplot without outlier
df %>%
  select(scrapbook:modernDance) %>% 
  filter(scrapbook < 4) %>%  # filter out outlier
  plot(
    main = "Scatterplot of Google Searches by State",
    xlab = "Searches for \"scrapbook\"",
    ylab = "Searches for \"modern dance\"",
    col  = "gray",  # Color of points
    pch  = 20,      # "Plotting character" (small circle)
  )

# Add fit line without outlier
df %>%
  filter(scrapbook < 4) %>%  # filter out outlier
  lm(modernDance ~ scrapbook, data = .) %>%
  abline()

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
