"""
Possible merging issue:
. unintentional one-to-many relationship
. unintentional many-to-many relationship
. unintentionally create duplicate records if a record exists in both tables
"""

# validating merges
"""
.merge(validate=None): checks if the merge is on specified type
    . one-to-one
    . one-to-many
    . many-to-one
    - many-to-many
"""

# validating concat
"""
.concat(verify_integrity=False)
    . check whether the new concatenated index contains duplicates
    . default value is False
"""
