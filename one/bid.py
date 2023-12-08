#Bid Game
#Secret bid game.
#Every person bids, if the bidder gave the highest amount His/Her name will stay in the winnder list.
#Winner list is dictionary in our case.
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


answer = ""
winner_dict = {
    "name": "empty",
    "bid" : 0
}

print("Welcome to the bid game!")
print("Game starts now.")

while answer != "no":

    name = input("What is your name?: ")
    bid = int(input("what is your bid?: $"))

    if(bid > winner_dict["bid"]):
        winner_dict["name"] = name
        winner_dict["bid"] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    clear_console()

print(f"The winner is {winner_dict["name"]} with a bid of ${winner_dict["bid"]}!")