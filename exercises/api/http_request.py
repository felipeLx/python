import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
print('status', r.status_code)
r.status_code

print(r.request.headers)
print("request body:", r.request.body)

# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

r=requests.get(url)
""" 
An image is a response object that contains the image as a <a href="https://docs.python.org/3/glossary.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01#term-bytes-like-object">bytes-like object</a>. As a result, we must save it using a file object. First, we specify the file path and name 
"""
path=os.path.join(os.getcwd(),'image.png')
path
print('print Path', path)

with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)

""" wget = python code """ 
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(), 'example1.txt')
r=requests.get(url)
with open(path, 'wb') as f:
    f.write(r.content)

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print('r', r)
print(r.text)
r.headers['Content-Type']
r.json()

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)