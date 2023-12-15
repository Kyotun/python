from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(- (self.screen_width/2 - 30), self.screen_width/2 - 30)
        random_y = random.randint(- (self.screen_height/2 - 30), self.screen_height/2 - 30)
        self.goto(random_x, random_y)
