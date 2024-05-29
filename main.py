from menu import MENU
from resources import resources


def check_resources(drink, menu, resources):

    resource_available = True
    for ingredient in menu[drink]['ingredients']:
        if menu[drink]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
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
    for ingredient in menu[drink]['ingredients']:
        resources[ingredient] -= menu[drink]['ingredients'][ingredient]

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
        for resource in resources:
            print(f"{resource.capitalize()}: {resources[resource]}ml")

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










