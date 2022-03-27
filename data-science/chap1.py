import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb, factorial

# geometric series: is the sum of a finite or an infinite sequence of numbers with a constant ratio between sucessive terms. is useful when handling situations such as N-1 failures followed by a success.
p = 1/2
n = np.arange(0,10)
X = np.power(p, n)

plt.bar(n, X)
# plt.show()

# binomial series: is instrumental in algebra when handling polynomials such as (a+b)² or (1+n)³. It provides a valuable formula when computing these powers.
n = 10
k = 2
comb(n, k)
factorial(k)

# Taylor approximation os a geometric-based approximation. It approximates the function according to the offset slope, curvature, and so on. The Taylor series has an infinite number of terms.
# An immediate application of the Taylor approximation s to derive the exponential series.

# data analysis problems: 
    # the observable vector Y
    # the variable vector X
    # the coefficient B
# y = Bn Xn

# inner product of a vectors
x = np.array([[1], [0], [-1]])
y = np.array([[3], [2], [0]])
z= np.dot(np.transpose(x), y)
print(z)

# norm: the norm give us essentially the length of the vector
x = np.array([[1], [0], [-1]])
n_norm = np.linalg.norm(x) # using the norm, one can define an angle called the cosine angle between two vectors.

# the difference between the cosine angle and the basic inner product is the normalization in the denominator.

# W: the geometric of the weighted l2-norm is determined by the matrix W.
W = np.array([[1,2,3], [4,5,6], [7,8,9]])
z = np.dot(x.T, np.dot(W, x))
print(z)

# matrix calculus: differentiation of matrices and vectors. To find the min or max of a scalar function with a vector input.
# matrix inversion
X = np.array([[1, 3], [-2,7], [0,1]])
XtX = np.dot(X.T, X)
XtXinv = np.linalg.inv(XtX)
print(XtXinv)

# when we are more interested om solving a linear equation
X = np.array([[1, 3], [-2,7], [0,1]])
y = np.array([[2], [1], [0]])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
print(beta)

# permutation: consider a set of n distinct balls. Suppose we want to pick k balls from the set without replacement. How many ordered configurations can we obtains?
# permutation: the number of choices is reduced in every state.

