#Average Height Calculator

print("Welcome to the average height calculator!")
heights_input = input("Please enter the heights with whitespace between: ")

heights = heights_input.split()
sum_of_heights = 0

for index in range(0, len(heights)):
    sum_of_heights += int(heights[index])

average_height = sum_of_heights / len(heights)

print(f"Total height: {sum_of_heights}")
print(f"Number of people: {len(heights)}")
print(f"Average height: {average_height}")