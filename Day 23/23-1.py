import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.onkey(player.move_up, 'Up')

game_is_on = True
counter = 6
while game_is_on:
    counter -= 1
    if counter == 0:
        counter = 6
        car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()
            print(len(car_manager.cars))
            break

    if player.is_at_finish_line():
        car_manager.increase_speed()
        score_board.lvl_up()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
