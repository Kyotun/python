from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCREEN_GAP = 30

class Scoreboard(Turtle):
    def __init__(self, screen_heigth):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, screen_heigth/2 - SCREEN_GAP)
        self.score = 0
        self.color("white")
        self.update_score_board()
    

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)


    def update_score_board(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score_board()