# explain - provides detailed plan information about the query without actually running it
# EXPLAIN SELECT * FROM table

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("reression").getOrCreate() 

df = spark.read.csv("trainsched.txt", header=True, sep=';', inferSchema=True)

df.registerTempTable('df')
spark.sql('EXPLAIN SELECT * FROM df').first()
# df.explain()

"""
exercise:
# Run explain on text_df
text_df.explain()

# Run explain on "SELECT COUNT(*) AS count FROM table1" 
spark.sql("SELECT COUNT(*) AS count FROM table1").explain()

# Run explain on "SELECT COUNT(DISTINCT word) AS words FROM table1"
spark.sql("SELECT COUNT(DISTINCT word) AS words FROM table1").explain()
"""