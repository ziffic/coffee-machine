from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

machine_on = True
espresso = MenuItem("Espresso", 50, 0, 18, 1.5)
latte = MenuItem("Espresso", 200, 150, 24, 2.5)
cappuccino = MenuItem("Espresso", 250, 100, 24, 3.0)
m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()


def str_to_class(choice):
    return getattr(sys.modules[__name__], choice)


def process_selection(choice):
    if choice == "report":
        cm.report()
        mm.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink_choice = str_to_class(choice)
        if cm.is_resource_sufficient(drink_choice):
            if mm.make_payment(drink_choice.cost):
                cm.make_coffee(drink_choice)
    elif choice == "off":
        global machine_on
        machine_on = False


while machine_on:
    process_selection(input("What would you like? (espresso/latte/cappuccino): ").lower())
