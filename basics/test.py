#I apply the things in this document, which I new learned.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hands = [
    {
        "user_hand" : random.choices(cards,k=3),
        "user_score" : 0
    },
    {
        "dealer_hand" : random.choices(cards,k=3),
        "dealer_score" : 0
    }
]

user_hand = hands[0]["user_hand"]
dealer_hand = hands[1]["dealer_hand"]

user_score = hands[0]["user_score"] = sum(user_hand)
dealer_score = hands[1]["dealer_score"] = sum(dealer_hand)

for card in user_hand:
    print(card)

print("------")

for card in range(len(user_hand)):
    if user_hand[card] == 11:
        user_hand[card] = 1

for card in user_hand:
    print(card)


# if user_score > 21:
#     for card in user_hand:
#         if card == 11:
#             user_hand[card] = 1