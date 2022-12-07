from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITION=[(0,0),(-20,0),(-40,0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.list = []
        self.create_snake()
        self.length = len(self.list)
        self.head = self.list[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)


    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("turtle")
        snake.color("cyan")
        snake.setposition(position)
        self.list.append(snake)


    def extend(self):
        #asd=self.list[-1].position()
        self.add_segment(self.list[-1].position())


    def move_forward(self):
        self.snake_follow()
        self.list[0].forward(MOVE_DISTANCE)
        # screen.update()

    def up(self):
        if self.list[0].heading() != DOWN:
            self.list[0].setheading(UP)
        # screen.update()

    def down(self):
        if self.list[0].heading() != UP:
            self.list[0].setheading(DOWN)
        # screen.update()

    def left(self):
        if self.list[0].heading() != RIGHT:
            self.list[0].setheading(LEFT)
        # screen.update()

    def right(self):
        if self.list[0].heading() != LEFT:
            self.list[0].setheading(RIGHT)
        # screen.update()

    def snake_follow(self):
        for i in range(1, len(self.list), 1):
            self.list[-i].setposition(self.list[-i - 1].position())
            self.list[-i].setheading(self.list[-i - 1].heading())
