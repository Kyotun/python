PLACEHOLDER = "[name]"

with open("intermediate/automation_special_text/Input/Letters/starting_letter.txt") as text_file:
    text_to_send = text_file.read()
    text_file.close()

with open("intermediate/automation_special_text/Input/Names/invited_names.txt") as name_file:
    names_list = name_file.readlines()
    name_file.close()

for name in names_list:
    name = name.strip()
    text = text_to_send.replace(PLACEHOLDER, name)
    file = open(f"intermediate/automation_special_text/Output/ReadyToSend/letter_for_{name}.txt", mode="w")
    file.write(text)
    file.close()
