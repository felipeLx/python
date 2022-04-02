import pandas as pd
import numpy as np

df = pd.read_csv('df_rain_disaster.csv', sep=';', encoding='latin1', index_col = False, header=0)

# df_have_rain = df.loc[df['Rain (mm)'] > 7.6]
# df_have_rain = df_have_rain.loc[df_have_rain['Disasters'] > 1]
# print(df_have_rain.head())

# df_have_complete = df_have_rain[['State', 'Period', 'high_disasters', 'high_rain', 'count']]


df['high_disasters'] = np.where(df['Disasters'] > 1, 1, 0)
df['high_rain'] = np.where(df['Rain (mm)'] > 7.6, 1, 0)
df['count'] = 1
df_havy_rain = df[['high_disasters', 'high_rain', 'count']]
df_pivot = pd.pivot_table(df_havy_rain, values='count', index=['high_rain'], columns=['high_disasters'], aggfunc=np.sum)

# cases:
    # P(A) the probability of Rain > 10
    # P(B) the probability of Disasters > 2
    # P(A|B) the probability of Rain > 10, given Disasters > 2
print(df_pivot)
# conditional probability where disaster bigger than 2
"""
PA = (2367+7016)/(2367+7016+24+51)
PB = (51+7016)/(2367+7016+24+51)
PAB = (7016)/(2367+7016+24+51)

result = PAB/PB # 0.992783
print(result)
"""

# conditional probability where disaster bigger than 1
PA = (6061+9458)/(6061+9458+1355+1939)
PB = (9458+1939)/(6061+9458+1355+1939)
PAB = (9458)/(6061+9458+1355+1939)

result = PAB/PB # 0.992783
print(result)