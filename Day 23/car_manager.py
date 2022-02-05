from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle(shape='square')
        new_car.penup()
        new_car.goto(320, randint(-240, 240))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.remove_car(car)

    def remove_car(self, car):
        self.cars.remove(car)
        car.hideturtle()
        del car

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
