# logist classifier wants a binary column indicating whether the row is a positive or negative example
df_true = df.where("endword in ('she', 'he', 'hers', 'his', 'her', 'him')")\
    .withColumn('label', lit(1)) # add 1 to row where the column finish with a pronoum
df_false = df.where("endword not in ('she', 'he', 'hers', 'his', 'her', 'him')")\
    .withColumn('label', lit(0)) # add 1 to row where the column not finish with a pronoum

# combining the positive and negative
df_ex = df_true.union(df_false)

# trainning the data
df_train, df_eval = df_ex.randomSplit((0.6, 0.4), 42)
# randomSplit: the first argument is a 2-tupple giving the portion desired in the first and second result, respectively
            # the second to turn off randomness if we need to replicate the result
            # 0.6 data into df_train
            # 0.4 into the df_eval
from pyspark.ml.classification import LogisticRegression
logistic = LogisticRegression(maxInter = 50, reqParam = 60, elasticNetParam= 0.3)
model = logistic.fit(df_train)

print('Training interaction: ', model.summary.totalIterations)

"""
exercise:
# Import the lit function
from pyspark.sql.functions import lit

# Select the rows where endword is 'him' and label 1
df_pos = df.where("endword = 'him'")\
           .withColumn('label', lit(1))

# Select the rows where endword is not 'him' and label 0
df_neg = df.where("endword <> 'him'")\
           .withColumn('label', lit(0))

# Union pos and neg in equal number
df_examples = df_pos.union(df_neg.limit(df_pos.count()))
print("Number of examples: ", df_examples.count())
df_examples.where("endword <> 'him'").sample(False, .1, 42).show(5)

# Split the examples into train and test, use 80/20 split
df_trainset, df_testset = df_examples.randomSplit((0.8, 0.2), 42)

# Print the number of training examples
print("Number training: ", df_trainset.count())

# Print the number of test examples
print("Number test: ", df_testset.count())

# Import the logistic regression classifier
from pyspark.ml.classification import LogisticRegression

# Instantiate logistic setting elasticnet to 0.0
logistic = LogisticRegression(maxIter=100, regParam=0.4, elasticNetParam=0.0)

# Train the logistic classifer on the trainset
df_fitted = logistic.fit(df_trainset)

# Print the number of training iterations
print("Training iterations: ", df_fitted.summary.totalIterations)
"""