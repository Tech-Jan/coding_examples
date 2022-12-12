from turtle import Turtle
FONT = ('Courier', 12, 'bold')
class writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 275)
        self.forward(20)
        self.forward(20)
        self.color("black")
        self.points = 0
        self.hideturtle()

    def increase_score(self, position, country):
        self.goto(position)
        self.points += 1
        self.write(f"{country}", False, align="right", font=FONT)