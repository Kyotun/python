#Tip calculator

print("Hey user. Welcome to the tip calculator")

total_bill = input("Please enter the total amount of the bill: ")
percentage_to_tip = input("Could you please enter the percentage to tip: ")

tip = float(total_bill) / float(percentage_to_tip)

bill_plus_tip = float(total_bill) + tip

number_people_paying = input("Please enter the number of people are paying: ")

each_pay = bill_plus_tip / float(number_people_paying)
print(f"Each person should pay: {each_pay}")
