#Trasure map game

line1 = ["□","□","□"]
line2 = ["□","□","□"]
line3 = ["□","□","□"]
map = [line1, line2, line3]
abc= ["a", "b", "c"]

print(f"{line1}\n{line2}\n{line3}")
print("Hiding your treasure! X marks the spot.")
print("Horizontal line is -> 1, 2, 3")
print("Vertical line is -> a, b, c")
position = input("Where do you want to store the treasure?\n")

letter = position[0].lower()
letter_index = abc.index(letter)

number_index = int(position[1])-1

map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")


