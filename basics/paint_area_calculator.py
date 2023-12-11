# Calculate the area that should be painted for given coverage.
import math


def paint_calculation(height, width, cover):
    num_cans = height * width / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


wall_height = int(input("Please enter the height of wall: "))
wall_width = int(input("Please enter the width of wall: "))
coverage = int(input("Please enter the coverage area: "))
paint_calculation(height=wall_height, width=wall_width, cover=coverage)
