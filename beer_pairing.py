import requests
from random import randrange
from pprint import pprint
from dataclasses import dataclass

@dataclass
class Beer():
    name: str
    abv: float
    description: str
    food_pairing: str


def main():
    data = get_beer()
    display_beer(data)
    
def get_beer():
    try:
        randomint = randrange(325)
    
        url = f'https://api.punkapi.com/v2/beers/{randomint}'

        response = requests.get(url)
        data = response.json()
        pprint(data)
        beer = get_beer_info_from_api_response(data)
        #pprint(beer)
        return beer
        
    except Exception as e:
        print('Could not connect please try again', e)

def get_beer_info_from_api_response(data):
    food_pairing = []
    try:
        beer_name = data[0]['name']
        beer_abv = data[0]['abv']
        beer_description = data[0]['description']
        
        food_pairing = data[0]['food_pairing']

        return Beer(beer_name, beer_abv, beer_description, food_pairing)

    except ValueError as e:
        print('Error values are not correct', e)


def display_beer(beer):

    print(f'Name of beer: {beer.name}')
    print(f'ABV: {beer.abv}%')
    print(f'Beer description: {beer.description}')
    print(f'Pairs best with: {beer.food_pairing}')

if __name__ == '__main__':
    main()