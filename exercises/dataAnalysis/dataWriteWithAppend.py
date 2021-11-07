# We can write to files without losing any of the existing data as follows by setting the mode argument to append: **a**.  you can append a new line as follows:

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

#  **r+** : Reading and writing. Cannot truncate the file.
#  **w+** : Writing and reading. Truncates the file.
#  **a+** : Appending and Reading. Creates a new file, if none exists.
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. # From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


# it can be useful to add a truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
    