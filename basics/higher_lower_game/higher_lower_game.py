from higher_lower_data import data
from higher_lower_art import logo
from higher_lower_art import vs
import random
import os

def clear_console():
  """Function for clearing the console."""
  os.system('cls' if os.name == 'nt' else 'clear')

def mix_list(list):
    random.shuffle(list)

def next_person(data_list, index):
    name = data[index]["name"]
    follower_count = data[index]["follower_count"]
    description = data[index]["description"]
    country = data[index]["country"]
    return name, follower_count, description, country

def game():
    score = 0
    i = 0
    condition = True
    mix_list(data)
    while condition:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        name_one, follower_count_one, description_one, country_one = next_person(data_list=data, index=i)
        i += 1
        print(f"Compare A: {name_one}, {description_one}, from {country_one}.")
        print(vs)
        name_two, follower_count_two, description_two, country_two = next_person(data_list=data, index=i)
        i += 1
        print(f"Against B: {name_two}, {description_two}, from {country_two}.")
        guess = input("Who has more followers? 'A' or 'B': ")

        clear_console()
        if follower_count_one > follower_count_two and  guess == 'A':
            score += 1
            continue
        elif follower_count_one < follower_count_two and guess == 'B':
            score += 1
            continue
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score is: {score}")
            score = 0
            condition = False
        
game()