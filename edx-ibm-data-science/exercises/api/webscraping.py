from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))

tag_child =tag_object.b
tag_child

parent_tag=tag_child.parent
parent_tag

sibling_1=tag_object.next_sibling
sibling_1

sibling_2=sibling_1.next_sibling
sibling_2

tag_string=tag_child.string
tag_string

unicode_string = str(tag_string)
unicode_string

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html.parser")

table_rows=table_bs.find_all('tr')
table_rows

first_row =table_rows[0]
first_row
print(type(first_row))

for i,row in enumerate(table_rows):
    print("row",i,"is",row)

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
list_input

table_bs.find_all(id="flight")
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

table_bs.find_all(href=True)

url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


