# explain - provides detailed plan information about the query without actually running it
# EXPLAIN SELECT * FROM table

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("reression").getOrCreate() 

df = spark.read.csv("trainsched.txt", header=True, sep=';', inferSchema=True)

df.registerTempTable('df')
spark.sql('EXPLAIN SELECT * FROM df').first()