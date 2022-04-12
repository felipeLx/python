from pyspark.sql import SparkSession

# start spark
spark = SparkSession.builder.appName("Datacamp").getOrCreate()

# Load trainsched.txt
df = spark.read.csv("trainsched.txt", header=True)

# Create temporary table called table1
df.createOrReplaceTempView('table1')