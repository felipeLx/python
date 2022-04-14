# spark UI is a web interface to inspect Spark execution
# logging - how to avoid a stealth loss of cpu when logging spark action
import logging
import sys

# log statement to inspect dataframes
logging.basicConfig(stream = sys.stdout, level = logging.INFO, format= '%(levelname)s - %(message)s')
logging.info('Hello %s', 'world')
logging.debug('Hello, take %d', 2)

# debug level
logging.basicConfig(stream = sys.stdout, level = logging.DEBUG, format= '%(levelname)s - %(message)s')
logging.debug('Hello, take %d', 2)

# debug lazy evaluation
# use simple timer to prove the stealth loss of CPU
# import timer
t = timer()
t.elapsed()
"""
t = timer()
t.reset()
t.elapsed()
"""
# naive approach
import time
class timer:
    start_time = time.time()
    step = 0

    def elapsed(self, reset=True):
        self.step += 1
        print('%d. elapsed: %.1f sec %s'
                % (self.step, time.time() - self.start_time))
        if reset:
            self.reset()
    
    def reset(self):
        self.start_time = time.time()
# stealth CPU wastage
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# create dataframe here
t = timer()
logging.info('No action here')
t.elapsed()
logging.debug('df has %d rows', df.count())
t.elapsed()

"""
exercise:
# Log columns of text_df as debug message
logging.debug("text_df columns: %s", text_df.columns)

# Log whether table1 is cached as info message
logging.info("table1 is cached: %s", spark.catalog.isCached(tableName="table1"))

# Log first row of text_df as warning message
logging.warning("The first row of text_df:\n %s", text_df.first())

# Log selected columns of text_df as error message
logging.error("Selected columns: %s", text_df.select("id", "word"))

# Uncomment the 5 statements that do NOT trigger text_df
logging.debug("text_df columns: %s", text_df.columns)
logging.info("table1 is cached: %s", spark.catalog.isCached(tableName="table1"))
# logging.warning("The first row of text_df: %s", text_df.first())
logging.error("Selected columns: %s", text_df.select("id", "word"))
logging.info("Tables: %s", spark.sql("show tables").collect())
logging.debug("First row: %s", spark.sql("SELECT * FROM table1 limit 1"))
# logging.debug("Count: %s", spark.sql("SELECT COUNT(*) AS count FROM table1").collect())
"""