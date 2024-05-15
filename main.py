from menu import MENU
from resources import resources


def check_resources(drink, menu, resources):

    resource_available = True
    if (menu[drink]['ingredients']['water']) > resources['water']:
        print("Sorry there is not enough water.")
        resource_available = False

    if (menu[drink]['ingredients']['coffee']) > resources['coffee']:
        print("Sorry there is not enough coffee.")
        resource_available = False

    if (menu[drink]['ingredients']['milk']) > resources['milk']:
        print("Sorry there is not enough milk.")
        resource_available = False

    return resource_available

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
        resources_quantity = check_resources(drink=user_choice, menu = MENU, resources=resources)

        if resources_quantity == False:
            machine_on = False
        else:
            # Ask coins





