import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/felipelx/Downloads/results.csv')
# print(df.isna().sum())

# prepare data
conditions = [df['home_score']> df['away_score'], df['home_score']== df['away_score'], df['home_score']< df['away_score']]
choices = [df['home_team'], 'Draw', df['away_team']]

df['Winner'] = np.select(conditions, choices)

df['Points'] = np.where(df['Winner'] == 'Draw', 1, 3)
df['home_team'] = df['home_team'].replace({'United States': 'USA'})
df['away_team'] = df['away_team'].replace({'United States': 'USA'})

correlation = df.corr()
print(correlation)
# df.to_csv('data/data_processed.csv')
# print(df.head())

# df_group = df.groupby(['Winner', 'Year'], as_index=False)['Points'].sum().sort_values(by='Year')
                                                                                                                                                                                        
# print(df_group.head())
#fig = sns.scatterplot(x='Year', y='Winner', data=df, hue='Winner')

#plt.show()
