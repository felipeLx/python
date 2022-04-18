# data pipeline: a set of steps to process data from a source to a destination
    # can consist of multiple steps
    # can span many systems
""""
- input: csv/json/web services/databases
- transformations
    withColumn(), filter(), drop(), dropDuplicates(), dropna(), fillna(),
- output: csv, parquet, database
- validation
- analysis
"""
from time import monotonic
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

schema = StructType([
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), False)
])

spark = SparkSession.builder.appName("data_clean").getOrCreate()

df = spark.read.format('csv').load(name='raw.csv', schema=schema)
# spark.read.format('csv').load('raw').schema(schema)
df = df.withColumn('id', monotonically_increasing_id())
# transform data

# after transformation, save data
df.write.parquet('outdata.parquet')
df.write.json('outdata.json')

"""
exercise:
# Import the data to a DataFrame
departures_df = spark.read.csv('2015-departures.csv.gz', header=True)

# Remove any duration of 0
departures_df = departures_df.filter(departures_df[3] > 0)

# Add an ID column
departures_df = departures_df.withColumn('id', F.monotonically_increasing_id())

# Write the file out to JSON format
departures_df.write.json('output.json', mode='overwrite')

"""