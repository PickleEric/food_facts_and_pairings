import food_api
import cocktail_api_setup
import beer_pairing
import database

def main():

    print('Welcome to the Best food facts and pairings')

    while True:

        selection = int(input('Please select from one of the following options \n'
        + ' 1. Enter food to search for'  # find food info AND cocktail info AND beer info 
        + ' 2. Display your recent saves \n'
        + ' Press any other number to quit: '))

        if selection == 1:
            get_food_and_drink_info()

        elif selection == 2:
            show_saved_data()

        else:
            print('bye!')

      

def get_food_and_drink_info():

    food_search = input('enter the food: ')

    # todo call food info api function 
    food = food_api.get_food(food_search)  # this method will return a Food object 

    # todo call beer info api function
    beer = beer_pairing.get_beer()

    # this will become an object, see the Beer class 
    cocktail = cocktail_api_setup.get_cockail_drink(food_search)
    
    # todo display all information 
    # probably call a function 

    display_results(food_search, food, beer, cocktail)
    # print(picture)

    # # create a function to display the info 
    # print(f'To make this drink at home the the instructions are {instructions}')
    # print(f'A good drink with {food} is {drink}')
    # print(f'The three main ingredients are {ingredient1}, {ingredient2}, and {ingredient3}')

    # todo ask use if they want to save this info 

    save = input('Do you want to save this? Enter Y for yes')
    if save == 'Y':
        save(food, cocktail, beer)
    


def display_results(food_search, food, beer, cocktail):
    # todo present information neatly 
    pass 


def show_saved_data():
    all_saved_data = database.get_all_food_and_drink_info()
    for data in all_saved_data:
        display_results(data.food_search, data.food, data.beer, data.cocktail)


if __name__ == '__main__':
    main()

