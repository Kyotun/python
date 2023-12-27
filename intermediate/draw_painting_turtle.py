import turtle as t
import random
import colorgram

rgb_colors = []
# Colorgram extracts 30 colors from image
colors = colorgram.extract('/Users/kyotun/Desktop/python_training/intermediate/image.jpeg', 30)

for color in colors:
    # Extract every r, g and b segment of extracted colors(amount of 30 in this case) of image 'image.jpeg'
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

dot_count = 100

# Create our little turtle, penup cause we don't want to draw lines between the dots.
t.colormode(255)
alex = t.Turtle()
alex.shape("turtle")
alex.speed("fastest")
alex.penup()


def draw_painting(width, height, step, dot_diameter):
    """
    Takes the width and height of frame as parameter.
    Takes distance between dots as parameter 'step'.
    Takes dot_diameter as last parameter.
    In the beginning, moves the turtle a little bit to south west and sets heading to east.
    Choose a random color from extracted colors from image and put a dot to current location and
    moves the turtle 1 step(given as parameter) forward.
    If turtle is at the edge of frame, add 1 to the height and turtles goes to the beginning of the frame.
    Continues with putting dots till the dot count is completed.
    """
    alex.setheading(225)
    alex.forward(300)
    alex.setheading(0)
    dot_count = width * height
    for dot in range (1,dot_count+1):
        alex.color(random.choice(rgb_colors))
        alex.dot(dot_diameter)
        alex.forward(step)
        if dot % width == 0 and dot != dot_count:
            alex.left(90)
            alex.forward(step)
            alex.left(90)
            alex.forward(step * width)
            alex.left(180)

draw_painting(5, 7, 50, 20)


screen = t.Screen()
screen.exitonclick()
