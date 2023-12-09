#Tip calculator(4)

print("Hey user. Welcome to the tip calculator")

bill = float(input("Please enter the total amount of the bill: $"))
percentage_to_tip = float(input("Could you please enter the percentage to tip: %"))

#Percentage is in 0.x form.
#Divide the percentage_to_tip with 100.
tip_in_percentage = percentage_to_tip / 100
tip = bill * tip_in_percentage

#Total amount that should be payed.
bill_plus_tip = bill + tip

number_people_paying = int(input("Please enter the number of people are paying: "))

#Round the total amount that each should pay by 2 digits.
bill_divided_people = bill_plus_tip / number_people_paying
final_amount = "{:.2f}".format(bill_divided_people)
type(final_amount)
#final_amount = round(bill_divided_people,2)
print(f"Each person should pay: {final_amount}")
