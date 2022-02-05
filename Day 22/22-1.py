# set field
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.title('My Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

r_paddle = Paddle('right')
l_paddle = Paddle('left')
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.move()
    # detect collision with walls
    if ball.ycor() > 285 or ball.ycor() < -275:
        ball.bounce_wall()
    # detect collision with paddles
    if ball.xcor() > 325:
        if ball.distance(r_paddle) < 50:
            ball.bounce_paddle()
        elif ball.xcor() > 390:
            ball.spawn()
            scoreboard.l_point()
    elif ball.xcor() < -325:
        if ball.distance(l_paddle) < 50:
            ball.bounce_paddle()
        elif ball.xcor() < -400:
            ball.spawn()
            scoreboard.r_point()

    screen.update()
screen.exitonclick()
