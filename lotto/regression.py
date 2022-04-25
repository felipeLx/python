from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("Lotto").getOrCreate()

trainning = spark.read.csv('sort.csv', sep=';', header=True, inferSchema=True)

# create vector
feature_assembler = VectorAssembler(inputCols=['bola 1','bola 2', 'bola 3'], outputCol='independ_features')

output = feature_assembler.transform(trainning)
print(output.columns)

finalized_data = output.select('independ_features', 'bola 4')
finalized_data.show()

# test split
from pyspark.ml.regression import LinearRegression
train_data, test_data = finalized_data.randomSplit([0.7, 0.3])
regressor = LinearRegression(featuresCol='independ_features', labelCol='bola 4')
regressor = regressor.fit(train_data)

# coeficient and intercept
print('coefficients: ', regressor.coefficients)
print('intercept: ', regressor.intercept)

# prediction
pred_results = regressor.evaluate(test_data)
pred_results.predictions.show()

# error of prediction
pred_results.rootMeanSquaredError
pred_results.meanAbsoluteError

# applying a model to evaluate data
predicted = regressor.transform(test_data)
x = predicted.first
print('Right' if x.label == int(x.prediction) else 'Wrong')

# train call model
from pyspark.ml.classification import BinaryLogisticRegressionSummary
auc_metric = pred_results.areaUnderROC
print('AUC: ', auc_metric)