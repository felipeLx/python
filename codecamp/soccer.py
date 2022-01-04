# curl -X GET https://api.api-futebol.com.br/v1/campeonatos/2/artilharia \
#   -H "Authorization: Bearer test_a8c37778328495ac24c5d0d3c3923b" 

import pandas as pd
import requests
url = "https://therundown-therundown-v1.p.rapidapi.com/affiliates"


my_headers = {'x-rapidapi-host': "therundown-therundown-v1.p.rapidapi.com",
    'x-rapidapi-key': "c93e9d3b88mshf2db2c94ff97d16p1c8d87jsn2dc57ea7230d"}

response = requests.request("GET", url, headers=my_headers)
print(response.text)