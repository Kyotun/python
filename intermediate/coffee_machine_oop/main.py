from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("Welcome to the coffee machine!")
while is_on:
    print("\nNeeded Ingredients and costs for drinks:")
    menu.get_items()
    print("\nMenu:")
    print("1- Make espresso.")
    print("2- Make cappuccino.")
    print("3- Make latte.")
    print("4- Refill water.")
    print("5- Refill milk.")
    print("6- Refill coffee.")
    print("7- Report the resources.")
    print("8- Close the machine.")
    wish = int(input("Please press the number that should be processed: "))
    if wish == 8:
        is_on = False
    elif wish == 7:
        coffee_maker.report()
        money_machine.report()
    elif wish == 6:
        coffee_maker.refill_coffee()
    elif wish == 5:
        coffee_maker.refill_milk()
    elif wish == 4:
        coffee_maker.refill_water()
    elif 4 > wish > 0:
        coffee_maker.format_input(wish)
        drink = menu.find_drink(coffee_maker.wish)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(order=drink)
    else:
        print("Please enter a valid option.")

print("See you later then!")
