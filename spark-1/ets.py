# extract, transform and select
# UDF, user defined function
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, length, udf
from pyspark.sql.types import BooleanType, StringType, IntegerType, FloatType, ArrayType

spark = SparkSession.builder.appName("reression").getOrCreate() 
df = spark.read.csv("trainsched.txt", header=True, sep=';', inferSchema=True)

# the first argument to the UDF is a function
short_udf = udf(lambda x: 
                    True if not x or len(x) < 10 else False,
                    BooleanType())
df.select(short_udf('text_data')\
    .alias('is short'))\
    .show()

# creating array UDF
in_udf = udf(lambda x: x[0:len(x)-1] if x and len(x) > 1
    else [],
    ArrayType(StringType()))
df.select('word array', in_udf('word_array').alias('without endword'))\
    .show(5, truncate=30)

# sparse vector format - two parallel arrays
"""
Array: [1.0, 0.0, 0.0, 3.0]
Sparse vector: (4, [0, 3], [1.0, 3.0])
"""

# has_attribute() way to determine that an object is a sparse vector
# hasattr(x, 'toArray')
# numNonZeros() is a fast way of determining that a vector is empty
# x.numNonZeros()
