# covariance and pearson plot
# scatter plot
plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')
plt.xlabel('total votes')
plt.ylabel('percent')

# covariance is the mean of the product of these differences

# pearson correlation: covariance / (std of x) * (std of y)
    # it is a comparison of the variability in the data due to codependence (the covariance) to the variability inherent to each variable independently (their standard deviations)

plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
plt.xlabel('versicolor')
plt.ylabel('petal width')

covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor
r = pearson_r(versicolor_petal_width, versicolor_petal_length)

# Print the result
print(r)