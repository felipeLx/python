import pandas as pd
import numpy as np

ambassadors = pd.Series([
    'France', 'UK', 'UK', 'Italy', 'Germany', 'Germany'
], index = [
    'Gerard', 'Kim', 'Peter', 'Armando', 'Peter', 'Ammon'
])

ambassadors.duplicated()
ambassadors.duplicated(keep = 'last') # (keep = False)

ambassadors.drop_duplicates(keep = 'last')

players = pd.DataFrame({
    'Name': [
        'Kobe',
        'Gerard',
        'Michael',
        'Kobe'
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF'
    ]
})

players.duplicated()
players.duplicated(subset = ['Name'])
players.duplicated(subset = ['Name'], keep = 'last')

df_string = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I   T_2',
    ]
})

df_string['Data'].str.split('_')
df_string = df_string['Data'].str.split('_', expand = True)
df_string.columns = ['Year', 'Sex', 'Country', 'No Children']
# df_string['Years'].str.contains('\?')
# df_string['Country'].str.strip()
# df_string['Years'].str.replace(' ', '')
df_alter = df_string['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'))
print(df_alter)