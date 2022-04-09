import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/worldcup-1930-2018.csv')
# print(df.isna().sum())

# prepare data
conditions = [df['Home Team Goals']> df['Away Team Goals'], df['Home Team Goals']== df['Away Team Goals'], df['Home Team Goals']< df['Away Team Goals']]
choices = [df['Home Team Name'], 'Draw', df['Away Team Name']]

df['Winner'] = np.select(conditions, choices)

df['Points'] = np.where(df['Winner'] == 'Draw', 1, 3)
# df.to_csv('data/data_processed.csv')
print(df.head())

df_group = df.groupby(['Winner', 'Year'], as_index=False)['Points'].sum().sort_values(by='Year')
                                                                                                                                                                                        
print(df_group.head())
#fig = sns.scatterplot(x='Year', y='Winner', data=df, hue='Winner')

#plt.show()
