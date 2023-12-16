from turtle import Turtle

SCREEN_WIDTH = SCREEN_HEIGTH = 600
MOVE_METER = 10
STARTING_POSITION = (0, -SCREEN_HEIGTH/2 + 2*MOVE_METER)
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.go_to_start()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.speed("fast")
        self.penup()

    def move_up(self):
        self.forward(MOVE_METER)

    def move_down(self):
        self.backward(MOVE_METER)
    
    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)