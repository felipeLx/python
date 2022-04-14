from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# UDF require to specify the type of result
# code missing one step: 
bad_udf = udf(lambda x: x.indeces[0] if (x and hasattr(x, 'toArray') and x.numNonzeros()) else 0, IntegerType())

try:
    df.select(bad_udf('outvec').alias('label')).first()
except Exception as e:
    print(e.__class__)
    print(e.errmsg)

from pyspark.ml.feature import CountVectorizer
cv = CountVectorizer(inputCol = 'words', outputCol = 'features')

model = cv.fit(df)
result = model.transform(df)
print(result)

"""
exercise:
# Selects the first element of a vector column
first_udf = udf(lambda x:
            float(x.indices[0]) 
            if (x and hasattr(x, "toArray") and x.numNonzeros())
            else 0.0,
            FloatType())

# Apply first_udf to the output column
df.select(first_udf("output").alias("result")).show(5)

# Add label by applying the get_first_udf to output column
df_new = df.withColumn('label', get_first_udf('output'))

# Show the first five rows 
df_new.show(5)


# Transform df using model
result = model.transform(df.withColumnRenamed('in', 'words'))\
        .withColumnRenamed('words', 'in')\
        .withColumnRenamed('vec', 'invec')
result.drop('sentence').show(3, False)

# Add a column based on the out column called outvec
result = model.transform(result.withColumnRenamed('out', 'words'))\
        .withColumnRenamed('words', 'out')\
        .withColumnRenamed('vec', 'outvec')
result.select('invec', 'outvec').show(3, False)	
"""