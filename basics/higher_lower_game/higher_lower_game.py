from higher_lower_data import data
from higher_lower_art import logo, vs
import random
import os

def clear_console():
  """Function for clearing the console."""
  os.system('cls' if os.name == 'nt' else 'clear')

def pull_account_information(account):
    """Takes the account as dictionary and returns the name, 
        description and country of that person as printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}."

def check_guess(guess, follower_one, follower_two):
    """Take the guess of user and follower counts and returns a bool if they got the guess True or False."""
    if follower_one > follower_two:
        return guess == 'A'
    else:
        return guess == 'B'

def check_score(condition, score):
    """Takes the condition(if the user knew the right answer) and current score.
        Add 1 to score if condition is true and prints the score. Otherwise prints users last score and lost the game print."""
    if condition == True:
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        return 0
    
def game():
    score = 0
    got_it_right = True
    print(logo)

    # Game countinues if the user got the right answer.
    while got_it_right:
        # Choose unique 2 person from list in format of dict.
        random_two_person = random.sample(data,2)

        # Print the information of choosen people.
        print(f"Compare A: {pull_account_information(random_two_person[0])}" )
        print(vs)
        print(f"Against B: {pull_account_information(random_two_person[1])}")

        # Take the guess as input from user
        guess = input("Who has more followers? 'A' or 'B': ")

        # Save the follower counts of the people
        follower_one = random_two_person[0]["follower_count"]
        follower_two = random_two_person[1]["follower_count"]

        # Check if the user knew the answer.
        got_it_right = check_guess(guess=guess, follower_one=follower_one, follower_two=follower_two)
        clear_console()
        print(logo)

        # If the user got it right, give a score and print his/hers score.
        # Or print that he/she lost the game.
        score = check_score(score=score, condition=got_it_right)

game()