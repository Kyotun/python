import turtle as t
import random


def random_color():
    """
    Choose a random integer between [0,255] for variables r, g and b.
    Returns a tuple (r,g,b).
    """
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    """
    Take size of gap as parameter. Size of gap -> Angle difference between circles.
    Draw a circle and put a angle difference(given parameter size_of_gap) between the next circle and
    draws the next circle.
    """
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