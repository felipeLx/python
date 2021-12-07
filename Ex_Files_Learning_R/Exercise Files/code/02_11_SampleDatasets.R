# File:     02_11_SampleDatasets.R
# Project:  LearningR

# INSTALL AND LOAD PACKAGES ################################

# Load base packages manually
library(datasets)  # For example datasets
?datasets
library(help = "datasets")

# SOME SAMPLE DATASETS #####################################

# iris data
?iris
iris

# UCBAdmissions
?UCBAdmissions
UCBAdmissions

# Titanic
?Titanic
Titanic

# state.x77
?state.x77
state.x77

#swiss
?swiss
swiss

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
