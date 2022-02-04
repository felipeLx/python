import pandas as pd

dogs = pd.DataFrame({
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [24, 24, 24, 17, 29, 2, 74],
    "date_of_birth":["2013-07-01", "2014-05-01", "2015-11-01", "2016-02-01", "2013-05-01", "2014-10-01", "2015-07-01"]
})

# to remove duplicate from DataFrame using specific column
dogs.drop_duplicates(subset="name")

# best practice is to use multiple columns using a list
unique_dogs = dogs.drop_duplicates(subset=["name", "breed"])

# count and sort
unique_dogs["breed"].value_counts()
unique_dogs["breed"].value_counts(sort=True)

# normalize argument is used to find the proportional by the total
unique_dogs["breed"].value_counts(normalize=True)