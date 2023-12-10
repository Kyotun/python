import random
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_hand(hand, score):
    if score > 21:
        for index in range(len(hand)):
            if hand[index] == 11 and sum(hand) > 21:
                hand[index] = 1
    score = sum(hand)
    return hand, score, score

def blackjack():
    game_will = ""
    game_continues = True

    hands = [
        {
            "user_hand" : random.choices(cards),
            "user_score" : 0
        },
        {
            "dealer_hand" : random.choices(cards),
            "dealer_score" : 0
        }
    ]


    while game_continues:
        hands[0]["user_hand"].append(random.choice(cards))
        hands[1]["dealer_hand"].append(random.choice(cards))

        user_hand = hands[0]["user_hand"]
        dealer_hand = hands[1]["dealer_hand"]

        user_score = hands[0]["user_score"] = sum(user_hand)
        dealer_score = hands[1]["dealer_score"] = sum(dealer_hand)

        user_hand, user_score, hands[0]["user_score"] = ace_hand(hand=user_hand, score=user_score)
        dealer_hand, dealer_score, hands[1]["dealer_score"] = ace_hand(hand=dealer_hand, score=dealer_score)

        if user_score > 21:
            print(f"Your final hand: {user_hand}")
            print(f"Computer's final hand: {dealer_hand}")
            print("You lost!")

        elif dealer_score > 21:
            print(f"Your final hand: {user_hand}")
            print(f"Computer's final hand: {dealer_hand}")
            print("You won!")

        else:
            print(f"Your cards: {user_hand}")
            print(f"Computer's cards(s): {dealer_hand[:-1]}")

            will1 = input("Type 'y' to get another card, type 'n' to pass: ")

            if will1 == 'n':
                print(f"Your final hand: {user_hand}")
                print(f"Computer's final hand: {dealer_hand}")

                if user_score > dealer_score:
                    print("You won!")
                elif user_score < dealer_score:
                    print("You lost!")
                else:
                    print("It's a draw!")

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