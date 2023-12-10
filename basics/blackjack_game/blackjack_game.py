import random
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def take_card(hand):
    hand.append(random.choice(cards))
    return hand

def calculate_score(hand):
    score = sum(hand)
    return score

def ace_hand(hand, score):
    if score > 21:
        for index in range(len(hand)):
            if hand[index] == 11 and sum(hand) > 21:
                hand[index] = 1
    score = calculate_score(hand=hand)
    return hand, score

def blackjack():
    user_hand = []
    dealer_hand = []

    game_will = ""
    game_continues = True

    user_hand = take_card(user_hand)
    dealer_hand = take_card(dealer_hand)

    while game_continues:
        user_hand = take_card(user_hand)
        dealer_hand = take_card(dealer_hand)

        user_score = calculate_score(hand=user_hand)
        dealer_score = calculate_score(hand=dealer_hand)

        user_hand, user_score = ace_hand(hand=user_hand, score=user_score)
        dealer_hand, dealer_score = ace_hand(hand=dealer_hand, score=dealer_score)

        if user_score > 21:
            print(f"Your final hand: {user_hand}")
            print(f"Computer's final hand: {dealer_hand}")
            print(f"{user_score} - {dealer_score}, You lost!")

        elif dealer_score > 21:
            print(f"Your final hand: {user_hand}")
            print(f"Computer's final hand: {dealer_hand}")
            print(f"{user_score} - {dealer_score}, You won!")

        else:
            print(f"Your cards: {user_hand}")
            print(f"Computer's cards(s): {dealer_hand[:-1]}")

            will1 = input("Type 'y' to get another card, type 'n' to pass: ")

            if will1 == 'n':
                print(f"Your final hand: {user_hand}")
                print(f"Computer's final hand: {dealer_hand}")

                if user_score > dealer_score:
                    print(f"{user_score} - {dealer_score}, You won!")
                elif user_score < dealer_score:
                    print(f"{user_score} - {dealer_score}, You lost!")
                else:
                    print(f"{user_score} - {dealer_score}, It's a draw!")

            elif will1 == 'y':
                continue

        game_will = input("Do you want to play another game? Type 'y' or 'n': ").lower()
        if game_will == 'y':
            game_continues = False
            blackjack()
        else:
            break



print(logo)
print("Welcome to the game Blackjack!")
answer = input("Do you want to play a game? 'y' or 'n': ")

if answer == 'y':
    blackjack()

print("See you later then!")