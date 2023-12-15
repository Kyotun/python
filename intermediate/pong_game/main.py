from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UP = "Up"
DOWN = "Down"
W = "w"
S = "s"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle(screen_width=SCREEN_WIDTH, kind="left")
paddle_right = Paddle(screen_width=SCREEN_WIDTH, kind="right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.up, W)
screen.onkey(paddle_left.down, S)
screen.onkey(paddle_right.up, UP)
screen.onkey(paddle_right.down, DOWN)
 
is_on = True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.check_walls(screen_heigth=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH) 

    """When ball too close to the paddle center and close to the wall, it bounces itself from there."""
    if ball.distance(paddle_right) < 50 and ball.xcor() > 350 or ball.distance(paddle_left) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        """Right side could not hold the ball. Ball switches side."""
        scoreboard.l_wins()
        ball.swtich()
    
    if ball.xcor() < -380:
        """Left side could not hold the ball. Ball switches side."""
        scoreboard.r_wins()
        ball.swtich()
    


screen.exitonclick()