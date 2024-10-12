from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WALLS = (270,-270)

screen = Screen()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball(0, 0)
scoreboard = Scoreboard()

game_ON = True

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(False)
screen.listen()



screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')


while game_ON:

    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)


    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.deflect()

    # Right Paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_Lscore()

    # Left Paddle
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_Rscore()

screen.exitonclick()