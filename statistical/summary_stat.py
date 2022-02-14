# summary statistics: mean and median

import numpy as np
np.mean(dem_share_PA)
# is heavily influencer by outliers

# median: the middle value of data set
np.median(dem_share_PA)

mean_length_vers = np.mean(versicolor_petal_length)

# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')

# percentile
np.percentile(df_swing['dem_share'], [25,50,75])

import matplotlib.pyplot as plt
import seaborn as sns

_ = sns.boxplot(x=, y=, data=,)
plt.xlabel('xx')
plt.ylabel('yy')

percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()

sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')
