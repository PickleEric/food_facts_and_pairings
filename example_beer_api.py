import requests
from random import randrange
from pprint import pprint

url = 'https://api.openbrewerydb.org/breweries/autocomplete?query=dog'

response = requests.get(url)
data = response.json()
#pprint(data)

url2 = 'https://api.openbrewerydb.org/breweries/search?query=dog'

response = requests.get(url2)
data = response.json()
#pprint(data)

url3 = 'https://api.punkapi.com/v2/beers/random'
response = requests.get(url3)
data = response.json()
#pprint(data)


randomint = randrange(325)
url4 = f'https://api.punkapi.com/v2/beers/1{randomint}'
response = requests.get(url4)
data = response.json()
pprint(data)

