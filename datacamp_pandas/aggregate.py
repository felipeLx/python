import pandas as pd

dogs = pd.DataFrame({
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [24, 24, 24, 17, 29, 2, 74],
    "date_of_birth":["2013-07-01", "2014-05-01", "2015-11-01", "2016-02-01", "2013-05-01", "2014-10-01", "2015-07-01"]
})

# mean - to tell the center of your data
dogs["height"].mean()

# others:
# median() mode() max() min() var() std() sum() quantile()
dogs["date_of_birth"].min()

# the aggregate, or agg, method allows you to compute custom summary statistics
def pct30(column):
    return column.quantile(0.3) # computes the thirtieth percentile of a DataFrame column.

# now we can subset the weight column and call dog-agg, passing in the name of your function, pct30
dogs["weight_kg"].agg(pct30)

# summarize multiple columns
dogs[["weight_kg", "height"]].agg(pct30)

def pct40(column):
    return column.quantile(0.4)

# will return thirtieth and fortieth percentiles of the dogs weights
dogs["weight_kg"].agg([pct30, pct40])

# computing cumulative statistcs, example cumulative sum
dogs["weight_kg"]
dogs["weight_kg"].cumsum()

# other cummulative satistics
# cummax() cummin() cumprod()