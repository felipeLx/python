z = 5
if z % 2 == 0:
    print('checking ' + str(z))
    print('z is even')
#no output

if z % 2 == 0:
    print('checking ' + str(z))
else:
    print('z is even')

if z % 2 == 0:
    print(str(z) + ' is divided per 2')
elif z % 3 == 0:
    print(str(z) + ' is divided per 3')
else:
    print('neight per 2 or 3')

import pandas as pd
brics = pd.read_csv("./brics.csv", index_col=0)

# which country with area over 8 millons km2
# 3 steps: select area, do comparison, use result
brics["area"]
brics.loc[:,"area"]
brics.iloc[:,2]

is_huge = brics["area"] > 8
brics[is_huge]

import numpy as np
np.logical_and(brics["area"] > 8, brics["area"] > 10)
brics[np.logical_and(brics["area"] > 8, brics["area"] > 10)]

cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

#one line
sel = cars[cars["drives_right"] == True]

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars["cars_per_cap"] > 500]

cpc = cars["cars_per_cap"]
between = np.logical_and(cpc > 100, cpc < 500)
# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[between]

