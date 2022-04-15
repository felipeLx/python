from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("data_clean").getOrCreate()

voter = spark.read.csv('voter.csv')

# transformation
voter = voter.withColumn('fullyear', voter.year + 2000)
voter = voter.drop(voter.year)

# lazy processing
# Spark takes advantage of data immutability to efficiently share / create new data representations throughout the cluster.
"""
exercise:
# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(Header=True).load('AA_DFW_2018.csv.gz')

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn('airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()
"""

# parquet
df = spark.read.format('parquet').load('filename.parquet')
df = spark.read.parquet('filename.parquet')

# writing parquet file
df.write.format('parquet').save('filename.parquet')
df.write.parquet('filename.parquet')

# parquet is good to write sql query
flight_df = spark.read.parquet('flights.parquet')
flight_df.createOrReplaceTempView('flights')
short_flight_df = spark.sql('SELECT * FROM flights WHERE Distance < 500')

"""
exercise:
# View the row count of df1 and df2
print("df1 Count: %d" % df1.count())
print("df2 Count: %d" % df2.count())

# Combine the DataFrames into one
df3 = df1.union(df2)

# Save the df3 DataFrame in Parquet format
df3.write.parquet('AA_DFW_ALL.parquet', mode='overwrite')

# Read the Parquet file into a new DataFrame and run a count
print(spark.read.parquet('AA_DFW_ALL.parquet').count())

# Read the Parquet file into flights_df
flights_df = spark.read.parquet('AA_DFW_ALL.parquet')

# Register the temp table
flights_df.createOrReplaceTempView('flights')

# Run a SQL query of the average flight duration
avg_duration = spark.sql('SELECT avg(flight_duration) from flights').collect()[0]
print('The average flight time is: %d' % avg_duration)
"""