import pandas as pd

dogs = pd.DataFrame({
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [24, 24, 24, 17, 29, 2, 74],
    "date_of_birth":["2013-07-01", "2014-05-01", "2015-11-01", "2016-02-01", "2013-05-01", "2014-10-01", "2015-07-01"]
})

# create and adding columns can go by many names
dogs["height_m"] = dogs["height"]/100
# print(dogs)
dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"]**2

bmi_lt_100 = dogs[dogs["bmi"] < 100]
bmi_lt_100_height = bmi_lt_100.sort_values("height", ascending=False)

print(bmi_lt_100_height)

""" 
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness) 
"""

"""
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness ["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
"""