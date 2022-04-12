from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Datacamp").getOrCreate()

table = spark.read.csv("train_raw.txt", header=True, inferSchema=True)

query = """
SELECT train_id, station, time,
LEAD(time, 1) OVER (ORDER BY time) AS next_time
FROM train_raw
WHERE train_id = 324
"""
query_out = """
SELECT train_id, station, time,
LEAD(time, 1) OVER (PARTITION train_id ORDER BY time) AS next_time
FROM train_raw
"""
spark.sql(query).show()

# Add col running_total that sums diff_min col in each group
query = """
SELECT train_id, station, time, diff_min,
SUM(diff_min) OVER (PARTITION BY train_id ORDER BY time) AS running_total
FROM schedule
"""

# Run the query and display the result
spark.sql(query).show()