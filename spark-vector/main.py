from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
# $example off$
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("CorrelationExample") \
        .getOrCreate()

    # $example on$
    data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
            (Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
            (Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
            (Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]
    df = spark.createDataFrame(data, ["features"])

    r1 = Correlation.corr(df, "features").head()

    # $example off$
    assert r1 is not None
    # $example on$
    print("Pearson correlation matrix:\n" + str(r1[0]))

    r2 = Correlation.corr(df, "features", "spearman").head()

    # $example off$
    assert r2 is not None
    # $example on$
    print("Spearman correlation matrix:\n" + str(r2[0]))
    # $example off$

    spark.stop()