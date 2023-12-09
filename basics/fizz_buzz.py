#Fizz Buzz game
# Number % 3 == 0 -> Fizz
# Number % 5 == 0 -> Buzz
# When both conditions are meet -> FizzBuzz

print("Hey, welcome to the fizzbuzz game!\nLet's play!")
target = int(input("Please enter number for end range: "))
for number in range(1,target+1):
    if(number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)
