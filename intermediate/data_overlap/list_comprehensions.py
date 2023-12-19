# List comprehension in integer list
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# List comprehension in string variable
name = "Emir"
letters_list = [letter for letter in name]
print(letters_list)

# List comprehension in range case
my_doubled_list = [2*num for num in range(1, 5)]
print(my_doubled_list)

# List comprehension with condition
names = ["Alex", "Beth", "Caroline", "David", "Elephant", "Freddie"]
long_uppercase_names = [name.upper() for name in names if len(name) > 5]
print(long_uppercase_names)

# List comprehension with fibonacci
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
doubled_numbers = [number * number for number in numbers]
print(doubled_numbers)

# List comprehension with condition(special case: data type converting is necessary)
list_of_strings = input("Enter the number of list with comma(,) between: ").split(',')
numbers = [int(string_number) for string_number in list_of_strings]
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Even numbers were: {even_numbers}")