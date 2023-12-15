from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Updating scoreboard. Clear the all scores first. 
        Then make them go to their places again and write the 
            scores of the each side."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    
    def l_wins(self):
        """If left side scores(if right side could not hold the ball) 
            left side will gain point and scoreboard will be updated."""
        self.l_score += 1
        self.update_scoreboard()

    def r_wins(self):
        """If right side scores(if left side could not hold the ball) 
            right side will gain point and scoreboard will be updated."""
        self.r_score += 1
        self.update_scoreboard()

