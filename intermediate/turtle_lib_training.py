import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

t.colormode(255)
alex = t.Turtle()
alex.shape("turtle")
alex.color("red")
directions = [0, 90, 180, 270, 360]
alex_speed_list = ["fastest", "fast", "slow", "normal", "slowest"]

pen_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
for _ in range(300):
    alex.pensize(random.randint(1,15))
    alex.color(random_color())
    alex.speed(random.choice(alex_speed_list))
    alex.forward(20)
    alex.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
