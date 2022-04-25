# follow example from gitgub/pyspark
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression

spark = SparkSession.builder.appName("binominal").getOrCreate()

df = spark.read.format('libsvm').load('https://raw.githubusercontent.com/apache/spark/master/data/mllib/sample_libsvm_data.txt')

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lrModel = lr.fit(df)

# coefficient and intercept
print('Coefficients: ' + str(lrModel.coefficients))
print('Intercept: ' + str(lrModel.intercept))

spark.stop()