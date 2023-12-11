#Pizza service calculator
#Calculate the price of the pizzas for given ingredients and size.

bill = 0
print("Thank you for choosing us!")
print("The menu is here!")
print("S size: $15")
print("M size: $20")
print("L size: $25")
size = input("Please enter the size: ")

print("\nExtra pepperoni costs +$2 for S and +3$ for others.")
add_pepperoni = input("Do you want pepperoni(Y or N): ")

print("\nExtra cheese costs +$1 for any kind.")
extra_cheese = input("Extra cheese?(Y or N): ")

if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
else:
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1

print(f"Total bill is {bill}. Enjoy your pizza!")