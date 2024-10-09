from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score  += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER YOUR SCORE IS {self.score}", move=False, align=ALIGNMENT, font=FONT)
                
