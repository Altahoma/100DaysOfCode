from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

game_is_on = True
while game_is_on:
    snake.move()

    time.sleep(0.1)
    screen.update()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 360 or snake.head.xcor() < -360 or snake.head.ycor() > 360 or snake.head.ycor() < -360:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
