from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split, length, monotonically_increasing_id, explode, when

spark = SparkSession.builder.appName("Datacamp").getOrCreate()

df = spark.read.text('/home/felipelx/Downloads/sherlock.txt')

df.select('part', 'title').distinct().sort('part').show(truncate=False)

#query print the word of the current row as w1
query = """
SELECT id, word AS w1,
LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3
FROM df
"""

spark.sql(query).sort('id').show()

#  lag function gives its values from a preview row
lag_query = """
    SELECT
    id,
    LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
    LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
    word AS w3
    FROM df
    ORDER BY id
"""
spark.sql(lag_query).show()

lag2_query = """
    SELECT
    id,
    LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
    LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
    word AS w3
    FROM df
    WHERE part=2
"""
spark.sql(lag2_query).show()

# repartition exercise
"""
# Word for each row, previous two and subsequent two words
query = 
SELECT
part,
LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
word AS w3,
LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w4,
LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w5
FROM text

spark.sql(query).where("part = 12").show(10)
"""

# exericise
"""
# Repartition text_df into 12 partitions on 'chapter' column
repart_df = text_df.repartition(12, 'chapter')

# Prove that repart_df has 12 partitions
repart_df.rdd.getNumPartitions()
"""