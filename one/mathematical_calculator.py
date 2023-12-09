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


answer = ""
output = 0


while answer != "n":

    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))

    print("Operations:")
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Please enter the operation: ")

    if( operation == "+"):
        output = add(number1=number1, number2=number2)
    elif( operation == "-"):
        output = substract(number1=number1, number2=number2)
    elif( operation == "*"):
        output = multiply(number1=number1, number2=number2)
    elif( operation == "/"):
        output = divide(number1=number1, number2=number2)
    else:
        print("You entered an invalid operation. Please try again.")
        continue

    print(f"The result is: {output}")

    answer = input("Do you wanna continue? 'y' or 'n': ").lower()


print("That was very funny. Take care of yourself, bye!")