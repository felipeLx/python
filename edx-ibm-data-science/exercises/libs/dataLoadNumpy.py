import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# %matplotlib inline

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Create a python list
a = ["0", 1, "two", "3", 4]

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])


# Slicing the numpy array
c = np.array([20, 1, 2, 3, 4])
c
d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c

# Create the index list
select = [0, 2, 3]

# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

e = np.array([0, 1, 2, 3, 4])
e
print(e.size)
print(e.ndim)
print(e.shape) #size
print(e.mean())
print(e.std())
print(e.max())
print(e.min())

u = np.array([1, 0])
u
v = np.array([0, 1])
v

# Numpy Array Addition
z = u + v
z

y = np.array([1, 2])
y

# Numpy Array Multiplication
z = 2 * y
z

# Calculate the production of two numpy arrays
z = u * v
z

# Calculate the dot product
np.dot(u, v)

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

u = np.array([1, 0])
v = np.array([0, 1])
z = u -v
z

# exercise
'''
Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together:
'''
j = [1,2,3,4,5]
k = [1,0,1,0,1]
l = np.array(j) * np.array(k)
l
print(l)

g = np.array([-1,1])
h = np.array([1,1])
Plotvec2(g,h)
print('the dot value of g and h is: ', np.dot(g,h))

m = np.array([1,1])
n = np.array([0,1])
Plotvec2(m,n)
print('the dot value of m and n is: ', np.dot(m,n))