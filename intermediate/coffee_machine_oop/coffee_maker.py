class CoffeeMaker:
    """CoffeeMaker class, models the machine that makes the coffee
    """

    def __init__(self):
        """In the beginning default water is 300 unit, milk is 200 unit, coffee has 100 unit.
        These are max values.
        """
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.wish = ""

    def format_input(self, user_input):
        """Convert the integer input into requested order.
        If input is 1 convert it to 'espresso'
        2 will be 'cappuccino'
        3 is going to be 'latte'.
        """
        if user_input == 1:
            self.wish = "espresso"
        elif user_input == 2:
            self.wish = "cappuccino"
        elif user_input == 3:
            self.wish = "latte"
        else:
            print("Input is invalid.")

    def refill_water(self):
        """Refills the water tank.
        Prints, it is full, if the water tank is full.
        """
        if self.resources["water"] < 300:
            self.resources["water"] = 300
        else:
            print("Water tank is full!")

    def refill_milk(self):
        """Refills the milk tank.
        Prints, it is full, if the milk tank is full.
        """
        if self.resources["milk"] < 200:
            self.resources["milk"] = 200
        else:
            print("Milk tank is full!")

    def refill_coffee(self):
        """Refills the coffee tank.
        Prints, it is full, if the coffee tank is full.
        """
        if self.resources["coffee"] < 100:
            self.resources["coffee"] = 100
        else:
            print("Coffee tank is full!")

    def report(self):
        """Prints a report of all resources.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
