# cachingis keeping data in memory so that it does not have to be refreshed or recalculated each time it is used
# police: LRU - Least Recently Used

# cache dataframe: df.cache()
# uncache: df.unpersist()
# is cache? df.is_cached
"""
store level: specifies 5 details about how it is cached: df.storageLevel
output: True, True, False, True, 1

1. useDisk
2. useMemory
3. useOffHeap
4. deserialized
5. replication
"""

# persist() -> allows you to specify the desired storage level using the first argument
# when memory is scarce -> df.persist(storageLevel=pyspark.StorageLevel.MEMORY_AND_DISK)
# df.cache() == df.persist()

"""
Caching a table
df.createOrReplaceTempView('df')
spark.catalog.isCached(tableName='df')
output: False

spark.catalog.cacheTable('df')
spark.catalog.isCached(tableName='df')
output: True

# uncache
spark.catalog.uncacheTable('df1')

"""