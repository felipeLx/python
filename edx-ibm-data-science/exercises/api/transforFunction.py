import pandas as pd
import numpy as np
import json

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df

#applying the transform function
df = df.transform(func = lambda x : x + 10)
df

result = df.transform(func = ['sqrt'])
result

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

""" 
**json.dump()** method can be used for writing to JSON file.
Syntax: json.dump(dict, file_pointer)
Parameters:
1.  **dictionary** – name of the dictionary which should be converted to JSON object.
2.  **file pointer** – pointer of the file opened in write or append mode.
 """
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)