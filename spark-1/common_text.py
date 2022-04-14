"""
query3 = 
    SELECT
        id,
        word AS w1,
        LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
        LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3
    FROM df

qery3agg = 
    SELECT w1, w2, w3, COUNT(*) AS count FROM(
        SELECT
            word AS w1,
            LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
            LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3
    FROM df)
    GROUP BY w1, w2, w3
    ORDER BY count desc

query4agg =
    SELECT w1, w2, w3, length(w1)+length(w2)+length(w3) AS length FROM (
        SELECT
            word AS w1,
            LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
            LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3
        FROM df
        WHERE part <> 0 AND part <> 13
    )
    GROUP BY w1, w2, w3
    ORDER BY length DESC

Two song or video identifiers that are near each other in sorted order will generally not be similar in other qualitative respects.
"""

"""
exercise:
# Find the top 10 sequences of five words
query = 
SELECT w1, w2, w3, w4, w5, COUNT(*) AS count FROM (
   SELECT word AS w1,
   LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
   LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3,
   LEAD(word, 3) OVER(PARTITION BY part ORDER BY id) AS w4,
   LEAD(word, 4) OVER(PARTITION BY part ORDER BY id) AS w5
   FROM text
)
GROUP BY w1, w2, w3, w4, w5
ORDER BY count DESC
LIMIT 10

df = spark.sql(query)
df.show()

# Unique 5-tuples sorted in descending order
query = 
SELECT DISTINCT w1, w2, w3, w4, w5 FROM (
   SELECT word AS w1,
   LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
   LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w3,
   LEAD(word, 3) OVER(PARTITION BY part ORDER BY id) AS w4,
   LEAD(word, 4) OVER(PARTITION BY part ORDER BY id) AS w5
   FROM text
)
ORDER BY w1 DESC, w2 DESC, w3 DESC, w4 DESC, w5 DESC 
LIMIT 10

df = spark.sql(query)
df.show()

#   Most frequent 3-tuple per chapter
query = 
SELECT chapter, w1, w2, w3, count FROM
(
  SELECT
  chapter,
  ROW_NUMBER() OVER (PARTITION BY chapter ORDER BY count DESC) AS row,
  w1, w2, w3, count
  FROM ( %s )
)
WHERE row = 1
ORDER BY chapter ASC
 % subquery

spark.sql(query).show()
"""