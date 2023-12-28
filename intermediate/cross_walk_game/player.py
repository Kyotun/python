from turtle import Turtle

SCREEN_WIDTH = SCREEN_HEIGTH = 600
MOVE_METER = 10
STARTING_POSITION = (0, -SCREEN_HEIGTH/2 + 2*MOVE_METER)
FINISH_LINE_Y = 280

class Player(Turtle):
    """Player class inherit from Turtle class.
    Default shape is turtle, color white, speed fast.
    """
    def __init__(self):
        super().__init__()
        self.go_to_start()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.speed("fast")
        self.penup()

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_METER)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_METER)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_METER)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_METER)
    
    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y
    
    def at_border(self):
        return self.ycor() < -SCREEN_HEIGTH/2 or self.xcor() > SCREEN_WIDTH/2
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)