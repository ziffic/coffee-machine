from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()
espresso = MenuItem("Espresso", 50, 0, 18, 1.5)
latte = MenuItem("Espresso", 200, 150, 24, 2.5)
cappuccino = MenuItem("Espresso", 250, 100, 24, 3.0)


machine_on = True


def process_selection(choice):
    if choice == "off":
        global machine_on
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


while machine_on:
    options = menu.get_items()
    process_selection(input(f"What would you like? ({options}): ").lower())
