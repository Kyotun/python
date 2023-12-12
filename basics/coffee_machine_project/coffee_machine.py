from coffee_machine_menu import MENU, resources


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


def report():
    """Print the resources left in coffee machine"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


def format_input(user_input):
    """Convert the integer input into requested order.
        If input is 1 convert it to 'espresso'
        2 will be 'cappuccino'
        3 is going to be 'latte'."""
    if user_input == 1:
        return "espresso"
    elif user_input == 2:
        return "cappuccino"
    elif user_input == 3:
        return "latte"
    else:
        print("Input is invalid.")


def money_taker():
    print("Please insert coins")
    total_money_inserted = int(input("How many quarters?: ")) * 0.01
    total_money_inserted += int(input("How many dimes?: ")) * 0.1
    total_money_inserted += int(input("How many nickles?: ")) * 0.05
    total_money_inserted += int(input("How many pennies?: ")) * 0.25
    return total_money_inserted


def make_coffee(order):
    """Decreases the amount of ingredients for prepared order.
            At the end prints the order."""
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    print(f"Here is your {order}. Enjoy!")


def money_calculator(order):
    """Take inserted money and order as input.
        If the inserted money >= cost of the order, print the prepared object and change amount.
        If money is not enough prints it's not enough."""
    order = format_input(user_input=order)
    cost = MENU[order]["cost"]
    total_money_inserted = money_taker()
    change = round(total_money_inserted - cost, 2)
    if total_money_inserted < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += cost
        print(f"Here is ${change} in change.")
        make_coffee(order=order)


def is_resource_sufficient(order):
    """Checks if the resources for chosen order is enough.
        Returns True if it's enough.
        Returns False if it's not enough."""
    order = format_input(user_input=order)
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient} for {order}")
            return False
    return True


def check_wish(user_input):
    """Takes user input and calls the function according to that wish.
        If user wishes to close the machine with integer input 8, returns False.
        Otherwise, do the wished action and returns True."""
    if user_input == 8:
        return False
    elif user_input == 7:
        report()
    elif user_input == 4:
        refill_water()
    elif user_input == 5:
        refill_milk()
    elif user_input == 6:
        refill_coffee()
    elif is_resource_sufficient(order=user_input):
        money_calculator(order=user_input)
    return True


state_on = True

while state_on:
    print("Hello!")
    print("1- Make espresso.")
    print("2- Make cappuccino.")
    print("3- Make latte.")
    print("4- Refill water.")
    print("5- Refill milk.")
    print("6- Refill coffee.")
    print("7- Report the resources.")
    print("8- Close the machine.")
    wish = int(input("What would you like to do?: "))
    state_on = check_wish(user_input=wish)

print("See you later, have a nice day!")
