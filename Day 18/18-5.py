from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


angles = [0, 90, 180, 270]
colors = ['purple', 'dodger blue', 'lime green', 'orange']

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
# timmy.pensize(5)
timmy.speed('fastest')
colormode(255)

for i in range(360):
    timmy.color(random_color())
    timmy.circle(150)
    timmy.right(1)

screen.exitonclick()
