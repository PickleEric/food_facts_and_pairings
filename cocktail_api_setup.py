import requests
from pprint import pprint

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

def getcockaildrink():

    try:
        food = input('What food would like like a cocktail to pair with? ')

        response = requests.get(url)
        data = response.json()
        pprint(data)

        drinkapi = data['drinks']
        for data in drinkapi:
            drink = data['strDrink']
            picture = data['strDrinkThumb']
            instructions = data['strInstructions']
            ingrediet1 = data['strIngredient1']
            ingrediet2 = data['strIngredient2']
            ingrediet3 = data['strIngredient3']
        print(picture)
        print(f'To make this drink at home the the instructions are {instructions}')
        pprint(f'A good drink with {food} is {drink}')
        print(f'The three main ingredients are {ingrediet1}, {ingrediet2}, and {ingrediet3}')

        return food, drink, picture, instructions, ingrediet1, ingrediet2, ingrediet3
    

    except Exception as e:
        print(e)
        print('There was an error contacting the API')

getcockaildrink()
