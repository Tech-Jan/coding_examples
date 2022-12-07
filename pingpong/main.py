from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

paddle1 = Paddle((350, 30))
paddle2 = Paddle((-350, 0))

ball = Ball()

my_screen = Screen()
my_screen.bgcolor("grey")
my_screen.setup(width=800, height=600)

my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(key="Up", fun=paddle1.pmoveup)
my_screen.onkey(key="Down", fun=paddle1.pmovedown)
my_screen.onkey(key="w", fun=paddle2.pmoveup)
my_screen.onkey(key="s", fun=paddle2.pmovedown)

game_on = True
while game_on:
    time.sleep(0.05)
    ball.move()
    ball.collisionright(paddle1)
    ball.collisionleft(paddle2)
    ball.collisionwall()
    my_screen.update()
    game_on = ball.out()

my_screen.exitonclick()
