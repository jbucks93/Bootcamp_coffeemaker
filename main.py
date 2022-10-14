from oop_menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from oop_money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
options = menu.get_items()

is_on = True

while is_on:
    options = menu.get_items()
    drink_choice = input(f"What would you like? {options}")
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



