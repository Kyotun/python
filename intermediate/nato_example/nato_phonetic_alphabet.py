import pandas as pd

# An Example to read someones name and check which characters are matching with the phonetic alphabet of NATO.
# Add the matching characters codes to the list
data = pd.read_csv("/Users/kyotun/Desktop/python/intermediate/nato_example/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

is_on = True
phonetic_code_list = []
while is_on:
    try:
        name = input("Please enter your name: ").upper()
        phonetic_code_list = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        print("Thank you for the entry.")
        print("The phonetic code is like this:")
        print(phonetic_code_list)
        is_on = False