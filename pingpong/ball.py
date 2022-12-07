import random
from turtle import Turtle

startspeedx = 6
startspeedy = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.goto(-300, 0)
        self.ballx = startspeedx
        self.bally = random.randint(0, startspeedx)
        self.timespeed=0.03

    def move(self):
        self.goto(self.xcor() + self.ballx, self.ycor() + self.bally)

    def speedx(self):
        self.ballx *= -1
        self.timespeed = 0.9*self.timespeed

    def speedy(self):
        a = 10
        self.bally = random.triangular(0, 3,abs(a)) * int([-1, 1][random.randrange(2)])

    def collisionright(self, objectr):
        # with paddleright
        if self.xcor() > objectr.xcor() - 25:
            if objectr.ycor() + 60 > self.ycor() > objectr.ycor() - 60:
                self.speedx()
                self.speedy()

    def collisionleft(self, objectl):
        if self.xcor() < objectl.xcor() + 25:
            if objectl.ycor() + 60 > self.ycor() > objectl.ycor() - 60:
                self.speedx()
                self.speedy()

    def collisionwall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bally *= -1

    def out(self):
        if self.xcor() > 400 or self.xcor() < -400:
            print("game over")
            return False
        else:
            return True
