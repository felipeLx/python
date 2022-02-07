# value not must be save like string
import pandas as pd

apple = pd.DataFrame({
    'date': ["2/13/18", "2/14/18", "2/15/18"],
    'time': ["16:00","16:00","16:00"],
    'price': ["164.34","167.34","177.34"]
})

print(apple.price.dtype)

apple["price"] = apple.price.astype("float")

# dot notation: apple.price
# bracket notation: apple["price"] -> to create a new serie or change an existing series
print(ri.is_arrested.head(5))

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' 
print(ri['is_arrested'].dtype)