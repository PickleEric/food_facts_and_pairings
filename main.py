import requests
import os
from pprint import pprint

from food import get_food, get_pairing, get_description, display


def main():
    wine=input('enter the name of the wine: ')
    data=get_food(wine)
    pairing=get_pairing(data)
    description=get_description(data)
    display(pairing)




if __name__ == '__main__':
    main()
