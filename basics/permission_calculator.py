# Check if someone can ride with roller coaster.
# Price types differs whether the person is older or younger.P

print("Hey there! You wanna ride with roller coaster huh?\n Let's see!\n")
height = int(input("Please enter your height: "))

bill = 0
if height > 120:
    print("You can ride with roller coaster!\nBut we need to check your age for price too!")
    age = int(input("Please enter your age: "))

    if age < 12:
        bill = 5
        print("Child tickets are $5! Enjoy the ride.")
    elif age < 18:
        bill = 7
        print("For youths the price is $7. Enjoy the ride!")
    elif 45 <= age <= 55:
        print("You have a right for a free ride. Enjoy it!")
    else:
        bill = 10
        print("So you're adult 18. Price is gonna be $10. Enjoy the ride!")
    
    wants_photo = input("By the way, do you want a photo taken? Y or N:")
    if wants_photo == 'Y':
        bill += 3

    print(f"The bill is :{bill}")

else:
    print("Unfortunately you're not allowed to ride with roller coaster...")
    print("Please come back when you're higher than 120. Untill then!")