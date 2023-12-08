# Ceaser Cipher program.
import alphabet

def caesar_cipher(input_text, shift_amount ,direction):
    text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        index = alphabet.letter_list.index(letter)
        new_index = index + shift_amount
        shifted_letter = alphabet.letter_list[new_index]
        text += shifted_letter
    print(f"{direction}d text is: {text}")

print("Hello, welcome to the Ceaser Cipher!")
answer = ""
while answer.lower() != "n":
    typ = input("Do you want to 'encode' or 'decode'? ").lower()
    message = input("Type the message please: ").lower()
    shift_number = int(input("Please enter the shift number: "))

    caesar_cipher(input_text=message, shift_amount=shift_number, direction=typ)
    
    answer = input("Do you wanna continue to decode/encode? Y or N: ").lower()
        

