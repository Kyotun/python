#Leap year calculator
#Calculate if a year leap is
#Every year that is divisible by 4 with no remainder

#Except every year that is evenly divisible by 100 with no remainder
#Unless the year is divisible by 400 with no remainder

print("Hey! This is leap year calculator!")
year = int(input("Please enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a leap year!")
        else:
            print("This year is not a leap year, sorry.")
    else:
        print("This year is a leap year!")
else:
    print("This year is not a leap year, sorry.")