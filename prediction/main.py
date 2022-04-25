# Demand calculation: The forecast is evaluated by the root mean squared error (RMSE)
from pyspark.sql import SparkSession
from matplotlib import pyplot as plt

spark = SparkSession.builder.appName("prediction").getOrCreate()

df_category = spark.read.csv("/home/felipelx/Downloads/test/prevision/item_categories.csv", header=True, inferSchema=True)
df_items = spark.read.csv("/home/felipelx/Downloads/test/prevision/items.csv", header=True, inferSchema=True)
df_train = spark.read.csv("/home/felipelx/Downloads/test/prevision/sales_train.csv", header=True, inferSchema=True)
df_sample = spark.read.csv("/home/felipelx/Downloads/test/prevision/sample_submission.csv", header=True, inferSchema=True)
df_shops = spark.read.csv("/home/felipelx/Downloads/test/prevision/shops.csv", header=True, inferSchema=True)
df_test = spark.read.csv("/home/felipelx/Downloads/test/prevision/test.csv", header=True, inferSchema=True)

"""
# check the dataframe
df_category.describe().show()
df_items.describe().show()
df_train.describe().show()
df_sample.describe().show()
df_shops.describe().show()
"""
print(df_train.columns)

plt.scatter(df_train['item_price'], df_train['item_cnt_day'])
plt.show()

spark.stop()