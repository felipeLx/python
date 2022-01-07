error = 50

while error > 1:
    error = error/4
    print(error)

offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
      offset = offset - 1
    else :
      offset = offset + 1
    print(offset)


seq = [1.73, 1.68, 1.71, 1.89]
for var in seq:
    print(seq)

# to print the index
for index, var in enumerate(fam):
    print('index ' + str(index) + ': ' + str(var))

for i in "door":
    print(i.capitalize())

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print("room " + str(index) + ":" + str(a))

for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for i in house:
    print("the " + i[0] + " is " + str(i[1]) + " sqm")


world = {
        "afghanistan": 30.55,
        "albania": 2.77,
        "algeria": 39.21 }
for key, value in world.items():
    print(key + "--" + str(value))


import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79)]
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7)]

bmi = np_weight/np_height **2
for val in bmi:
    print(val)

meas = np.array([np_height, np_weight])
for val in meas:
    print(val)

# to print each element on array
for val in np.nditer(meas):
    print(val)

# dictionary: use the items() method to define the sequence in the for loop
for key, val in my_dict.items():
# numpy array: use the nditer() function to specify the sequence
for val in np.nditer(my_array):

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, val in europe.items():
    print("the capital of " + key + " is " + val)

# dealing with a 1D NumPy array
for x in my_array:
# dealing with a 2D NumPy array
for x in np.nditer(my_array):

# For loop over np_height
for i in np_height:
    print(str(i) + " inches")

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)
