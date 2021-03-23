import requests
import os
from pprint import pprint

# todo decide what data you'll return - keep it simple if possible 

def display(pairing):
    index=1
    print('here is list of food that will be good with th wine')
    #pprint(pairing)
    for food in pairing:
       print('food', index, food)
       index=index+1


def get_description(data):
    return data['text']

def get_pairing(data):
    return data['pairings']


def get_food(order):

    url= 'https://api.spoonacular.com/food/wine/dishes'
    key = os.environ.get('FOOD_API')
    wine='%s'%(order)
    params = {'wine': wine, 'apiKey': key}
    data = requests.get(url, params).json()

    if data:
        return data
        # do you need to do more proccesing?
    else:
        return None



def extract_different_options(data):
    return data['title']


def extract_restaurant(data):
    return data['restaurantChain']

