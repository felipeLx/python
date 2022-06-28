"""
Which of the following conditions should be met in order to apply gradient descent?
    The error function should be differentiable
    The error function should be continuos

The sigmoid function is defined as sigmoid(x) = 1/(1+e^-x). If the score is defined by 4x1 + 5x2 - 9 = score, then which of the following points has exactly a 50% probability of being blue or red?
    (1,1)
    (-4, 5)

The Softmax Function
Which is the equivalent of the sigmoid activation function, but when the problem has 3 or more classes.
"""
import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    return np.exp(L)/np.sum(np.exp(L))

"""
One-hot encoding
transform class that is not a number in a tabular format

Animal Duck? Beaver? Walrus?
duck    1       0       0
beaver  0       1       0
walrus  0       0       1
"""

"""
Maximum Likelihood Estimation
pick the model that gives the existing labels the highest probability

Maximize probability: log(ab) = log(a) + log(b)
a good model give us a low cross entropy and a bad model will give us a high cross entropy.

Cross-Entropy
connection between probabilities and error functions.
small cross-entropy - events happen based on the probability
large cross-entropy - event don't happen based on the probability
"""
import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y*np.log(P) + (1-Y)*np.log(1-P))

"""
If a point is well classified, we will get a small gradient. And if it's poorly classified, the gradient will be quite large.

The gradient descent step simply consists in subtracting a multiple of the gradient of the error function at every point, then this updates the weights in the following way:
w' = w + alpha(y - ŷ)x
b' = b + alpha(y - ŷ)

learning rate = 1/m * alpha (calling alpha)
"""