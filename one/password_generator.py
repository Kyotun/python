# Generate a password for given amount of letters, symbols and number

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
characters = [letters,numbers,symbols]

print("Hey, welcome to the PyPass Generator!")
letter_amount = int(input("How many letters would you like in your password?: "))
symbol_amount = int(input("How many symbols would you like in your password?: "))
number_amount = int(input("How many numbers would you like in your password?: "))
total_len = letter_amount + symbol_amount + number_amount
password_list = []

def func(pass_list, symbol_list, symbol_amount, str_len):
    random_index = random.randint(0,len(choosen_list)-1)
    pass_list.append(symbol_list[random_index])
    symbol_amount = symbol_amount -1
    str_len = str_len - 1
    return symbol_amount, str_len
    

while total_len > 0:
    random_charlist = random.randint(0,2)
    choosen_list = characters[random_charlist]

    if random_charlist== 0 and letter_amount > 0: 
        #letters
        letter_amount, total_len = func(password_list, choosen_list, letter_amount, total_len)
    elif random_charlist==1 and number_amount > 0:
        #numbers
        number_amount, total_len = func(password_list, choosen_list, number_amount, total_len)
    elif random_charlist==2 and symbol_amount > 0:
        #symbols
        symbol_amount, total_len = func(password_list, choosen_list, symbol_amount, total_len)
    else:
        pass

password_str = ''.join(password_list)
print(f"Password is: {password_str}")

