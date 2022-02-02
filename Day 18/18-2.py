from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.color('purple')

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
