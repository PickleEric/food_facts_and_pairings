import requests
from pprint import pprint

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

def getcockaildrink():

    try:

        response = requests.get(url)
        data = response.json()
        pprint(data)

        drinkapi = data['drinks']
        for data in drinkapi:
            drink = data['strDrink']
        return drink

    except Exception as e:
        print(e)
        print('There was an error contacting the API')

