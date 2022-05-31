import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage,"html.parser")
    return soupdata


save=""
for num in range(0, 7):
    soup=make_soup("http://www.ceetrus.com/fr/implantations-sites-commerciaux?page="+str(num))
    for rec in soup.find_all('tr'):
        saverec=""
        for data in rec.find_all('td'):
            data = data.text.strip()
            if "," in data:
                data = data.replace(",", "")
            saverec=saverec+","+data
        if len(saverec)!=0:
         save=save+"\n"+saverec[1:]
    print('#%d done' % num)

headers="Nom_commercial_du_Site,Ville,Etat,Surface_GLA,Nombre_de_boutique,Contact"
with open(os.path.expanduser("sites_commerciaux.csv"), "w") as csv_file:
    csv_file.write(headers)
    csv_file.write(save)