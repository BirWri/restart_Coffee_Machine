from menu import MENU
from resources import resources

def check_resources(drink, menu, resources):
    print(menu[drink]['ingredients']['water'])


machine_on = True
while machine_on:
    # Ask the user what they would like
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(user_choice)

    # Turn coffee machine off
    if user_choice == "off":
        machine_on = False
        print("Machined switched off")
    else:

        # User can print report of the resources
        if user_choice == "report":
            print(f"Water: {resources['water']}ml\n"
                  f"Milk: {resources['milk']}ml\n"
                  f"Milk: {resources['coffee']}ml\n"
                  f"Money: ${resources['money']}")

        # Check if there are enough resources
        # Make a function that takes user_choice, menu and resources, as an input
        check_resources(drink=user_choice, menu = MENU, resources=resources)




