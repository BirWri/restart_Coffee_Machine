from menu import MENU
from resources import resources

# Variable to save the profit
money = 0

def check_resources(drink, menu, resources):
    """Check if the coffee machines has enough resources to make requested drink. Return False if
    any of the ingredients are missing"""
    resource_available = True
    for ingredient in menu[drink]['ingredients']:
        if menu[drink]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            resource_available = False

    return resource_available


def calculate_payment(quarters, dimes, nickles, pennies):
    """Calculates how much money the user inserted into the coffee machine"""
    q = quarters*0.25
    d = dimes*0.10
    n = nickles*0.05
    p = pennies*0.01
    x = q + d + n + p
    return x


def deduct_from_resources(drink, menu, resources):
    """Deducts the used ingredients from the machine resources"""
    for ingredient in menu[drink]['ingredients']:
        resources[ingredient] -= menu[drink]['ingredients'][ingredient]

machine_on = True
while machine_on:
    # Ask the user what they would like
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn coffee machine off
    if user_choice == "off":
        machine_on = False
        print("Machined switched off")

    elif user_choice == "report":
        # User can print report of the available resources
        for resource in resources:
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        print(f"Money: ${money}")

    elif not user_choice:
        print("Input missing.")

    elif user_choice != "latte" and user_choice != "espresso" and user_choice != "cappuccino":
        print("Drink doesnt exist")

    else:

        # Check if there are enough resources
        resources_quantity = check_resources(drink=user_choice, menu=MENU, resources=resources)

        # If resources_quantity return False, the coffee machine will switch off
        if not resources_quantity:
            machine_on = False
        else:
            print("Please insert coins:")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))

            # Calculate the money input
            payment = calculate_payment(quarters, dimes, nickles, pennies)

            if payment >= MENU[user_choice]['cost']:
                #Make the drink
                deduct_from_resources(drink=user_choice, menu=MENU, resources=resources)
                #Add money to the bank
                money += MENU[user_choice]['cost']
                #Calculate money back
                if payment > MENU[user_choice]['cost']:
                    money_back = payment - MENU[user_choice]['cost']
                    print(f"Here is ${money_back} dollars in change.")
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print("“Sorry that's not enough money. Money refunded.")










