#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11)
fig, axes = plt.subplots(figsize=(12,6))
axes.plot(
    x, (x ** 2 ), color = 'red', linewidth = 3,
    marker = 'o', markersize = 8, label= '-X^2')

axes.plot(x, -1 * (x ** 2), 'b--', label = '-X^2')
axes.set_xlabel('X')
axes.set_ylabel('X Squared')

axes.set_title("My Plot")
axes.legend()
fig

axes.plot(x, x+0, linestyle = 'solid')
axes.plot(x, x+1, linestyle = 'dashed')
axes.plot(x, x+2, linestyle = 'dashdot')
axes.plot(x, x+3, linestyle = 'dotted')

axes.set_title('My Plot')


# grid plot
plt.figure(figsize = (14,6))
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax1 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax1 = plt.subplot2grid((3,3), (1,2), colspan=3)
ax1 = plt.subplot2grid((3,3), (2,0))
ax1 = plt.subplot2grid((3,3), (2,1))

# scater plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (20 *np.random.rand(N))**2 # 0 to 15 point radii

plt.figure(figsize=(14,6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
plt.colorbar()

plt.show()

#Histogram
values = np.random.randn(1000)
plt.subplots(figsize = (12,6))
plt.hist(values, bins=100, alpha=0.8, histtype='bar', color='steelblue', edgecolor='green')
plt.xlim(xmin=5, xmax=5)
plt.show()
fig.savefig('hist.png')

# combine plots
values2 = np.random.randn(500)
plt.subplots(figsize=(12,6))
plt.hist(values, bins=100, alpha=0.8, density=1, histtype='bar', color='steelblue', edgecolor='green')
plt.plot(values2, density(values2), color='#FF7F00', linewidth=3.0)
plt.xlim(xmin=-5, xmax=5)
plt.show()

# bar plot
Y = np.random.rand(1,5)[0]
Y2 = np.random.rand(1,5)[0]

plt.figure(figsize=(12,4))
barWidht = 0.5
plt.bar(np.arange(len(Y)), Y, width=barWidht, color='#00b894')
plt.show()