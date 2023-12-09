#Week calculator(3)

#In 1 year there is total of 52 weeks
#Max year is 90
one_year_in_weeks = 52
max_age = 90

print("Hey User.")
age = input("Please enter your age: ")
age_as_int = int(age)

#Calculate the actual age in weeks
age_in_weeks = age_as_int * one_year_in_weeks

#Calculate the total weeks have been lived
life_limit_in_weeks = max_age * one_year_in_weeks

#Calculate the total weeks left
weeks_left = life_limit_in_weeks - age_in_weeks

print(f"You have {weeks_left} weeks left.")