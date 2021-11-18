
import pandas as pd
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page



#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

len(tables)

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

pd.read_html(str(tables[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html

dataframe_list = pd.read_html(url, flavor='bs4')
len(dataframe_list)
dataframe_list[5]

pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
