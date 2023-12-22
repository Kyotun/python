# Generate a password for given amount of letters, symbols and number
# Passwords that generated contains the given amount of letters, symbols and number but in random placement.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_new_password():
    letter_amount = random.randint(8,10)
    symbol_amount = random.randint(3,5)
    number_amount = random.randint(2,4)

    password_list = []
    
    password_letters = [random.choice(letters) for _ in range (letter_amount)]
    password_symbols = [random.choice(symbols) for _ in range (symbol_amount)]
    password_numbers = [random.choice(numbers) for _ in range (number_amount)]
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    
    generated_password = "".join(password_list)
    return generated_password


