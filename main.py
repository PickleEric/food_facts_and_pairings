import food_api
import cocktail_api_setup
import beer_pairing

def main():

    print('Welcome to the Best food facts and pairings')

    while True:

        selection = int(input('Please select from one of the following options \n'
        + ' 1 = Find a cocktail for your food \n'
        + ' 2 = Find food facts for your food and pairing options \n'
        + ' 3 = Find a beer pairing for your food \n'
        + ' 4 = Display your recent saves \n'
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

            


if __name__ == '__main__':
    main()

