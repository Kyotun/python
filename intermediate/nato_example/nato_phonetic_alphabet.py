import pandas as pd

# An Example to read someones name and check which characters are matching with the phonetic alphabet of NATO.
# Add the matching characters codes to the list
phonetic_dict = pd.read_csv("intermediate/nato_example/nato_phonetic_alphabet.csv")
phonetic_code_list = []

name = input("Please enter your name: ").upper()
for (index, row) in phonetic_dict.iterrows():
    if row.letter in name:
        phonetic_code_list.append(row.code)
    
print(phonetic_code_list)