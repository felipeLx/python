import numpy as np 
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a
A = np.array(a)
A

# Access the element on the second row and third column
A[1, 2]
# Access the element on the second row and third column
A[1][2]
# Access the element on the first row and first and second columns
A[0][0:2]

# Create a numpy array X and Y
X = np.array([[1, 0], [0, 1]]) 
X
Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y
Z = X + Y
Z

# Create a matrix D and E
D = np.array([[0, 1, 1], [1, 0, 1]])
D
E = np.array([[1, 1], [1, 1], [-1, 1]])
E
F = np.dot(D,E)
F
print(F)