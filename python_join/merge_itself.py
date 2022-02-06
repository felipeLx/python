# merge itself -> referred to as a self join
# table A 4 rows 3 columns, table B 4 rows 3 columns -> table with row that merge with 6 columns
original_sequels = sequels.merge(sequels, left_on="sequel", right_on="id", suffixes=("_org", "_seq"))
print(original_sequels.head())

# we can merge the tables on differents columns
# left_on and right_on where the sequel's id matches the original movie's id

# continue format results
print(original_sequels[:,["title_org", "title_seq"]].head())

# when to merge itself (self join)
# . hierarchical relationships
# . sequential relationships
# . graph data
crews_self_merged = crews.merge(crews, on="id", suffixes=("_dir", "_crew"))
# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == "Director") & 
     (crews_self_merged['job_crew'] != "Director"))
direct_crews = crews_self_merged[boolean_filter]