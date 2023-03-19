from turtle import Turtle, Screen
from padle import Padle
import time
turtle = Turtle()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
padle = Padle()


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(fun=padle.move_down, key='Down')
    screen.onkey(fun=padle.move_up, key='Up')

print(padle.shapesize())
screen.exitonclick()