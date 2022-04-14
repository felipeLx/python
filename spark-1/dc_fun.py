from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, sum
from pyspark.sql import Window

spark = SparkSession.builder.appName("Datacamp").getOrCreate()

df = spark.read.csv("train_raw.txt", header=True, inferSchema=True)
# df.show()

# use col to be more redeable
df_col = df.select(col('train_id'), col('station'))

# can combine two functions
df.select('train_id', 'station').withColumnRenamed('train_id', 'train')

# dot notation
# df_dot = spark.sql('SELECT train_id, station FROM df LIMIT 5')

# OR
df_dot = df.select(col('train_id').alias('train'), 'station').limit(5)
df_dot.show()

# window dot notation
df_window = df.withColumn('id', row_number()
    .over(Window.partitionBy('train_id')
.orderBy('time')))
df_window.show()

