""" Using the <code>with</code> statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.
 """

import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
file = urllib.request.urlretrieve(url, filename)

filereader = open(filename, 'r')

with open(filename, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
# Read first four characters
    print(file1.read(4))

# Read one line
with open(filename, "r") as file1:
    print("first line: " + file1.readline())

# Iterate through the lines
with open(filename,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list
with open(filename, "r") as file1:
    FileasList = file1.readlines()