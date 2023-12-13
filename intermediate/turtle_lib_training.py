import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        alex.color(random_color())
        alex.circle(50)
        alex.setheading(alex.heading() + size_of_gap)

t.colormode(255)
alex = t.Turtle()
alex.shape("turtle")
heading = 5
alex.speed("fastest")

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
