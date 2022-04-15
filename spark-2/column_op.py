# df:
    # made up of rows and columns
    # immutable
    # various transformation to operations to modify data

# returns rows filter/where name starts with M
"""
voter_df.filter(voter_name.name.like('M%')).show()
remove nulls
remove odds entries
split data from combined sources
negate with ~
voter_df.filter(voter_df['name'].isNotNull())
voter_df.filter(voter_df.year > 1800)
voter_df.where(voter_df['_c0'].contains('VOTE'))
voter_df.where(~ voter_df._c1.isNull())

from array import ArrayType
import pyspark.sql.functions as F
voter = withColumn('upper', F.upper('name'))
voter.withColumn('splits', F.split('name', ' '))
voter.withColumn('year', voter['_c4'].cast(IntegerType()))

# ArrayType column functions
.size(<column>) returns the length of ArrayType() column
.getItem(<index>) ised to retrievea specific item at index of list column

exercise:
# Show the distinct VOTER_NAME entries
voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)

# Filter voter_df where the VOTER_NAME is 1-20 characters in length
voter_df = voter_df.filter('length(VOTER_NAME) > 0 and length(VOTER_NAME) < 20')

# Filter out voter_df where the VOTER_NAME contains an underscore
voter_df = voter_df.filter(~ F.col('VOTER_NAME').contains('_'))

# Show the distinct VOTER_NAME entries again
voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)

exercise:
# Add a new column called splits separated on whitespace
voter_df = voter_df.withColumn('splits', F.split(voter_df.VOTER_NAME, '\s+'))

# Create a new column called first_name based on the first item in splits
voter_df = voter_df.withColumn('first_name', voter_df.splits.getItem(0))

# Get the last entry of the splits list and create a column called last_name
voter_df = voter_df.withColumn('last_name', voter_df.splits.getItem(F.size('splits') - 1))

# Drop the splits column
voter_df = voter_df.drop('splits')

# Show the voter_df DataFrame
voter_df.show()
"""