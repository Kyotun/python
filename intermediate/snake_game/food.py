from turtle import Turtle
import random
SCREEN_GAP = 30

class Food(Turtle):
    """Food Class inherit from Turtle class.
    parameters are screen width and height should be given for accurate results.
    Shape is default circle, color is red, speed is fastest.
    """
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
        """Picks a random location within the screen and put the food in that randomly chosen location.
        """
        random_x = random.randint(- (self.screen_width/2 - SCREEN_GAP), self.screen_width/2 - SCREEN_GAP)
        random_y = random.randint(- (self.screen_height/2 - SCREEN_GAP), self.screen_height/2 - SCREEN_GAP)
        self.goto(random_x, random_y)
