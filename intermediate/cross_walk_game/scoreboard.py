from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
SCREEN_WIDTH = SCREEN_HEIGHT = 600
GAP = 30
LEFT_CORNER = (-SCREEN_WIDTH/2 + GAP, SCREEN_HEIGHT/2 - GAP)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(LEFT_CORNER)
        self.update_scoreboard()
    
    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)