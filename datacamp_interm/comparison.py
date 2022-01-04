# numPy

# logical_and()
# logical_or()
# logical_not()

my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10  and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen > 17 or my_kitchen < 14)

# Double my_kitchen smaller than triple your_kitchen?
compare_kitchen = (2 * my_kitchen) < (3 * your_kitchen)
print(compare_kitchen)

x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10)) # FALSE

import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))


