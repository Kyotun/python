# Methamatical calculator.
# Apply the given operation(adding, substracting, multiplying, dividing) for the given to numbers.

from mathematical_calculator_art import logo


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

will = ""
output = 0


def calculator():
    """
    Prints the operations as symbols.
    Takes the first number from user as float input.
    Asks user to which operation to apply.
    Asks user to give the second number.
    Asks user to if he/she wants to do more calculation with the answer.
    If 'y', number1 is answer and asks user to next operation and the other number.
    """
    print(logo)

    print("Operations:")
    for symbol in operations:
        print(symbol)
    number1 = float(input("Please enter the first number: "))
    do_continue = True

    while do_continue:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print("You entered an invalid operation. Please try again.")
            continue

        number2 = float(input("Please enter the second number: "))

        func = operations[operation]
        output = func(number1=number1, number2=number2)

        print(f"Answer is: {number1} {operation} {number2} = {output}")

        will = input(
            f"Type 'y' to continue calculating with the answer, type 'n' to start a new calculation, or 'exit' to finish to calculating: ").lower()

        if will == 'y':
            number1 = output
        elif will == 'n':
            do_continue = False
            calculator()
        elif will == "exit":
            print("That was very funny. Take care of yourself, bye!")
            break


calculator()
