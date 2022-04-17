# shuffling: refers to moving data around to various workers to complete a task
    # hide complexity from the user
    # limit use of .repartition(num_partitions)
    # use .coalesce(num_partitions) to reduce the number of partitions
    # use care when calling .join()
    # use broadcast() is a method to provide a copy of an object to each worker

from pyspark.sql.functions import broadcast
combined_df = df_1.join(broadcast(df_2))

# Join the flights_df and aiports_df DataFrames
normal_df = flights_df.join(airports_df, \
    flights_df["Destination Airport"] == airports_df["IATA"] )

# Show the query plan
normal_df.explain()

# Import the broadcast method from pyspark.sql.functions
from pyspark.sql.functions import broadcast

# Join the flights_df and airports_df DataFrames using broadcasting
broadcast_df = flights_df.join(broadcast(airports_df), \
    flights_df["Destination Airport"] == airports_df["IATA"] )

# Show the query plan and compare against the original
broadcast_df.explain()


start_time = time.time()
# Count the number of rows in the broadcast DataFrame
broadcast_count = broadcast_df.count()
broadcast_duration = time.time() - start_time

# Print the counts and the duration of the tests
print("Normal count:\t\t%d\tduration: %f" % (normal_count, normal_duration))
print("Broadcast count:\t%d\tduration: %f" % (broadcast_count, broadcast_duration))

"""
While the difference in time is miniscule for our example, the ratio between the durations is significant. Depending on the makeup of the data being joined, you can notably cut the run time for Spark operations.
"""