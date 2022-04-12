from pyspark.sql import SparkSession

# start spark
spark = SparkSession.builder.appName("Practice").getOrCreate()

# Load trainsched.txt
df = spark.read.csv("trainsched.txt", header=True, sep=';', inferSchema=True)
df.head(3)
df.printSchema()
df.describe()

# show table
df.describe().show()
df.show()

# type
type(df)
df.dtypes

# select column
df.select('Name').show()
df.select(['Name', 'Experience']).show()

# add columns and drop columns
df.withColumn('More Experience', df['Experience'] * 2).show()
df.drop('More Experience')
df.show()

# rename column
df.withColumnRenamed('Name', 'FullName').show()

# handle missing values
df_missing = spark.read.csv("trainsched_m.txt", header=True, sep=';', inferSchema=True)
df_missing.show()

# drop columns with null values
df.na.drop().show()
df.na.drop(how='any')
df.na.drop(how='any', thresh=2)
df.na.drop(how='any', thresh=2, subset=['experience'])

# fill null values
df.na.fill('missing_values', ['experience']).show()

# imputer function to missing values
from pyspark.ml.feature import Imputer

imputer = Imputer(inputCols=['age', 'experience'], outputCols=['{}_imputed'.format(c) for c in ['age', 'experience']]).setStrategy('mean')

imputer.fit(df).transform(df).show()

# filter operation
df_f = spark.read.csv('trainsched_f.txt', header=True, sep=';', inferSchema=True)
df_f.filter('salary >= 2000')
df_f.filter('salary >= 2000').select('name', 'experience').show()

df_f.filter(df_f['salary'] >= 2000)
df_f.filter((df_f['salary'] >= 2000) & (df_f['age'] >= 30))
df_f.filter(~(df_f['salary'] >= 2000))

# aggregate operation
df_g = spark.read.csv('trainsched_g.txt', header=True, sep=';', inferSchema=True)
df_g.groupBy('department').agg({"salary": "mean"}).show()
df_g.groupBy('department').sum()