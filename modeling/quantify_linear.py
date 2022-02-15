# quantify linear relationship

"""
correlations
= 1 , very correlation
= 0.03 , no correlation
= 0.54 , not clear
"""

# Mean
mean = sum(x)/len(x)

# Deviation, sometimes called centering
dx = x - np.mean(x)

# Variance
variance = np.mean(dx * dx)

# Standard Deviation
stdev = np.sqrt(variance)

# Covariance
    # Deviations of 2 variables
dx = x - np.mean(x)
dy = y - np.mean(y)
    # Co-vary means to vary together
deviation_products = dx*dy
"""
For each deviation product, if both x and y are varying in the same *direction* the result is positive
The average of those products will be larger if both variables change in the same direction more ofter than not.

Correlation
if we divide each deviation by the variables standard deviation, the result is the covariance of the normalized deviations , or "correlation"
"""
zx = dx/np.std(x)
zy = dy/np.std(y)

# Mean of the normalize deviations
correlation = np.mean(zx * zy)
# correlation -1 to 1
# positive: correlated means as one variable goes up, the other goes up
# negative: correlated means as one goes up, the other goes down

# Compute the deviations by subtracting the mean offset
dx = x - np.mean(x)
dy = y - np.mean(y)

# Normalize the data by dividing the deviations by the standard deviation
zx = dx / np.std(x)
zy = dy / np.std(y)

# Plot comparisons of the raw data and the normalized data
fig = plot_cdfs(dx, dy, zx, zy)

# Compute the covariance from the deviations.
dx = x - np.mean(x)
dy = y - np.mean(y)
covariance = np.mean(dx * dy)
print("Covariance: ", covariance)

# Compute the correlation from the normalized deviations.
zx = dx / np.std(x)
zy = dy / np.std(y)
correlation = np.mean(zx * zy)
print("Correlation: ", correlation)

# Plot the normalized deviations for visual inspection. 
fig = plot_normalized_deviations(zx, zy)

# Complete the function that will compute correlation.
def correlation(x,y):
    x_dev = x - np.mean(x)
    y_dev = y - np.mean(y)
    x_norm = x_dev / np.std(x)
    y_norm = y_dev / np.std(y)
    return np.mean(x_norm * y_norm)

# Compute and store the correlation for each data set in the list.
for name, data in data_sets.items():
    data['correlation'] = correlation(data['x'], data['y'])
    print('data set {} has correlation {:.2f}'.format(name, data['correlation']))

# Assign the data set with the best correlation.
best_data = data_sets['A']