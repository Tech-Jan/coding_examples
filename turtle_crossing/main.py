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
screen.onkey(key="Up", fun=tim.moveup)
car = CarManager()
my_scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if tim.finish():
        my_scoreboard.increase_score()
        car.increase_speed()

    car.create_car()
    car.move_cars()
    if car.collision(tim):
        game_is_on = False
        my_scoreboard.gameover()
time.sleep(10)
