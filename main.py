from menu import MENU
from resources import resources


def check_resources(drink, menu, resources):
#refractor the code to not depend on kewords... as milk is missing in one drink and is causing an error
    resource_available = True
    if (menu[drink]['ingredients']['water']) > resources['water']:
        print("Sorry there is not enough water.")
        resource_available = False

    if (menu[drink]['ingredients']['coffee']) > resources['coffee']:
        print("Sorry there is not enough coffee.")
        resource_available = False

    if not menu[drink]['ingredients']['milk']:
        return resource_available
    else:
        if (menu[drink]['ingredients']['milk']) > resources['milk']:
            print("Sorry there is not enough milk.")
            resource_available = False
            return resource_available

def calculate_payment(quarters, dimes, nickles, pennies):
    q = quarters*0.25
    d = dimes*0.10
    n = nickles*0.05
    p = pennies*0.01
    x = q + d + n + p
    print(x)
    return x

def deduct_from_resources(drink, menu, resources):
    resources['water'] = resources['water'] - menu[drink]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - menu[drink]['ingredients']['coffee']
    if menu[drink]['ingredients']['milk']:
        resources['milk'] = resources['milk'] - menu[drink]['ingredients']['milk']

machine_on = True
while machine_on:
    # Ask the user what they would like
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(user_choice)

    # Turn coffee machine off
    if user_choice == "off":
        machine_on = False
        print("Machined switched off")

    elif user_choice == "report":
        # User can print report of the resources / MAKE IT INTO A FUNCTION
        print(f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Milk: {resources['coffee']}ml\n"
                f"Money: ${resources['money']}")

    elif not user_choice:
        print("Input missing.")

    elif user_choice != "latte" and user_choice != "espresso" and user_choice != "cappuccino":
        print("Drinks doesnt exist")

    else:

        # Check if there are enough resources
        # Make a function that takes user_choice, menu and resources, as an input
        resources_quantity = check_resources(drink=user_choice, menu=MENU, resources=resources)

        if not resources_quantity:
            machine_on = False
        else:
            print("Please insert coins:")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))

            # Add error handling for input here

            # Calculate the money input
            payment = calculate_payment(quarters, dimes, nickles, pennies)

            if payment >= MENU[user_choice]['cost']:
                #Make coffee
                deduct_from_resources(drink=user_choice, menu=MENU, resources=resources)
                #Add money to the bank

                #Calculate money back
                if payment > MENU[user_choice]['cost']:
                    money_back = payment - MENU[user_choice]['cost']
                    print(f"Here is ${money_back} dollars in change.")
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print("“Sorry that's not enough money. Money refunded.")










