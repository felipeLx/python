import numpy as np

a = np.arange(4)

# vectorizing operation, will apply for all numbers in the array
a + 10

# to modify the array we need to add = signal
a += 100

b = np.arange(5)
# not alter the array, generate copy with plus 20 for each value
b + 20
print(b)

c = np.random.randint(100, size=(3,3))
print(c)