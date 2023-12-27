from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCREEN_GAP = 30

class Scoreboard(Turtle):
    """Scoreboard class inherit from Turtle class.
    Screen height should be as parameter given for the placement of scoreboard.
    As default, color is white.
    """
    def __init__(self, screen_heigth):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, screen_heigth/2 - SCREEN_GAP)
        self.score = 0
        self.highest_score = 0
        self.read_highest_score()
        self.color("white")
        self.update_score_board()
        self.move_speed = 0.1
    

    def reset(self):
        """Resets the scoreboard.
        If current score higher than the past highest score, current score will be saved as highest score.
        """
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            with open("intermediate/snake_game/highest_score.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_score_board()
    

    def read_highest_score(self):
        with open("intermediate/snake_game/highest_score.txt") as file:
            self.highest_score = file.read()
            file.close()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)


    def update_score_board(self):
        self.clear()
        self.write(f"Score = {self.score}, Highest Score = {self.highest_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score_board()
        self.move_speed *= 0.9