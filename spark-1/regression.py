from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("reression").getOrCreate()

trainning = spark.read.csv("test.txt", header=True, inferSchema=True, sep=';')

# create vectors
from pyspark.ml.feature import VectorAssembler
featureassembler = VectorAssembler(inputCols=["experience", "age"], outputCol="independent_features")

output = featureassembler.transform(trainning)
output.columns

finalized_data = output.select('Independent_features', 'salary')
finalized_data.show()

# test split
from pyspark.ml.regression import LinearRegression
train_data, test_data = finalized_data.randomSplit([0.7, 0.3])
regressor = LinearRegression(featuresCol='Independent_features', labelCol='salary')
regressor = regressor.fit(train_data)

# coeficients
regressor.coefficients

# intercept
regressor.intercept

# prediction
pred_results = regressor.evaluate(test_data)
pred_results.predictions.show()

# error of the prediction
pred_results.rootMeanSquaredError
pred_results.meanAbsoluteError

