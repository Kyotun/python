#Rock-paper-scissors game

import random
from rock_paper_scissors_art import rock, paper, scissors
images = [rock, paper, scissors]

print("Hey! Welcome the the rock-paper-scissors game!")
print("Please type 0 for rock, 1 for paper and 2 for scissors.")
choise = int(input("Please choose one: "))

if (choise > 2 or choise < 0):
    print("Please enter a valid number.")
else:
    print(f"Your choice: {choise}")
    
    choise_random = random.randint(0,2)
    print(f"Computers choice: {choise_random}")

    if (choise > 2 or choise < 0):
        print("Please enter a valid number.")
    elif choise == choise_random:
        print(f"Your choice: {images[choise]} \nComputer choice: {images[choise_random]}")
        print("It's a draw!")
    elif ((choise - choise_random) == 1) or ((choise - choise_random) == -2):
        print(f"Your choice: {images[choise]} \nComputer choice: {images[choise_random]}")
        print("You won, congratulations!")
    else:
        print(f"Your choice: {images[choise]} \nComputer choice: {images[choise_random]}")
        print("You lost :(.") 
