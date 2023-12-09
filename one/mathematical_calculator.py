#Methamatical calculator.
#Apply the given operation(adding, substracting, multiplying, dividing) for the given to numbers.


def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

will = ""
output = 0

def calculator():
    print("Operations:") 
    for symbol in operations:
        print(symbol)
    number1 = int(input("Please enter the first number: "))
    do_continue = True

    while do_continue:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print("You entered an invalid operation. Please try again.")
            continue

        number2 = int(input("Please enter the second number: "))

        func = operations[operation]
        output = func(number1=number1, number2=number2)

        print(f"{number1} {operation} {number2} = {output}")

        will = input(f"Type 'y' to continue calculating with the answer, type 'n' to start a new calculation, or 'exit' to finish to calculating: ").lower()

        if will == 'y':
            number1 = output
        elif will == 'n':
            do_continue = False
            calculator()
        elif will == "exit":
            print("That was very funny. Take care of yourself, bye!")
            break


calculator()