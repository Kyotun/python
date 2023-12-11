# Find the highest number from the given input list

print("Hey! Welcome to the highest number finder!")
numbers_str = input("Please enter the numbers with whitespace between: ")
numbers = numbers_str.split()

# String to integer as list
for index in range(0, len(numbers)):
    numbers[index] = int(numbers[index])

highest_score = 0
max = 0
# Find the highest number comparing to former heighest score
for number in range(0, len(numbers)):
    if numbers[index] > highest_score:
        max = numbers[index]

print(f"Maximum number from given input is: {max}")