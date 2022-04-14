# applying a model to evaluate data
# use transform operation
predicted = df_trained.transform(df_test)
# transform operation return a dataframe - adds columns to the dataset, a prediction column and a probability column
# prediction -> double, in this case value 0 or 1
# probability -> vector of length two, vector between 0 and 1
                # first: prob that is false
                # second: prob that is true

x = predicted.first
print('Right' if x.label == int(x.prediction) else 'Wrong')

# train call model
# some evaluation data in df called df_eval
# to calculate the performance of this classification model: Area Under Curve, AUC
model_stats = model.evaluate(df_eval) # return BinaryLogisticReressionSummary
pyspark.ml.classification.BinaryLogisticReressionSummary
print('\nPerformance: %.2f' % model_stats.areaUnderROC)

"""
exercise:
# Score the model on test data
testSummary = df_fitted.evaluate(df_testset)

# Print the AUC metric
print("\ntest AUC: %.3f" % testSummary.areaUnderROC)

# Apply the model to the test data
predictions = df_fitted.transform(df_testset).select(fields)

# Print incorrect if prediction does not match label
for x in predictions.take(8):
    print()
    if x.label != int(x.prediction):
        print("INCORRECT ==> ")
    for y in fields:
        print(y,":", x[y])
"""