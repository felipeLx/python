# scatter plot compare the values of different variables across observations
# sometime call bi-variate comparison
ax.scatter(climate_change["co2"], climate_change["relative_temp"])
ax.set_xlabel("CO2")
ax.set_ylabel("Relative temp")
plt.show()

# first argument: correspond to the distance along the x-axis
# second argument: correspond to the height along the y-axis

# customize scatter plot
eighties = climate_change["1980-01-01": "1989-12-31"]
nineties = climate_change["1990-01-01": "1999-12-31"]
fig, ax = plt.subplots()

# to show 2 bivariate comparisons
ax.scatter(eighties["co2"], eighties["relative_temp"], color="red", label="eighties")
ax.scatter(nineties["co2"], nineties["relative_temp"], color="blue", label="nineties")

# we can select these parts of the data using the time-series indexing
ax.set_xlabel("CO2")
ax.set_ylabel("Relative temp")
plt.show()

# enconding a third variable by color
# continuous variable
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)
ax.set_xlabel("CO2")
ax.set_ylabel("Relative temp")
plt.show()

# add this line of code before the plotting code, the figure style will look completely different
plt.style.use("ggplot")
# will emulates the stype of the R library ggplot
# when use this code will be apply for all graphics below that

# to back to default
ptl.style.use("default")
# https://matplotlib.org/gallery/style_sheets/style_sheets_refer

# good options color: "seaborn-colorblind" or "tableau-colorbind10"
# greuscale to print
