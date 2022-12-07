import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
print(snake)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("hunt the food")
screen.tracer(0)

food = Food()

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="s", fun=snake.move_forward)

score = Scoreboard()

game_on = True

while game_on == True:
    snake.move_forward()
    screen.update()
    time.sleep(0.1)

    # detect collision food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect_collision with border
    if snake.head.xcor() > 280 or snake.head.xcor() < -289 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.gameover()
        game_on = False

    #detect collion with snake
    for segment in snake.list[1:]:
        if snake.head.distance(segment) < 10:
            score.gameover()
            game_on = False

screen.exitonclick()
