# Calculate the sum of even numbers in a given range

print("Welcome to the even number adder!")

end_range  = int(input("Please enter the right end of the range(from 0 to ...): "))

sum_of_even_numbers = 0
# Add 1 to include last number
# Add step of 2 to get just even numbers.
for number in range(0, end_range+1, 2):
    sum_of_even_numbers += number

print(f"Range was from 0 to {end_range}")
print(f"Sum of even numbers in that range: {sum_of_even_numbers}")