import pandas as pd

brics = pd.read_csv("./brics.csv", index_col = 0)

brics["country"] #type Series
brics[["country", "capital"]] # type DataFrame

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

#pandas
#loc: label based
# iloc: integer position-based
brics.loc[["RU", "IN", "CH"]]
brics.loc[["RU"],["country", "capital"]]
brics[:, ["country"]]
brics.iloc[[1,2,3]]

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[:4])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#  loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index 

# Print out observation for Japan
print(cars)
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
print(cars)
print(cars.loc[['MOR'], ['drives_right']])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars.iloc[:,-1])

# Print out drives_right column as DataFrame
print(cars.iloc[:,[-1]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap', 'drives_right']])
