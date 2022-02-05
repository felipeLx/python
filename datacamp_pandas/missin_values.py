# DataFrama with missing values
dogs.isna()

# to check all rows sumarize
dogs.isna().any()

# counting missing values
dogs.isna().sum()

# can view by graphic
dogs.isna().sum().plot(kind="bar")
plt.show()

# removing missing
dogs.dropna()

# replace missing
dogs.fillna(0)