fruits = input("Please enter the names of the fruits: ").split(",")

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f"Error mesage: {error_message}, index was: {index}, number of item was: {len(fruits)}")
    else:
        print(fruit + "pie!")

make_pie(2)