import matplotlib.pyplot as plt

# create instagram
dog_pack["height_cm"].hist()
# the x-axis represents the heights of the dogs, y-axis represents the number of the dogs in each height range
plt.show()

# adjust the number of bars, or bins, using the "bins" argument
dog_pack["height_cm"].hist(bins=20)
# y-axis (0, 2, 4, 6, ....)

dog_pack["height_cm"].hist(bins=5)
# y-axis (0, 5, 10, 15, ....)

# bar-plots can reveal relationships between a categorical variable and a numeric variable, like breed and weight
avg_weight_by_breed = dog_pack.groupby("breed")["weight"].mean()
avg_weight_by_breed.plot(kind="bar")
plt.show()

# add title
avg_weight_by_breed.plot(kind="bar", title="Mean Weight by Dog Breed")
plt.show()

# line plots are great for visualization changes in numeric variables over time
sully.head()
sully.plot(x="date", y="weight", kind="line")
plt.show()

# rotate axis labels
sully.plot(x="date", y="weight", kind="line", rot=45)
plt.show()

# scatter plot viz* relationships between 2 numeric variables
dog_pack.plot(x="height", y="weight", kind="scatter")
plt.show()

# plot can be layered on top on one another
dog_pack[dog_pack["sex"] == "F"]["height"].hist()
dog_pack[dog_pack["sex"] == "M"]["height"].hist()
plt.legend(["F", "M"])
plt.show()

# transparency
dog_pack[dog_pack["sex"] == "F"]["height"].hist(alpha=0.7)
