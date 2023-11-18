#Check if someone can ride with rollercoaster.

print("Hey there! You wanne ride with rollercoaster huh?\n Let's see!\n")
height = int(input("Please enter your height: "))

if height > 120:
    print("You can ride with rollercoaster!\nBut we need to check your age for price too!")
    age = int(input("Please enter your age: "))
    if age < 12:
        print("For under 12 is price $5! Enjoy the ride.")
    elif age < 18:
        print("For the age between 12-18 the price is $7. Enjoy the ride!")
    else:
        print("So you're over 18. Price is gonna be $10. Enjoy the ride!")
else:
    print("Unfortunately you're not allowed to ride with rollercoaster...")
    print("Please come back when you're higher than 120. Untill then!")