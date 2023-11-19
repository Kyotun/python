#Love calculator

#Calculate the love score 
#based on the characters occur in names of a couple

print("Hey! Welcome to the love calculator!")
name1 = input("Please enter the first name: ")
name2 = input("Please enter the second name")

combined_names = name1 + name2
lower_names = combined_names.lower()

t =lower_names.count("t")
r =lower_names.count("r")
u =lower_names.count("u")
e =lower_names.count("e")
first_digit = t + r + u + e

l =lower_names.count("l")
o =lower_names.count("o")
v =lower_names.count("v")
e =lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit)+str(second_digit))

if (score == 0):
    print("You guys unmatching names, sorry...") 
elif(score < 20):
    print("You two have a bad match.")
elif(score < 40):
    print("Not too bad.")
elif(score < 60):
    print("You achieved around the avarage, good!")
elif(score < 80):
    print("You're great, give it your all to better it!")
else:
    print("You guys are perfect!")
