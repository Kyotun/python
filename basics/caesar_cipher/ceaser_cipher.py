# Ceaser Cipher program.
# Encode or decode the given string in the given direction with the given number of character.

# Examples:
# Input: encode the string "Hello World" with shift number 9.
# Input: decode the string "Ajkak Kakjs" with the shift number 19.

import alphabet
from caesar_art import logo


def caesar_cipher(input_text, shift_amount, direction):
    text = ""
    shift_amount = shift_amount % 26
    if direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet.letter_list:
            index = alphabet.letter_list.index(char)
            new_index = index + shift_amount
            shifted_letter = alphabet.letter_list[new_index]
            text += shifted_letter
        else:
            text += char
    print(f"{direction}d text is: {text}")


print(logo)
print("Hello, welcome to the Ceaser Cipher!")
answer = ""
while answer.lower() != "n":
    typ = input("Do you want to 'encode' or 'decode'? ").lower()
    message = input("Type the message please: ").lower()
    shift_number = int(input("Please enter the shift number: "))

    caesar_cipher(input_text=message, shift_amount=shift_number, direction=typ)

    answer = input("Do you wanna continue to decode/encode? Y or N: ").lower()

print("Goodbye!")
