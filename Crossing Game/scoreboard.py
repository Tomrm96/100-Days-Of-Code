from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0,260)
        self.level = 1       
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.level  += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER AT LEVEL: {self.level}", move=False, align=ALIGNMENT, font=FONT)