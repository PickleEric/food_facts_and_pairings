import requests
from random import randrange
from pprint import pprint

class Beer():
    # todo use a dataclass if prefered 
    def __init__(self, name, abv, description, food_pairing):
        self.name = name
        self.abv = abv
        self.description = description
        self.food_pairing = food_pairing


def main():
    data = get_beer()
    display_beer(data)
    
def get_beer():
    try:
        randomint = randrange(325)
    
        url = f'https://api.punkapi.com/v2/beers/{randomint}'

        response = requests.get(url)
        data = response.json()

        # todo what does this response look like? 
        # you may need to do more processing and return some info? 

        beer = get_beer_info_from_api_response(data)
        return beer 

    except Exception as e:
        print('Could not connect please try again', e)


# this is a GREAT candidate for a unittest - no mocking!
def get_beer_info_from_api_response(data):

    beer_abv = data[0]['abv']
    beer_description = data[0]['description']
    beer_name = data[0]['name']
    food_pairing = ', '.join(data[0]['food_pairing'])  # suggest this might be better as a list? 

    return Beer(beer_name, beer_abv, beer_description, food_pairing)

    # todo error handling if response is in unexpected format


def display_beer(beer):
    print(f'Name of beer: {beer.name}')
    print(f'ABV: {beer.abv}%')
    print(f'Beer description: {beer.description}')
    print(f'This beer pairs best with: {beer.food_pairing}')


if __name__ == '__main__':
    main()