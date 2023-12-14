from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake.segment_number = 4
snake.create_snake()

screen.update()


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    
    for segment_number in range(len(snake.segments)-1, 0, -1):
        new_x = snake.segments[segment_number - 1].xcor()
        new_y = snake.segments[segment_number - 1].ycor()
        snake.segments[segment_number].goto(new_x,new_y)
    snake.segments[0].forward(20)
    
screen.exitonclick()