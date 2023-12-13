from turtle import Turtle, Screen
import random

alex = Turtle()
alex.shape("turtle")
alex.color("red")
directions = [0, 90, 180, 270, 360]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
alex_speed_list = ["fastest", "fast", "slow", "normal", "slowest"]

pen_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
for _ in range(300):
    alex.pensize(random.randint(1,15))
    alex.color(random.choice(colours))
    alex.speed(random.choice(alex_speed_list))
    alex.forward(20)
    alex.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
