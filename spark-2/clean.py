# prepare raw data to be used n data processing pipeline
"""
Reformatting or replacing text
Performing calculation
Removing garbage or incomplete data
"""
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("data_clean").getOrCreate()

peopleSchema = StructType([
    # define name
    StructField("name", StringType(), True),
    # add age field
    StructField("age", IntegerType(), True),
    # add city field
    StructField("city", StringType(), True)
])

people_df = spark.read.format('csv').load(name='raw.csv', schema=peopleSchema)

spark.stop()