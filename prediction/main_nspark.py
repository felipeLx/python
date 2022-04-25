import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_sample = pd.read_csv("/home/felipelx/Downloads/test/prevision/sample_submission.csv", header=0)
df_train = pd.read_csv("/home/felipelx/Downloads/test/prevision/sales_train.csv", header=0)
df_train['avg_item_price'] = df_train.groupby('date', as_index=False)['item_price'].transform('mean')
df_train['item_sold'] = df_train.groupby('date', as_index=False)['item_cnt_day'].transform('sum')
df_train['item_count'] = df_train.groupby('item_id', as_index=False)['item_id'].transform('count')

df_full = pd.merge(df_train, df_sample, on='date', how='left')
product_uniques = df_train['item_id'].unique()
# print(product_uniques)

# fig, ax = plt.subplots()

# check scatter plot chart to see the trend
# plt.scatter(df_train['avg_item_price'], df_train['item_sold'])

# sns.countplot(x=product_uniques)
# plt.show()

corr = df_train.corr()
print(corr)

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)

fig, ax = plt.subplots()
plot_timeseries(ax, df_train['date'], df_train['avg_item_price'], 
                'blue', 'Time', 'Avg Price')
plt.show()