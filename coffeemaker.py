import os
clear = lambda: os.system('cls')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}

def make_coffee(MENU, resources, coffee_choice):
    resources["money"] += MENU[coffee_choice]["cost"]
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"] 
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    print(f" Here is your {coffee_choice}. Enjoy!")


def money_count(MENU, coffee_choice):
    user_quarters = int(input("how many quarters? "))
    user_dimes = int(input("how many dimes? "))
    user_nickels = int(input("how many nickels? "))
    user_pennies = int(input("how many pennies? "))
    total_paid = float((user_quarters * .25) + (user_dimes * .10) + (user_nickels * .05) + (user_pennies * .01))
    drink_cost = float(MENU[coffee_choice]["cost"])
    total_change = total_paid - drink_cost
    total_change = float("{:.2f}".format(total_change))
    return total_change


def check_resources(MENU, resources, coffee_choice):
    if MENU[coffee_choice]["ingredients"]["water"] > resources["water"]:
        print("Add water to coffee machine")
        return False
    elif MENU[coffee_choice]["ingredients"]["milk"] > resources["milk"]:
        print("Add milk to coffee machine")
        return False
    elif MENU[coffee_choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Add coffee to coffee machine")
        return False
    else:
        return True
    


def coffee_maker(resources, MENU):
    coffee_choice = input("What would you like? (espresso, latte, or cappucino) ")
    if coffee_choice == "off":
        return
    elif coffee_choice == "report":
        print(resources)
        coffee_maker(resources, MENU)
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappucino":
        check_resources(MENU, resources, coffee_choice)
        if check_resources:
            total_change = money_count(MENU, coffee_choice)
            if total_change >= 0:
                make_coffee(MENU, resources, coffee_choice)
                coffee_maker(resources, MENU)
            else:
                print("Not enough funds, money refunded")
                coffee_maker(resources, MENU)
        else:
            coffee_maker(resources, MENU)


coffee_maker(resources, MENU)


