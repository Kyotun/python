# Ceaser Cipher program.
import alphabet

def encrypt(plain_text, shift_amount):
    encrypted_text = text_creator(plain_text, shift_amount)
    print(f"Encrypted text is: {encrypted_text}")

def decrypt(plain_text, shift_amount):
    decrypted_text = text_creator(plain_text, -shift_amount)
    print(f"Decrypted text is: {decrypted_text}")

def text_creator(plain_text, shift_amount):
    text = ""
    for letter in plain_text:
        index = alphabet.letter_list.index(letter)
        new_index = index + shift_amount
        shifted_letter = alphabet.letter_list[new_index]
        text += shifted_letter
    return text


print("Hello, welcome to the Ceaser Cipher!")
answer = ""
while answer.lower() != "n":
    typ = input("Do you want to 'encode' or 'decode'? ").lower()
    message = input("Type the message please: ").lower()
    shift_number = int(input("Please enter the shift number: "))

    if(typ == "encode"):
        encrypt(plain_text=message, shift_amount=shift_number)
    else:
        decrypt(plain_text=message, shift_amount=shift_number)
    
    answer = input("Do you wanna continue to decode/encode? Y or N: ").lower()
        

