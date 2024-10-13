from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score  += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open('Snake Game/data.txt', mode='r') as high_score:
            return int(high_score.read())

    def update_high_score(self):
        with open('Snake Game/data.txt', mode='w') as high_score:
            high_score.write(str(self.score))