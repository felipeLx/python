list_a = ["Hello", "New"]

def my_list(lst, arg):
    lst.append(arg)
    return ' , '.join(lst)
    

print(my_list(list_a, "World"))


import pandas as pd

df = pd.read_csv('/home/felipelx/Downloads/sales.csv')

df = df.sort_values(by='SALES', ascending=False)
print(len(df))

df2 = df.copy()
print(len(df2))

# df.to_csv('sales.csv')
print(df.head())
df2 = df2[(df2['SALES'] >= 11886.60) & (df2['SALES'] < 14082.80)]
print(df2.sort_values(by='SALES', ascending=False))