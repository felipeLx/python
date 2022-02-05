# dictionaries
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

# to access value of a dictionary
my_dict["key1"]

# 2 ways to create a DataFrame
# from a list of dictionaries and from a dictionary of lists

# list of dictionary
# -> constructed row by row
list_dicts = [
    {"name": "Ginger", "breed": "Dachshund", "height": 22},
    {"name": "Ice", "breed": "Poodle", "height": 28}
]
new_dog = pd.DataFrame(list_dicts)

# dictionary of lists
# -> column by column, each key be a column name, each value will be a list of values in the column
dict_of_lists = {
    "name": ["Ginger", "Ice"],
    "breed": ["Dachshund", "Poodle"],
    "heigh": [22, 28]
}

new_dog = pd.DataFrame(dict_of_lists)
