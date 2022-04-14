from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split, length, monotonically_increasing_id, explode, when

spark = SparkSession.builder.appName("Datacamp").getOrCreate()

df = spark.read.text('/home/felipelx/Downloads/sherlock.txt')
print(df.first()) # print the first row
print(df.count()) # count the number of rows

# loading parquet
# df1 = spark.read.load('/home/felipelx/Downloads/sherlock.parquet') # parquet is a hadoop file format to store data structures
df.show(15, truncate=False)

# lower operation converts a column to lower case
df1 = df.select(lower(col('value')))

# regex_replace
df1 = df1.select(regexp_replace('value', 'mr\.', 'mr').alias('v'))
df1 = df1.select(regexp_replace('value', 'don\'t', 'do not').alias('v'))
df2 = df1.select(regexp_replace('value', 'isn\'t', 'is not').alias('v'))

df1 = df1.select(split('v', '[ ]').alias('words'))
punctuation = "_|.\?\!\",\'\[\]\*()"
df3 = df2.select(split('v', '[%s]' % punctuation).alias('words'))
# df3.show(truncate=False)

nonblank_df = df3.where(length('word') > 0)

# monotonically_increasing_id create a column of integers that are always increasing
df3 = nonblank_df.select('word', monotonically_increasing_id().alias('id'))

# explode() takes an array of things, and puts each thing on its own row, preserving the order
df4 = df3.select(explode('words').alias('word'))

# window function to use the partition clause
df4 = df4.withColumn('title', when(df4.id < 25000, 'Preface')
                                .when(df4.id < 50000, 'Chapter1')
                                .when(df4.id < 75000, 'Chapter 2')
                                .otherwise('Chapter 3'))

# repartition on a column
df5 = df4.repartition(4, 'part')
print(df5.rdd.getNumPartitions()) # return number of partition