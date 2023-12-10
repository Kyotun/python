import os
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def check_the_guess(guess, number_to_guess):
    if guess > number_to_guess:
        print("Too High")
    elif guess < number_to_guess:
        print("Too low")
    else:
        print("You won!")

def set_difficulty():
    difficulty = input("Choose a difficulty. 'Easy' or 'Hard'?: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def guess_number_game():
    attempt_right = set_difficulty()
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    guess_turn = 0
    guess = 0
    user_won = False

    while guess_turn < attempt_right and random_number != guess:
        print(f"You have {attempt_right-guess_turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_the_guess(guess=guess, number_to_guess=random_number)

        guess_turn += 1
        if guess_turn == attempt_right and random_number != guess:
            print("You've run out of guesses, you lost...\n")
        elif random_number != guess:
            print("Guess again.\n")

print("Welcome to the Number Guessing Game!")
will = input("Do you wanna play the game? 'yes' or 'no': ")
while will == "yes":
    clear_console()
    guess_number_game()
    will = input("Do you wanna play the game again? 'yes' or 'no': ")

print("See you later then, bye!")
