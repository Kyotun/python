from turtle import Turtle
import random

DIRECTION_MULTIPLIER = [-1,1]
MOVE_SPEED = 10
SPEED_DECREASE_MULTIPLIER = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("circle")
        self.x_move = MOVE_SPEED
        self.y_move = MOVE_SPEED
        self.move_speed = 0.1

    def move(self):
        """Move function of the ball.
           Adds a constant value to its x and y coordinates and increase the coordinates to their limits."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    

    def bounce_y(self):
        """Reverses the direction of the ball in direction of y-axis."""
        self.y_move *= -1
    

    def bounce_x(self):
        """Reverses the direction of the ball in direction of x-axis."""
        self.x_move *= -1
        self.move_speed *= SPEED_DECREASE_MULTIPLIER

    
    def check_walls(self, screen_width, screen_heigth):
        """As parameters screen width and screen hegith should be given.
           Calculates the distance between the walls and the ball. If the distance between a ball and wall
           is too litle, ball will bounce back. If this wall parallel to y-axis, ball resets itself."""
        x_cor = self.xcor()
        y_cor = self.ycor()
        upper_heigth = screen_heigth/2
        lower_heigth = -upper_heigth
        right_side = screen_width/2
        left_side = -right_side

        if upper_heigth - y_cor < 15 or y_cor - lower_heigth < 15:
            self.bounce_y()

    
    def swtich(self):
        """Switches the direction of the ball if the bal hitted a wall one of two sides.
           X-axis direction will be reversed but y-axis direction will be randomly chosen.
           Either 1 or -1.(Up or down.)"""
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= random.choice(DIRECTION_MULTIPLIER)
        self.move_speed = 0.1