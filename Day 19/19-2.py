from turtle import Turtle, Screen
from random import randint


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
screen = Screen()
x = -300
y = -175
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    y += 50
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.pendown()
    turtles.append(new_turtle)

referee = Turtle(shape='turtle')
r_x = 300
r_y = 200
referee.penup()
referee.goto(r_x, r_y)
referee.right(90)
for i in range(20):
    referee.forward(10)
    referee.penup()
    referee.forward(10)
    referee.pendown()
referee.left(180)

guess = screen.textinput('Make your bet', 'Which turtle will win the race? Enter the color: ')

finish = False
while not finish:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor() >= 300:
            winner = turtle.pencolor()
            finish = True
            if winner == guess:
                print(f'You\'ve won! The {winner} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winner} turtle is the winner!')
            break

screen.exitonclick()
