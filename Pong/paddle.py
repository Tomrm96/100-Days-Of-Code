from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, starting_position_x, starting_position_y):
            super().__init__()
            self.color('white')
            self.penup()
            self.shape('square')
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.goto(starting_position_x, starting_position_y)

    def move_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)

