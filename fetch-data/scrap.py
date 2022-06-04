from bs4 import BeautifulSoup

with open('antt.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    links_a = soup.find_all('a', class_='heading')
    for link in links_a:
        a_name = link.text
        print(a_name)
"""
    links_html = soup.find_all('a', class_='resource-url-analytics')
    for link in links_html:
        print(link.text)
"""