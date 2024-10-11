from turtle import Turtle 


class Ball(Turtle):
    def __init__(self, starting_position_x, starting_position_y):
            super().__init__()
            self.color('white')
            self.penup()
            self.shape('circle')
            self.goto(starting_position_x, starting_position_y)



    def move(self):
        self.goto(300, 140)


    def move_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)

