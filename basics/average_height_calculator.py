# Average Height Calculator

print("Welcome to the average height calculator!")

# Ask user the enter the heights of the people in format like -> 192 188 150 172 ...
heights_input = input("Please enter the heights with whitespace between: ")

# Splits the heights into elements of a list. heights[0] = 192, heights[1] = 188, ...
heights = heights_input.split()
sum_of_heights = 0

# Take all the heights turn them into integer from string, and add them in every iteration to the sum_of_heights.
for index in range(0, len(heights)):
    sum_of_heights += int(heights[index])

average_height = sum_of_heights / len(heights)

print(f"Total height: {sum_of_heights}")
print(f"Number of people: {len(heights)}")
print(f"Average height: {average_height}")