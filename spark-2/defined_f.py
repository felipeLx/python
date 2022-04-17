#  udf  user defined function
# stores as variable
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pandas import DataFrame
# start session
spark = SparkSession.builder.appName("defines_function").getOrCreate()
user_df = spark.read.csv('raw.csv', header=True, sep=';')
# reverse string udf
def reverseString(str):
    return str[::-1]

udfReverse = udf(reverseString, StringType())

# use with spark
user_df = user_df.withColumn('name_reversed', udfReverse(user_df.name))
user_df.show()
"""
# sorting Cap
def sortingCap():
    return random.choice(['G', 'H', 'R', 'S'])
udfSortingCap = udf(sortingCap, StringType())
user_df = user_df.withColumn('sorting_cap', udfSortingCap())
"""
spark.stop()

"""
exercise:
def getFirstAndMiddle(names):
  # Return a space separated string of names
  return ' '.join(names[:-1])

# Define the method as a UDF
udfFirstAndMiddle = F.udf(getFirstAndMiddle, StringType())

# Create a new column using your UDF
voter_df = voter_df.withColumn('first_and_middle_name', udfFirstAndMiddle(voter_df.splits))

# Show the DataFrame
voter_df.show()
"""