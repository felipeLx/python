from math import log
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('bmh')

n = np.linspace(1, 10)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,n**3,2**n]

# plot setup
plt.figure(figsize=(12,10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])

plt.legend(loc=0)
plt.ylabel('Relative runtime')
plt.xlabel('n')
