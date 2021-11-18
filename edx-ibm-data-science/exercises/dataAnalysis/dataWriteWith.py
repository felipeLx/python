# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line B")

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line D\n", "This is line E\n", "This is line F\n"]

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())