from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):
        for i in range(0,3):
            snake = Turtle()
            snake.shape('square')
            snake.color('white')
            snake.penup()
            snake.goto(x=STARTING_POSITIONS[i], y=0)
            self.snakes.append(snake)


    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[i-1].xcor()
            new_y = self.snakes[i-1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
