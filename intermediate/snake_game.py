from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    segments.append(new_turtle)

for index in range(len(segments)-1):
    segments[index+1].goto(segments[index].xcor()+20,segments[index].ycor())

screen.update()


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    
    for segment_number in range(len(segments)-1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x,new_y)
    segments[0].forward(20)
    
screen.exitonclick()