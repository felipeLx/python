# import libraries to strach table from websites
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import contextlib
from urllib3.exceptions import InsecureRequestWarning

old_merge_environment = requests.Session.merge_environment_settings

@contextlib.contextmanager
def no_ssl_verification():
    opened_adaptors = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        opened_adaptors.add(self.get_adapter(url))

        settings = old_merge_environment(self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings
    
    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment

        for adapter in opened_adaptors:
            try:
                adapter.close()
            except:
                pass                


# url disaster table
url = 'https://s2id.mi.gov.br/paginas/series/'

with no_ssl_verification():
    page = requests.get(url)
    print('its ok')

    page = requests.get(url, verify=True)
    print('its ok with True')

page = requests.get(url, verify=False)
print('its ok with False')

session = requests.Session()
session.verify = True

with no_ssl_verification():
    page = requests.get(url, verify = True)
    print('works with True')

try:
    page = requests.get(url)
except requests.exceptions.SSLError:
    print('SSL error')

try:
    session.get(url)
except requests.exceptions.SSLError:
    print('SSL error')

# transform to python format
soup = BeautifulSoup(page.text, 'lxml')
table_site = soup.find('div', {id: 'resultados'})

headers = []
for i in table_site.find_all('th'):
    title = i.text
    headers.append(title)
    print(i.text)