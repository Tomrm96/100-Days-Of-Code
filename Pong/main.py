from turtle import Screen
from paddle import Paddle
from ball import Ball



screen = Screen()
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)
ball = Ball(0, 0)

game_ON = True

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(False)
screen.listen()

screen.onkey(left_paddle.move_up, 'Up')
screen.onkey(left_paddle.move_down, 'Down')

screen.onkey(right_paddle.move_up, 'w')
screen.onkey(right_paddle.move_down, 's')


while game_ON:
    ball.move()
    screen.update()


screen.exitonclick()