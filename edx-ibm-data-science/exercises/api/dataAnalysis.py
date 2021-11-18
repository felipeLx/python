# Import pandas library
import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

df.shape
df.info()
df.describe()

""" 
We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:
**.isnull()**
**.notnull()**
 """
missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")   

""" 
Check all data is in the correct format (int, float, text or other).
dtype() to check the data type
astype() to change the data type
 """

df.dtypes