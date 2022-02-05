from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed = 5
        self.spawn()

    def move(self):
        self.forward(self.speed)

    def spawn(self):
        self.home()
        self.setheading(randint(0, 360))

    def bounce_wall(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_paddle(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
