# File:     02_07_Comments.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# Load base packages manually
library(datasets)  # For example datasets

# LOAD AND PREPARE DATA ####################################

?iris
df <- iris
head(df)

# COMMENT OUT LINES ########################################

# Use comments to disable commands
hist(df$Sepal.Width,
  # col  = "#CD0000",  # red3
  # border = NA,  # No borders
  main = "Histogram of Sepal Width",
  xlab = "Sepal Width (in cm)")

# THIS IS A LEVEL 1 HEADER #################################

## This Is a Level 2 Header ================================

### This is a level 3 header. ------------------------------

# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
detach("package:datasets", unload = TRUE)  # For base

# Clear plots
dev.off()  # But only if there IS a plot

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)