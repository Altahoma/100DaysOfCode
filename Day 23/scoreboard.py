from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def lvl_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color('red')
        self.home()
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)
