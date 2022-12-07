import random
from turtle import Turtle

startspeedx = 6
startspeedy = 3


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

    def move(self):
        self.goto(self.xcor() + self.ballx, self.ycor() + self.bally)

    def speedx(self):
        self.ballx = - (abs(self.ballx) + 1) * self.ballx / (abs(self.ballx))

    def speedy(self):
        a = abs(round(self.ballx))
        self.bally = random.randint(0, a) * int([-1, 1][random.randrange(2)])

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
            self.bally = -self.bally

    def out(self):
        if self.xcor() > 400 or self.xcor() < -400:
            print("game over")
            return False
        else:
            return True
