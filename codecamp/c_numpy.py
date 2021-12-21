import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# select value from row index 1
a[1]
# A[d1,d2,d3,d4]

# select value from column index 1 and row index 0
a[1,0]

# like slice where the last index is not considered
print(a[0:2])

# select every row and then select the first to dimensions
a[:, :2]

b = np.array([1,2,3,4])
b.sum()
b.mean()
b.std()
b.var()

# can use math operation with matrix
a.sum()
a.sum(axis = 0)