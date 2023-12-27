# Blackjack game.
# The game is builded according to the real life blackjack game
# See the rules of the blackjack game in web, if you don't know.

import random
import os
from blackjack_art import logo


def clear_console():
    """
    Clears the console/terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def take_card():
    """
    Creates a list of card and choose a random card from this list.
    List contains cards as integers.
    11 -> Ace
    10 -> Queen, King, Joker
    Other cards have normal point.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """
    Calculates the score of the given parameter(users hand).
    If sum of the card of given hand is equal 21 and there is just 2 card, returns 0.
    If there is an ace and sum of cards is bigger than 21, ace will be counted as 1 not 11.
    returns the sum of the new created hand.
    """
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    """
    Compare the given two scores -> User score and computer score.
    If both of them went over 21, user loses.
    If equal -> Draw
    If computer/user is 0, computer/user wins.
    If user <=21 and computer went over 21, user wins.
    In other cases, who has bigger sum that person wins.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lost :c"

    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lost, opponent has Blackjack..."
    elif user_score == 0:
        return "Win with a Blackjack ;)"
    elif user_score > 21:
        return "You went over. You lose :("
    elif computer_score > 21:
        return "Opponent went over. You win :)"
    elif user_score > computer_score:
        return "You win :)"
    else:
        return "You lost :c"


def blackjack():
    """
    Starts the game of blackjack. In the beginning creates a empty list for user and computer.
    Append 2 random card to their hand and goes into while loop. Game continues when as long as the 
    conditions are established.
    """
    print(logo)

    user_hand = []
    dealer_hand = []
    game_continues = True

    for _ in range(2):
        user_hand.append(take_card())
        dealer_hand.append(take_card())

    while game_continues:
        user_score = calculate_score(hand=user_hand)
        dealer_score = calculate_score(hand=dealer_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_continues = False
        else:
            will1 = input("Type 'y' to get another card, type 'n' to pass: ")
            if will1 == 'y':
                user_hand.append(take_card())
            else:
                game_continues = False
                
    while dealer_score != 0 and dealer_score < 17:
        """
        If dealer could not win and his score smaller than 17, he should 
        take card.
        """
        dealer_hand.append(take_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Dealers's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))


print(logo)
print("Welcome to the game Blackjack!")
answer = input("Do you want to play a game? 'y' or 'n': ")

while answer == 'y':
    """
    If user wants to play game with answer 'y', clears the console and starts the blackjack game
    from start.
    """
    clear_console()
    blackjack()
    answer = input("Would you like to play another game? 'y' or 'n': ").lower()

print("See you later then!")
