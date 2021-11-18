import pandas as pd

# Read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
# Print first five rows of the dataframe
df.head()

# Read data from Excel File and print the first five rows
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

dfxls = pd.read_excel(xlsx_path)
dfxls.head()

# Access to the column Length
x = df[['Length']]
x

# Get the column as a series
y = df['Length']
y

# Get the column as a dataframe
z = df[['Artist']]
type(z)

# Access to multiple columns
m = df[['Artist','Length','Genre']]
m

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name
df.loc[1, 'Artist']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']

# exercise: create frame from Rating
q1 = df[['Rating']]
q1

# exercise: create frame from Released and Artist
q2 = df[['Released', 'Artist']]
q2

#Access the 2nd row and the 3rd column of <code>df</code>:
df.iloc[1,2]

""" 
I) Use the following list to convert the dataframe index df to characters and assign it to df_new; 
II) find the element corresponding to the row index a and column  'Artist'. III) Then select the rows a through d for the column  'Artist'
 """
new_index=['a','b','c','d','e','f','g','h']
df_new = df
df_new.index = new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']