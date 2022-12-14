from turtle import Turtle
import random
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 0:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def collision(self, myturtle):
        for car in self.all_cars:
            if car.distance(myturtle) < 20:
                return True
        return False

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
