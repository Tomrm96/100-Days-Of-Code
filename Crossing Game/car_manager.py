from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()   
            car.shape('square')
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            RANDOM = random.randint(-250, 250)
            car.goto(300, RANDOM)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT