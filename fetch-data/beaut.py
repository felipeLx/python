html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.p['class']
soup.a
soup.find_all('a')
soup.find(id="link3")

# extract URL found on a tag
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

# tag name access by ['id'], like a dictionary
tag = BeautifulSoup('<b id="boldest">Extremely bold</b>', 'html.parser').b
tag['id']
tag.attrs # {'id': 'boldest'}

"""
from bs4 import CData
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())
for string in soup.string:
    print(repr(string))
"""

link = soup.a
for parent in link.parents:
    print(parent.name)