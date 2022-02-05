from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.goto(0, 330)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color('red')
        self.home()
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()
