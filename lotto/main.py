import pandas as pd
import numpy as np

df = pd.read_csv('/home/felipelx/Downloads/loto_facil.csv', sep=';', header=0)

# sort values for each row
df_sort = pd.DataFrame(np.sort(df.values, axis=1), columns=df.columns)

# df_sort.to_csv('sort.csv', sep=';', index=False)

df_agg = pd.DataFrame(df_sort.groupby(['bola 1'], as_index=False).agg(['count', 'mean', 'std', 'min', 'max']))
print(df_agg.head(15))

