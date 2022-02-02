import colorgram
from turtle import Turtle, Screen, colormode
from random import choice


colors = []
palette = colorgram.extract('image.png', 20)
for color in palette:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors.append((r, g, b))

timmy = Turtle()
screen = Screen()

colormode(255)
timmy.shape('turtle')
timmy.hideturtle()
timmy.pensize(10)
timmy.speed('fastest')
timmy.penup()
x = -225
y = -225

for i in range(10):
    timmy.goto(x, y)
    for j in range(9):
        timmy.color(choice(colors))
        timmy.dot()
        timmy.forward(50)
    timmy.color(choice(colors))
    timmy.dot()
    y += 50

timmy.hideturtle()
screen.exitonclick()
