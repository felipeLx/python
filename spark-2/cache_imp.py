# cache implementation
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark = SparkSession.builder.appName("defines_function").getOrCreate()
df = spark.read.csv('/home/felipelx/Downloads/voters.csv', header=True, sep=';')

# cache on a DF object prior to a given Action
df.cache().count()
# OR
df = df.withColumn('spark_id', monotonically_increasing_id())
df = df.cache()
df.show()

"""
exercise:
start_time = time.time()

# Add caching to the unique rows in departures_df
departures_df = departures_df.distinct().cache()

# Count the unique rows in departures_df, noting how long the operation takes
print("Counting %d rows took %f seconds" % (departures_df.count(), time.time() - start_time))

# Count the rows again, noting the variance in time of a cached DataFrame
start_time = time.time()
print("Counting %d rows again took %f seconds" % (departures_df.count(), time.time() - start_time))
"""
spark.stop()

"""
exercise:
# Determine if departures_df is in the cache
print("Is departures_df cached?: %s" % departures_df.is_cached)
print("Removing departures_df from cache")

# Remove departures_df from the cache
departures_df.unpersist()

# Check the cache status again
print("Is departures_df cached?: %s" % departures_df.is_cached)
"""