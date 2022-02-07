from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.goto(0, 330)
        self.load_score()
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update()

    def game_over(self):
        self.color('red')
        self.home()
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def load_score(self):
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())

    def save_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))
