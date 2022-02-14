"""
the same data may be interpreted diff depending on choice of bins
"""

"""
Bee Swarm plot
when sweeping the data into bins, we lose the actual values
ex.:
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)

each point on the plot represents the share
"""
sns.swarmplot(x=, y=, data=)
plt.xlabel()
plt.ylabel()

df.head(4)
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')