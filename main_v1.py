from data import MENU, resources

PENNIES = .01
NICKELS = .05
DIMES = .10
QUARTERS = .25

machine_on = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0


def process_selection(choice):
    global profit

    if choice == "report":
        display_resources()
        display_money_collected(profit)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_ingredients(choice):
            amount_received = process_payment()
            drink_cost = MENU[choice]["cost"]
            if amount_received > drink_cost:
                refund_amount = amount_received - drink_cost
                profit += drink_cost
                deduct_ingredients(choice)
                print(f"Here is ${round(refund_amount, 2)} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif choice == "off":
        global machine_on
        machine_on = False


def display_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def check_ingredients(drink):
    have_ingredients = True
    for keys, value in MENU[drink]["ingredients"].items():
        if resources[keys] < MENU[drink]["ingredients"][keys]:
            print(f" * Sorry there is not enough {keys}.")
            have_ingredients = False

    return have_ingredients


def process_payment():
    print("Please insert coins.")
    payment = 0.00
    payment += collect_payment("quarters")
    payment += collect_payment("dimes")
    payment += collect_payment("nickels")
    payment += collect_payment("pennies")
    return payment


def collect_payment(coin):
    if coin == "quarters":
        return int(input("    How many quarters? ")) * QUARTERS
    elif coin == "dimes":
        return int(input("    How many dimes? ")) * DIMES
    elif coin == "nickels":
        return int(input("    How many nickels? ")) * NICKELS
    elif coin == "pennies":
        return int(input("    How many pennies? ")) * PENNIES
    else:
        return 0


def display_money_collected(money):
    print(f"Money: ${money}")


def deduct_ingredients(drink):
    for keys, value in MENU[drink]["ingredients"].items():
        resources[keys] -= MENU[drink]["ingredients"][keys]


while machine_on:
    process_selection(input("What would you like? (espresso/latte/cappuccino): ").lower())
