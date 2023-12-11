# Choose a random person
import random

# Collect the people
names_string = "A, B, C"

# Choose a delimiter to split the names, here is ", "
names = names_string.split(", ")

# Create a range for to choose a random number from it
num_items = len(names)
random_choice = random.randint(0, num_items-1)

# Choose a random person from the list
random_person = names[random_choice]

print(f"{random_person} will pay the bill.")


