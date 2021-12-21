#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#matplotlib inline

x = np.arange(-10, 11)
plt.figure(figsize = (12,6))
plt.title('My nice plot')
plt.subplot(1,2,1) #row, column, panel selected
plt.plot(x, x**2)
plt.plot(x, -1* (x ** 2))
plt.legend(['X²', 'Vertical lines'])
plt.xlabel('X')
plt.ylabel('X squared')
plt.show()