from turtle import Turtle

SCREEN_PADDLE_GAP = 30


class Paddle(Turtle):
    def __init__(self, screen_width, kind):
        """Screen width is the length of x axis.
        Kind: If paddle should be positioned in left side -> 'left'
        Otherwise kind is 'right'.
        """
        super().__init__()
        self.screen_width = screen_width
        self.kind = kind
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.settle_paddle(self.kind)
    
    def settle_paddle(self, paddle_kind):
        """Set the paddle left or right for given string 'paddle_kind'.
        There are two possiblity. 'left' or 'right'.
        """
        half_of_width = self.screen_width/2
        if paddle_kind == "left":
            self.goto(-(half_of_width - SCREEN_PADDLE_GAP), 0)
        elif paddle_kind == "right":
            self.goto(half_of_width - SCREEN_PADDLE_GAP, 0)
    
    def up(self):
        """Move the paddle 20 pixel in direction of +y.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle 20 pixel in direction of -y.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
