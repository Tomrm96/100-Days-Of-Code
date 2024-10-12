from turtle import Turtle 



class Ball(Turtle):
    def __init__(self, starting_position_x, starting_position_y):
            super().__init__()
            self.color('white')
            self.penup()
            self.shape('circle')
            self.x_move = 10
            self.y_move = 10
            self.ball_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)



    def bounce(self):
        self.y_move *= -1

    def deflect(self):
         self.x_move *= -1
         self.adjust_ball_speed


    def reset(self):
         self.ball_speed = 0.1
         self.goto(0,0)
         self.deflect()


    def adjust_ball_speed(self):
        if self.ball_speed == 0.001:
            pass
        else:
            self.ball_speed *= 0.7

