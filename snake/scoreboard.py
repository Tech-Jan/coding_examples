from turtle import Turtle
FONT = ('Courier', 12, 'bold')
ALIGNMENT =  "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,275)
        self.forward(20)
        self.forward(20)
        self.color("brown")
        self.points = 0
        self.write(f"Score = {self.points}", False, align=ALIGNMENT, font= FONT)
        self.hideturtle()


    def increase_score(self):
        self.clear()
        self.points += 1
        self.write(f"Score = {self.points}", False, align="right", font= FONT)

    def gameover(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"U LOST", False, align="right", font=FONT)