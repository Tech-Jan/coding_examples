from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("Black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def moveup(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False
