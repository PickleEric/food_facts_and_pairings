import requests
from random import randrange
from pprint import pprint

def main():
    data = get_beer()
    display_beer(data)
    
def get_beer():
    try:
        randomint = randrange(325)
    
        url = f'https://api.punkapi.com/v2/beers/{randomint}'

        response = requests.get(url)
        data = response.json()
        return data

        #pprint(data)

    except Exception as e:
        print('Could not connect please try again', e)

def display_beer(data):

    beer_abv = data[0]['abv']
    beer_description = data[0]['description']
    beer_name = data[0]['name']
    food_pairing = ', '.join(data[0]['food_pairing'])

    print(f'Name of beer: {beer_name}')
    print(f'ABV: {beer_abv}%')
    print(f'Beer description: {beer_description}')
    print(f'This beer pairs best with: {food_pairing}')

if __name__ == '__main__':
    main()