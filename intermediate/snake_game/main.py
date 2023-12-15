from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = 1000
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGTH)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(segment_number=5, screen_width=SCREEN_WIDTH, screen_heigth=SCREEN_HEIGTH)
food = Food(screen_height=SCREEN_HEIGTH, screen_width=SCREEN_WIDTH)
score_board = Scoreboard(screen_heigth=SCREEN_HEIGTH)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(score_board.move_speed)

    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        score_board.increase_score()
        snake.extend()
    
    if snake.check_wall():
        is_on = False
        score_board.game_over()

    if snake.check_collision():
        is_on = False
        score_board.game_over()

        

    
    
screen.exitonclick()