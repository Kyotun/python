#Treasure Island game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
      ''')

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
    