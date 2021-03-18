import requests
from pprint import pprint

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

def getcockaildrink(food):   # pass the food in as an argument

    try:
        data = make_cocktail_api_request(url)   # mock this call 
       
        pprint(data)

        drinkapi = data['drinks']

        # there's a loop here but you are only using the last item in the list 
        for data in drinkapi:
            drink = data['strDrink']
            picture = data['strDrinkThumb']
            instructions = data['strInstructions']
            ingredient1 = data['strIngredient1']
            ingredient2 = data['strIngredient2']
            ingredient3 = data['strIngredient3']

        return food, drink, picture, instructions, ingredient1, ingredient2, ingredient3
    

    except Exception as e:
        print(e)
        print('There was an error contacting the API')


def make_cocktail_api_request(url):  # mock this in order to test 
    return requests.get(url).json()  


# for manually testing this module 
if __name__ == '__main__':
    food = input('What food would like like a cocktail to pair with? ')
    getcockaildrink(food)
