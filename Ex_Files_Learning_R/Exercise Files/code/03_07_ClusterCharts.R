# File:     03_07_ClusterCharts.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# pacman must already be installed; then load contributed
# packages (including pacman) with pacman
pacman::p_load(pacman, rio, tidyverse)
# pacman: for loading/unloading packages
# rio: for importing data
# tidyverse: for so many reasons

# LOAD AND PREPARE DATA ####################################

# Save data to "df" (for "data frame")
# Rename outcome as "y" (if it helps)
# Specify outcome with df$y

df <- import("data/StateData.xlsx") %>%
  as_tibble() %>%
  select(state_code, 
    psychRegions,
    instagram:modernDance) %>% 
  mutate(psychRegions = as.factor(psychRegions)) %>%
  rename(y = psychRegions) %>%
  print()

# ANALYZE DATA #############################################

# By using standardized object and variable names, the same
# code can be reused for different analyses

# Calculate clusters
hc <- df %>%  # Get data
  dist %>%    # Compute distance/dissimilarity matrix
  hclust      # Compute hierarchical clusters

# Plot dendrogram
hc %>% plot(labels = df$state_code)

# Draw boxes around clusters
hc %>% rect.hclust(k = 2, border = "gray80")  # 2 boxes
hc %>% rect.hclust(k = 3, border = "gray60")  # 3 boxes
hc %>% rect.hclust(k = 4, border = "gray40")  # 4 boxes

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
