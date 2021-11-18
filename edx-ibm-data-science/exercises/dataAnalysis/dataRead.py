import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
file = urllib.request.urlretrieve(url, filename)

filereader = open(filename, 'r')
print(filereader.name)
FileContent = filereader.read()
print(FileContent)
print(type(FileContent))
filereader.close()