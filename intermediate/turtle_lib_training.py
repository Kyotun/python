import turtle as t
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('/Users/kyotun/Desktop/python_training/intermediate/image.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

dot_count = 100

t.colormode(255)
alex = t.Turtle()
alex.shape("turtle")
alex.speed("fastest")
alex.penup()

def draw_painting(width, height, step, dot_diameter):
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
