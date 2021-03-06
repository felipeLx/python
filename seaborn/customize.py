# last chapter
# customize
"""
style = includes background and axes
options: white, dark, whitegrid, darkgrid, ticks

default: white
"""
sns.catplot(x="age", y="masculinity_important", 
            data=masculinity_data, hue="feel_masculine", 
            kind="point")

sns.set_style("whitegrid")

# changing the palette
sns.set_palette("RdBu")

sns.catplot(x="how_masculine", data=masculinity_data, kind="count", order=category_order)

# create your on palette
custom_palette = ["red", "green", "orange", "blue"]
sns.set_palette(custom_palette)

# changing the scale
sns.set_context()
# smallest to largest: "paper", "notebook", "talk", "poster"
sns.set_context("talk")


# exercise
sns.set_style("whitegrid")
sns.set_palette("Purples")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# exercise
sns.set_style("darkgrid")

# Set a custom color palette
custom_palette=["#39A7D0", "#36ADA4"]
sns.set_palette(custom_palette)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box", col="Group")
g.fig.suptitle("New Title", y=1.03)
g.set_titles("This is {col_name}")

g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
g.set(xlabel="New x Label", ylabel="New y Label")

plt.xticks(rotation=90)


# exercise
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", ylabel="Average MPG")


# Show plot
plt.show()