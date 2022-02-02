from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.color('purple')

for i in range(4):
    timmy.right(90)
    timmy.forward(100)

screen.exitonclick()
