#Treasure Island game
from treasure_island_art import logo
print(logo)

print("Welcome to the Treasure Island! Beware of your choices!")
left_or_right = input("You wanna go to left or right?\n")

if left_or_right.lower() == "left":
    print("\nAlright.")
    print("You arrived a shore.")
    swim_or_wait = input("Are you gonna swim or wait?\n")
    if(swim_or_wait.lower() == "wait"):
        print("\nGood one!")
        print("Now you have to choose a boat.")
        print("There are 3 boats with different colours...")
        colour_of_boat = input("Red, White or Black?\n")
        if colour_of_boat.lower() == "black":
            print("\nYou went to the treasure island and found the treausre :)")
        else:
            print("\nYour boat has crushed into a rock and you drowned, game is over...")
    else:
        print("\nYou drowned, game is over...")
else:
    print("\nYou fell into a hole, game is over!")
    