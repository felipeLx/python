'''''
df.sort_values("name of the column")
-> change the order of the columns

df.sort_values("name of the column", ascending=False)
-> descending order

df.sort_values(["name of the column", "name of other column"])
-> will order for the first on the list, and second for the "other"

df.sort_values(["name of the column", "name of other column"], ascending=[False, True])

df["name"]
-> when want to zoom in just one column

df[["name", "other name"]]
-> to select multiple columns, you need 2 pairs of square brackets
-> the outher square brackets are responsible for subsetting the DataFrame,
    and the inner square brackets are creating a list of column name to subset

cols_to_subset = ["breed", "heigh"]
df[cols_to_subset]

dogs["height_cm"] > 50
-> the most comumn way to subset rows, creating a logical condition to filter against

subsetting based on text area or date
dogs[dogs["breed"] == "Labrador"]
dogs[dogs["date_of_birth"] > "2015-01-01"]

subsetting based on multiple condition
dogs[(dogs["color"] == "Brown") | (dogs["color"] == "Black")] 
is_lab = dogs["breed"] = "Labrador"
is_brown = dogs["color"] = "Brown"
dogs[is_lab & is_brow]

subsetting using .isin() * categorical variable
is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

'''''
