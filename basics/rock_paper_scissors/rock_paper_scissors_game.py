# Rock-paper-scissors game

import random
from rock_paper_scissors_art import rock, paper, scissors
images = [rock, paper, scissors]

print("Hey! Welcome the the rock-paper-scissors game!")
print("Please type 0 for rock, 1 for paper and 2 for scissors.")
choice = int(input("Please choose one: "))

# 0 -> Rock
# 1 -> Paper
# 2 -> Scissors
if choice > 2 or choice < 0:
    """
    Choice should be either 0, 1 or 2.
    """
    print("Please enter a valid number.")
else:
    print(f"Your choice: {choice}")
    
    # Choose a random option for computer.
    choice_random = random.randint(0,2)
    print(f"Computers choice: {choice_random}")

    # 0 -> Rock
    # 1 -> Paper
    # 2 -> Scissors
    # (Substract) 2-1 = 1, Scissors vs Paper (Scissors win)
    # 1 - 0 = 1, Paper vs Rock (Paper wins)
    # 0 - 2 = -2, Rock vs Scissors (Rock wins)
    if choice > 2 or choice < 0:
        print("Please enter a valid number.")
    elif choice == choice_random:
        print(f"Your choice: {images[choice]} \nComputer choice: {images[choice_random]}")
        print("It's a draw!")
    elif ((choice - choice_random) == 1) or ((choice - choice_random) == -2):
        print(f"Your choice: {images[choice]} \nComputer choice: {images[choice_random]}")
        print("You won, congratulations!")
    else:
        print(f"Your choice: {images[choice]} \nComputer choice: {images[choice_random]}")
        print("You lost :(.") 
