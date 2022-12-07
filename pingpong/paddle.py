from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position)

    def pmoveup(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 30)

    def pmovedown(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y - 30)
