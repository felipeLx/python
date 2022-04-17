"""
File size optimization
Consider if you're given 2 large data files on a cluster with 10 nodes. Each file contains 10M rows of roughly the same size. While working with your data, the responsiveness is acceptable but the initial read from the files takes a considerable period of time. Note that you are the only one who will use the data and it changes for each run.

Which of the following is the best option to improve performance?
Split the 2 files into 50 files of 400K rows each.
"""
# Import the full and split files into DataFrames
full_df = spark.read.csv('departures_full.txt.gz')
split_df = spark.read.csv('departures_0*.txt.gz') # how to read multiple files

# Print the count and run time for each DataFrame
start_time_a = time.time()
print("Total rows in full DataFrame:\t%d" % full_df.count())
print("Time to run: %f" % (time.time() - start_time_a))

start_time_b = time.time()
print("Total rows in split DataFrame:\t%d" % split_df.count())
print("Time to run: %f" % (time.time() - start_time_b))

"""
The results should illustrate that using split files runs more quickly than using one large file for import. Note that in certain circumstances the results may be reversed. This is a side effect of running as a single node cluster. Depending on the tasks required and resources available, it may occasionally take longer than expected. If you perform multiple runs of the tasks, you should see the full file import as generally slower than the split file import.
"""