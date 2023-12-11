#Heads or tails.
#Generate random number 0 or 1.
#If it is 1 it should be heads. If it is 0 it should be tails.

import random

print("Welcome to the heads&tails generator!")
random = random.randint(0,1)
if random == 1:
    print("It's Heads!")
else:
    print("It's Tails!")