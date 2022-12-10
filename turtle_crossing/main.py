import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
screen.listen()
screen.onkey(key="Up",fun=tim.moveup)
car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    tim.finish()
    car.create_car()
    car.move_cars()