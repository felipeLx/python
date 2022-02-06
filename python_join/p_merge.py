wards_census = wards.merge(census, on="ward")
print(wards_census(4))
print(wards_census.shape)
# (50,9)
# DataFrame with 50 rows and 9 columns

wards_census.columns
# return columns with _x or _y
# when the both columns contain the same column name

# suffixes
wards_census = wards.merge(census, on="ward", suffixes=('ward', '_cen'))

import pandas as pd

taxi_owners = pd.DataFrame({
    "rid": ["T6285","T4862","T1495","T4231","T5971"],
    "vid": [6285, 4862, 1495, 4231, 5971],
    "owner": ["AGEAN", "MANGIB", "FUNRIDE", "ALQSH", "EUNIFFORD"],
    "address": ["4536 N. ELSTON AVE.", "5717 N. WASHTENAW AVE.", "3351 W. ADDISON ST.", "6611 N. CAMPBELL AVE.", "3351 W. ADDISON ST." ],
    "zip": [60630, 60659, 60618, 60645, 60618]
})

taxi_veh = pd.DataFrame({
    "vid": [2767, 1411, 6500, 2746, 5922],
    "make": ["TOYOTA", "TOYOTA", "NISSAN", "TOYOTA", "TOYOTA"],
    "model": ["CAMRY", "RAV4", "SENTRA", "CAMRY", "CAMRY"],
    "year": [2013, 2017, 2019, 2013, 2013],
    "type": ["HYBRID","HYBRID","GAS", "HYBRID","HYBRID"],
    "owner": ["SEYED", "DESZY", "AGAPH", "MIDWEST", "SUMETTI"]
})

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=("_own", "_veh"))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

