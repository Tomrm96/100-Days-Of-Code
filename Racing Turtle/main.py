from turtle import Turtle, Screen
import random

race_on = False
racers = []
racing_turtle_colours = ['red', 'blue', 'green', 'yellow', 'purple', 'black']
y_positions = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Who will win the race?', prompt='Enter a turtle colour: ')

for turtle in range(0,6):
    racer = Turtle(shape='turtle')
    racer.color(racing_turtle_colours[turtle])
    racer.penup()
    racer.goto(x= -230, y=y_positions[turtle])
    racers.append(racer)

if user_bet:
    race_on = True

while race_on:
    for racer in racers:
        if racer.xcor() >230:
            race_on = False
            winning_turtle = racer.pencolor()
            if winning_turtle == user_bet:
                print('You Won! {turtle} was the winning Turtle!'.format(turtle=winning_turtle))
            else:
                print('You lost :( {turtle} was the winning Turtle!'.format(turtle=winning_turtle))

        racer.forward(random.randint(0,10))

screen.exitonclick()