#Generate heads or tails.

import random

print("Welcome to the heads&tails generator!")
random = random.randint(0,1)
if random == 1:
    print("It's Heads!")
else:
    print("It's Tails!")