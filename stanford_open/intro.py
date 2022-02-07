"""
Preparing the Data
- examine the data
- clean the data

"""
import pandas as pd

ri = pd.read_csv('/home/felipelx/Downloads/police.csv')
print(ri.head(3))

is_null_values = ri.isnull().sum()
print(is_null_values)

ri.drop('sarch_basis', axis='columns', inplace=True)
ri.dropna(subset=['seach_conducted', 'frisk_performed'], inplace=True)

###
# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(["county_name", "state"], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)