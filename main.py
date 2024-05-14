import menu
from resources import resources

# Ask the user what they would like
user_choice = input("What would you like? (espresso/latte/cappuccino): ")
print(user_choice)

# User can print report of the resources
if user_choice == "report":
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Milk: {resources['coffee']}ml\n"
          f"Money: ${resources['money']}")





