from turtle import Turtle

PLAYER_ONE_ALIGNMENT = 'left'
PLAYER_TWO_ALIGNMENT = 'right'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-100,200)
        self.write(f"{self.score_left}", move=False, align=PLAYER_ONE_ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.score_right}", move=False, align=PLAYER_TWO_ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f"{self.score_left}", move=False, align=PLAYER_ONE_ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.score_right}", move=False, align=PLAYER_TWO_ALIGNMENT, font=FONT)
        
    def increase_Lscore(self):
        self.clear()
        self.score_left  += 1
        self.update_scoreboard()

    def increase_Rscore(self):
        self.clear()
        self.score_right += 1
        self.update_scoreboard()
