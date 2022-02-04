""" 
summary statistics can be useful to compare different groups

you can gain many insights from summaries of individual groups
"""

import pandas as pd

dogs = pd.DataFrame({
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [24, 24, 24, 17, 29, 2, 74],
    "date_of_birth":["2013-07-01", "2014-05-01", "2015-11-01", "2016-02-01", "2013-05-01", "2014-10-01", "2015-07-01"]
})

dogs[dogs["color"] == "Black"]["weight_kg"].mean()

# group summaries
dogs.groupby("color")["weight_kg"].mean()
dogs.groupby("color")["weight_kg"].agg([min, max, sum])

# grouping to multi variables
dogs.groupby(["color", "breed"])["weight_kg"].mean()

# many groups, many summaries
dogs.groupby(["color", "breed"])[["weight_kg", "height"]].mean()