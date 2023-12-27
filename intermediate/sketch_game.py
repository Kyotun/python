# Create turtle, move turtle to different directions while pen is down(turtle draws while moving)

from turtle import Turtle, Screen

alex = Turtle()
screen = Screen()

def move_forward():
    alex.forward(10)

def move_backward():
    alex.backward(10)

def turn_left():
    alex.left(10)

def turn_right():
    alex.right(10)

def reset_all():
    alex.clear()
    alex.penup()
    alex.home()
    alex.pendown()

def quit_game():
    return False

def left_bow_forward():
    turn_left()
    move_forward()

def right_bow_forward():
    turn_right()
    move_forward()

def left_bow_backward():
    turn_left()
    move_backward()

def right_bow_backward():
    turn_right()
    move_backward()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset_all, "c")

screen.onkey(left_bow_forward, "q")
screen.onkey(right_bow_forward, "e")
screen.onkey(left_bow_backward, "y")
screen.onkey(right_bow_backward, "x")

screen.exitonclick()
    