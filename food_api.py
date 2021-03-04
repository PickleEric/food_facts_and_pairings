import requests
import os
from pprint import pprint



def main():
    item=input('what would you like to eat? ')
    data=get_food(item)
    food_items = data['menuItems']
    #pprint(food_items)
    for food in food_items:
        restaurant=extract_restaurant(food)
        choices=extract_different_options(food)
        print(choices, 'restaurant name:', restaurant)



def get_food(order):

    url= 'https://api.spoonacular.com/food/menuItems/search'
    key = os.environ.get('FOOD_API')
    item='%s'%(order)
    params = {'query': item, 'apiKey': key}
    data = requests.get(url, params).json()

    if data:
        return data
    else:
        return None



def extract_different_options(data):
    return data['title']


def extract_restaurant(data):
    return data['restaurantChain']


if __name__ == '__main__':
    main()
