"""
merge_asof()
. has an argument that can be set to 'forward' to select the first row in the right table whose key column is
    greater than or equal to the left's
. it can be used to do fuzzy matching of dates between tables
. after matching two tables, if there are missing values at the top of the table from the right table,  this      function can fill then it
"""

"""
merge_asof() and merge_ordered()
. this function can set the suffix for overlaping column names
. this function can be used when working with ordered or time-series data

"""

"""
merge_ordered()
. it allows for a right join during the merge
. if it cannot match the rows of the table exactly, it can use forward fill to interpolate the missing data
"""