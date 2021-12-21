import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})

df['Sex'].unique()
df['Sex'].value_counts()

df['Sex'].replace('D', 'F')
df['Sex'].replace({'D':'F', 'N': 'M'})

df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
})

df[df['Age'] > 100]
df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
print(df)