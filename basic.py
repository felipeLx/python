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