import pandas as pd

dogs = pd.DataFrame({
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [24, 24, 24, 17, 29, 2, 74],
    "date_of_birth":["2013-07-01", "2014-05-01", "2015-11-01", "2016-02-01", "2013-05-01", "2014-10-01", "2015-07-01"]
})
# pivot tables is another wat to calculate group summary statistics

dogs.pivot_table(values = "weight_kg", index = "color")
# values the column that you want to summarize
# index the column that you want to group by

# by default pivot_tables takes the mean value for each group
# if want diff sumarize statistics we can use the aggfunc arguments and pass it a function
import numpy as np

dogs.pivot_table(values = "weight_kg", index = "color", aggfunc = np.median)

# multiple statistics
dogs.pivot_table(values = "weight_kg", index = "color", aggfunc = [np.mean, np.median])

# pivot on two variables
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.pivot_table(values = "weight_kg", index = "color", columns= "breed")

# filling missing values
dogs.pivot_table(values = "weight_kg", index = "color", columns= "breed", fill_value=0)

# margins argument to True, the last row and last column of the pivot table contain the mean of all the values
# in the column or row, not including the missing values that were filled in with Os
dogs.pivot_table(values = "weight_kg", index = "color", columns= "breed", fill_value = 0, margins = True)
