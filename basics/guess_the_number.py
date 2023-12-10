import os
import random

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def guess_func(guess, number_to_guess):
    if guess > number_to_guess:
        print("Too High")
    elif guess < number_to_guess:
        print("Too low")
    else:
        print("You won!")
        return True

def set_difficulty(difficulty):
    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    return attempt

def guess_number_game():
    difficulty = input("Choose a difficulty. 'Easy' or 'Hard'?: ").lower()
    attempt_right = set_difficulty(difficulty=difficulty)
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    guess_turn = 0
    user_won = False

    while guess_turn < attempt_right and not user_won:
        print(f"You have {attempt_right-guess_turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        user_won = guess_func(guess=guess, number_to_guess=random_number)

        guess_turn += 1
        if guess_turn == attempt_right and user_won == False:
            print("You've run out of guesses, you lost...\n")
        elif user_won == False:
            print("Guess again.\n")

print("Welcome to the Number Guessing Game!")
will = input("Do you wanna play the game? 'yes' or 'no': ")
while will != "no":
    clear_console()
    guess_number_game()
    will = input("Do you wanna play the game again? 'yes' or 'no': ")

print("See you later then, bye!")
