from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

timmy.shape('turtle')

for i in range(3, 10):
    angle = 360/i
    for j in range(i):
        timmy.right(angle)
        timmy.forward(100)


screen.exitonclick()
