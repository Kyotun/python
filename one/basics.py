#BMI Calculator

print("Hey user.")

#Input function stores inputs as 'str' in variables.
#For division we need to type cast from 'str' to 'float'.
height = input("Please enter your height in meter please: ")
height_float = float(height)

print("Thank you.")

weight = input("Could you enter your weight in kilograms too: ")
weight_float = float(weight)

#Turn division to str to be able to concat the strings.
print("Your BMI is: " + str(weight_float/(height_float**2)))

