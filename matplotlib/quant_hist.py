# histogram, show us the entire distribution of values within a variable
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar("Rowing", mens.rowing["Height"].mean())
ax.bar("Gymnastics", mens.gym["Height"].mean())

# histogram would instead show the full distribution of values within each variable
ax.hist(mens.rowing['Height'], label="Rowing")
ax.hist(mens_gym['Height'], label="Gymnastics")
ax.set_xlabel("Height")
ax.set_ylabel("# of observation")
ax.legend()
plt.show()

# how matplot decide how to devide the data up into the diff bars
"""
by default the number of bars or bins in a histogram is 10
"""
ax.hist(mens.rowing['Height'], label="Rowing", bins=5)
ax.hist(mens_gym['Height'], label="Gymnastics", bins=5)

# we can provide a set of numbers
ax.hist(mens.rowing['Height'], label="Rowing", bins=[150, 160, 170, 180])
ax.hist(mens_gym['Height'], label="Gymnastics", bins=[150, 160, 170, 180])

# change the type of the histogram
ax.hist(mens.rowing['Height'], label="Rowing", bins=[150, 160, 170, 180], histtype="step")
ax.hist(mens_gym['Height'], label="Gymnastics", bins=[150, 160, 170, 180], histtype="step")


fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()