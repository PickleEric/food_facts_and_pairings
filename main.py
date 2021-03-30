import food_api
import cocktail_api_setup
import beer_pairing
import sqlite_db.database
db = sqlite_db.database

def main():

    print('Welcome to the Best food facts and pairings')

    while True:

        selection = int(input('Please select from one of the following options \n'
        + ' 1 = Enter food to search for \n'
        + ' 2 = Display your recent saves \n'
        + ' 3 = Save entry?'
        + ' Press any other number to quit: '))

        if selection == 1:
            cocktail_api_setup.getcockaildrink()
        #elif selection == 2:
           # food_api.get_food()
        elif selection == 3:
            beer_pairing.main()
        #elif selection == 4:
            #NEEDSQLMODULE TO WORK GET INFORMATION saved by user
        else:
            exit()
def get_food_drink_info():

    food_search = input('Enter food:')
            
    food = food_api.get_food(food_search)
    beer = beer_pairing.get_beer()
    cocktail = cocktail_api_setup.getcockaildrink(food_search)

    display_results(food_search, food, beer, cocktail)

    save = input('Bookmark this pairing? Y or N')
    if save == 'Y':
        save(food, cocktail, beer)
    elif save == 'N':
        main()
    else:
        quit()

def display_results(food_search, food, beer, cocktail):

    print(f'You searched: {food_search}')
    print(f'Food information: {food}')
    print(f'Beer: {beer}')
    print(f'cocktail: {cocktail}')
def save(food_search, food, beer, cocktail):
    
    pass

def show_save_data():
    all_saved_data = db.save_pairing()
    for data in all_saved_data:
        display_results(data.food_search, data.food, data.beer, data.cocktail)

if __name__ == '__main__':
    main()

