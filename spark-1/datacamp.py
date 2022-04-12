from pyspark.sql import SparkSession

# start spark
spark = SparkSession.builder.appName("Datacamp").getOrCreate()

# Load trainsched.txt
df = spark.read.csv("trainsched.txt", header=True, sep=';', inferSchema=True)
df.show()

# Create temporary table called table1
df_temp = df.createOrReplaceTempView('table1')

# Inspect the columns in the table df
spark.sql("DESCRIBE df").show()