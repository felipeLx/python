# quantitative comparisons between parts of the data
import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('medals.csv', index_col=0)
fig, ax = plt.subplots()

ax.bar(medals.index, medals['Gold'])
plt.show()

# when name of the x-axis overlap
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')

# add other medals
ax.bar(medals.index, medals['Silver'], botton=medals['Gold'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')

# add other medal
ax.bar(medals.index, medals['Bronze'],
    bottom=medals['Gold']+ medals['Silver'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')

# add label
ax.bar(medals.index, medals['Gold'], label="Gold")
ax.bar(medals.index, medals['Silver'], botton=medals['Gold'], label="Silver")
ax.bar(medals.index, medals['Bronze'],
    bottom=medals['Gold']+ medals['Silver'], label="Bronze")
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')
ax.legend()
ax.show()
