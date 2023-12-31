# Generate a password for given amount of letters, symbols and number
# Passwords that generated contains the given amount of letters, symbols and number but in random placement.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Hey, welcome to the PyPass Generator!")
letter_amount = int(input("How many letters would you like in your password?: "))
symbol_amount = int(input("How many symbols would you like in your password?: "))
number_amount = int(input("How many numbers would you like in your password?: "))

password_list = []

for char in range(0,letter_amount+1):
    password_list.append(random.choice(letters))

for char in range(0,number_amount+1):
    password_list.append(random.choice(numbers))

for char in range(0,symbol_amount+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"Password is: {password}")

