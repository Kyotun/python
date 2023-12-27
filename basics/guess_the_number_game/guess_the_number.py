# Generate a number between [1, 100]
# Print out too low or too high according to the guessed number.
# If the choosen number is 70, and user guess below 70 the output will be: "Too low"
# There are two mods. Easy or Hard.
# Easy mod has 10 right for guessing, Hard mod has 5 right.

import os
import random
from guess_the_number_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def clear_console():
    """
    Function for clearing the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def check_the_guess(guess, number_to_guess, turn):
    """
    Takes the guess, random generated number and turn left to make guess as input.
    If the guess is wrong, decrease the number of turns and returns it.
    If the guess is right, prints 'You won!'.
    """

    if guess > number_to_guess:
        print("Too High")
        return turn - 1
    elif guess < number_to_guess:
        print("Too low")
        return turn - 1
    else:
        print("You won!")


def set_difficulty():
    """
    Asks user for difficulty. There are two options. 'easy' or 'hard'.
    If difficulty is easy, returns EASY_LEVEL_TURNS which equals to 10.
    If difficulty is hard, returns HARD_LEVEL_TURNS which equals to 5."""

    difficulty = input("Choose a difficulty. 'Easy' or 'Hard'?: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS


def guess_number_game():
    """
    Sets the difficulty of game(easy or hard). Easy has 10, hard has 5 turn.
    Generate a random number between [1-100].
    Takes guesses as input from the user.
    It ends if the attempt right of user is 0 or user wins.
    """

    print(logo)
    attempt_right = set_difficulty()
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    guess = 0
    user_won = False

    while attempt_right != 0 and random_number != guess:
        print(f"You have {attempt_right} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt_right = check_the_guess(guess=guess, number_to_guess=random_number, turn=attempt_right)

        if attempt_right == 0 and guess != random_number:
            print("You've run out of guesses, you lost...\n")
        elif guess != random_number:
            print("Guess again.\n")


print("Welcome to the Number Guessing Game!")
will = input("Do you wanna play the game? 'yes' or 'no': ")
while will == "yes":
    clear_console()
    guess_number_game()
    will = input("Do you wanna play the game again? 'yes' or 'no': ")

print("See you later then, bye!")
