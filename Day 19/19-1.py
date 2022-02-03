from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(10)


def backward():
    timmy.forward(-10)


def turn_right():
    timmy.right(10)


def turn_left():
    timmy.left(10)


def clear():
    timmy.penup()
    timmy.goto(0, 0)
    timmy.pendown()
    timmy.clear()


timmy.shape('turtle')
timmy.speed('fastest')

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')
screen.onkey(clear, 'c')
screen.listen()
screen.exitonclick()
