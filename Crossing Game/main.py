import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
cars = CarManager()
player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(False)
screen.listen()

screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move_car()

    for car in cars.cars:
       if car.distance(player) < 20:
           game_is_on = False
           scoreboard.game_over()

    if player.at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_score()

screen.exitonclick()