# line plot
# each plot point represents the same "thing" typically tracked over time

"""
common example: is tracking the value of a company's stock over time, as shown here
"""

sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line")

sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line", style="location", hue="location")

# setting the markers parameter equal to "True" will display a marker for each data point
# the marker will vary based on the subgroup you've set using the "style" parameter
# if you don't want the line styles to vary by subgroup, set the "dashes" parameter equal to "False"
sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line", style="location", hue="location",
            markers=True, dashes=False)

# line plot can also be used when you have more than one observation per x-value
# if a line plot is given multiple observations per x-value, it will aggregate them into a single summary measure

"""
Shaded region is the confidence interval
. assumes dataset is a random sample
. 95% confident that the mean is whithin this interval
. indicates uncertainly in our multiple
"""

# replacing confidence interval with standard deviation
sns.relplot(x="hour", y="NO_2_mean",
            data=air_df,
            kind="line",
            ci="sd")
ci="sd" # to make a shaded area
# turn off the confidence interval by setting the "ci" parameter equal to "None"

# exercise
sns.relplot(x="model_year", y="horsepower", markers=True, dashes=False,
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin") 

# recap
"""
FaceGrid - relplot() catplot() -> can create subplots
AxesSubplots - scatterplot() countplot() -> only create a single plot
"""
g = sns.catplot(x="model_year", y="horsepower",data=gdp_data, kind="box") 
g.fig.suptitle("New Title", y=1.03)
