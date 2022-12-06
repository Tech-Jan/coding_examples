import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

screen = Screen()
screen.setup(width=700, height=800)

turtles = []

tim = Turtle()
tim.shape("turtle")
turtles.append(tim)

tom = Turtle()
tom.shape("turtle")
tom.color("red")
turtles.append(tom)

lum = Turtle()
lum.shape("turtle")
lum.color("pink")
turtles.append(lum)

felt = Turtle()
felt.shape("turtle")
felt.color("brown")
turtles.append(felt)

is_race_on = False

width = 700
height = 500

i = 1
for turtle_index in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.goto(-width / 2 + 20, -height / 2 + i * 50)
    turtles.append(tim)
    i += 1

screen.listen()
my_bet = screen.textinput(title="hey Race", prompt="who will winenter:")
turtles[0].goto(-width / 2 + 20, -height / 2 + 50 + 300)
tom.goto(-width / 2 + 20, -height / 2 + 50 + 400)
lum.goto(-width / 2 + 20, -height / 2 + 50 + 450)
felt.goto(-width / 2 + 20, -height / 2 + 50 + 555)
for turtle in turtles:
    turtle.clear()

if my_bet:
    is_race_on = True

while is_race_on:
    rand_disctance = random.randint(0, 10)
    current_turtle = turtles[random.randint(0, len(turtles) - 1)]
    current_turtle.forward(29)
    if not current_turtle.pos()[0] < 250:
        is_race_on = False

screen.exitonclick()
