from coffee_machine_menu import MENU, resources


def money_calculator(order):
    """Take inserted money and order as input.
        If the inserted money >= cost of the order, print the prepared object and change amount.
        If money is not enough prints it's not enough."""
    total_money_inserted = 0
    cost = MENU[order]["cost"]
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money_inserted = quarters * 0.01 + dimes * 0.1 + nickles * 0.05 + pennies * 0.25
    change = round(total_money_inserted - cost, 2)
    if total_money_inserted < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resource_regulator(order=order)
        resources["money"] += cost
        print(f"Here is ${change} in change.")
        print(f"Here is your {order}. Enjoy!")


def report():
    """Print the resources left in coffee machine"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


def resource_regulator(order):
    """Decreases the amount of ingredients for prepared order."""
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]


def is_resource_sufficient(order):
    """Checks if the resources for chosen order is enough.
        Returns True if it's enough.
        Returns False if it's not enough."""
    is_sufficient = False
    if resources["milk"] < MENU[order]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        is_sufficient = True
    return is_sufficient


def refill_water():
    """Refills the water tank.
        Prints, it is full, if the water tank is full."""
    if resources["water"] < 300:
        resources["water"] = 300
    else:
        print("Water tank is full!")


def refill_milk():
    """Refills the milk tank.
        Prints, it is full, if the milk tank is full."""
    if resources["milk"] < 200:
        resources["milk"] = 200
    else:
        print("Milk tank is full!")


def refill_coffee():
    """Refills the coffee tank.
        Prints, it is full, if the coffee tank is full."""
    if resources["coffee"] < 100:
        resources["coffee"] = 100
    else:
        print("Coffee tank is full!")


def check_wish(user_input):
    """Takes user input and calls the function according to that wish.
        If user wishes to close the machine with 'off' order, returns False"""
    if user_input == "off":
        return False
    elif user_input == "report":
        report()
    elif user_input == "refill water":
        refill_water()
    elif user_input == "refill milk":
        refill_milk()
    elif user_input == "refill coffee":
        refill_coffee()
    elif is_resource_sufficient(order=user_input):
        money_calculator(order=user_input)
    return True


state_on = True

while state_on:
    # TODO: prepare a menu like 1- ..., 2-..., etc.
    wish = input("What would you like? (espresso/latte/cappuccino): ")
    state_on = check_wish(user_input=wish)

print("See you later, have a nice day!")
