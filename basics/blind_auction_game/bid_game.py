# Bid Game
# Secret bid game.
# Every person bids, if the bidder gave the highest amount His/Her name will stay in the winnder list.
# Winner list is dictionary in our case.

import os
from bid_game_art import logo


def clear_console():
    """Clears the console/terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bid(bid_record):
    """Iterates through given dict, finds the new highest bid and takes the name of the bidder.
    Assigns the winner to the bidders name and highest bid to his/hers bid."""
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


bids = {}
answer = ""

print(logo)
print("Welcome to the bid game!")
print("Game starts now.")

while answer != "no":
    """If there is no more bidder left, auction is over."""
    name = input("What is your name?: ")
    bid = int(input("what is your bid?: $"))
    bids[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    clear_console()

find_highest_bid(bids)
