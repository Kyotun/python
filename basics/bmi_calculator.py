# BMI Calculator(2)

print("Hey user.")

# Input function stores inputs as 'str' in variables.
# For division, we need to type cast from 'str' to 'float'.
height = float(input("Please enter your height in meter please: "))
weight = float(input("Could you enter your weight in kilograms too: "))

bmi = weight/ (height**2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    