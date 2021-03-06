# print('Hello World')

# Check the Python Version

import sys

print(sys._version_info)
# frint(sys._version_info)

print('Hello World')

type(12.0)

# you can wrap the type
type(2)
type(float(2))

# Convert a string into an integer with error
int('1 or 2 people')

# Type of True
type(True)

# Convert True to int
int(True) # False = 0; True = 1

type(6/7)
type(6 // 2)
# we can use the double slash for integer division, where the result is rounded down to the nearest integer:


# Store value into variable
x = 43 + 60 + 16 + 41
y = x / 60
print(y)

math_opt = 3 + 2 * 2
print(math_opt)

name = "Michael Jackson"
print(name[::2]) # Get every second element. The elments on index 1, 3, 5 ...
name[0:5:2] # Get every second element in the range from index 0 to index 4

# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name_m = "Michael Jackson"
print(name_m.find('el'))

# Slice to print the 3 first elements
d = "ABCDEFG"
print(d[0:3])

# print out backslash
print("\\")

# to uppercase
f = "You are wrong"
f.upper()

# Consider the variable g, and find the first index of the sub-string snow
g_text = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went. Everywhere that Mary went The lamb was sure to go"
print(g_text.find("snow"))
print(g_text.replace("Mary", "Maria"))

#PYTHON TYPES

#Tuples - can be access by index is imutable
type_tuples = (1, 2, 3, 4, "Text")

#list - can be access by index and is mutable
type_list = [1, 2, 3, 4, "Text"]

# Create a list <code>a_list</code>, with the following elements <code>1</code>, <code>hello</code>, <code>\[1,2,3]</code> and <code>True</code>.
a_list = [1, "hello", [1,2,3], True]

# Retrieve the elements stored at index 1, 2 and 3 of <code>a_list</code>.
a_list[1:4]
a_list

#concatenate
A = [1,2,3]
B = [4,5,6]
C = A + B
print(C)

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple
print(len(genres_tuple))
genres_tuple.index("disco")

# sort
C_tuple=(-5, 1, -3)
sorted(C_tuple)

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

# Access to the value by the key
Dict["key1"]
# Access to the value by the key
Dict[(0, 1)]

# We can verify if an element is in the dictionary:
# Verify the key is in the dictionary
'The Bodyguard' in Dict

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

album_sales_dict = {
    "Back in Black": 50,
    "The Bodyguard": 50,
    "Thriller": 65,
}

album_sales_dict["Thriller"]   

# set

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_union = album_set1.union(album_set2)
print(album_union)

album_set1.issubset(album_union)

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

rating = 8.5
if rating > 8:
    print('this album is amazing')

rating = 7
if rating > 8:
    print('This album is amazing')
elif rating <= 8:
    print('This album is ok')

album_year = 1979
if album_year < 1980 or album_year == 1993 or album_year == 1991:
    print('Album Year: ', album_year)

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]

while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i=i+1
    rating = PlayListRatings[i]

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    squares.remove(squares[i])
    i = i + 1
    print('new square', new_squares)
    print('old square', squares)

myFavouriteBand = 'AC/DC'
def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")