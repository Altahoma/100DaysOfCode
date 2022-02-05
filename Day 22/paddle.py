from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        if position == 'right':
            self.goto(350, 0)
        elif position == 'left':
            self.goto(-350, 0)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)
