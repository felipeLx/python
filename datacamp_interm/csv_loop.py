import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)
for val in brics: # will pick the columns name
    print(val)

for lab, row in brics.iterrows():
    print(lab)
    print(row)
    print(lab + ": " + row["capital"])
    #create series on every interation
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)
print(brics)

cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

for lab, row in cars.iterrows():
    print(lab + ": " + str(row["cars_per_cap"]))

# Code for loop that adds COUNTRY column
for car, row in cars.iterrows():
    cars.loc[car, "COUNTRY"] = (row["country"].upper())

cars["COUNTRY"] = cars["country"].apply(str.upper)
