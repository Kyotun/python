from turtle import Turtle, Screen

alex = Turtle()
alex.shape("arrow")
alex.color("red")

for _ in range(10):
    alex.penup()
    alex.forward(10)
    alex.pendown()
    alex.forward(10)





screen = Screen()
screen.exitonclick()
