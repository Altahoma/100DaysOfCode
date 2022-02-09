from turtle import Turtle, Screen
import pandas
import random


screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)

bg = Turtle().shape(image)

board = Turtle()
board.hideturtle()
board.penup()

printer = Turtle()
printer.hideturtle()
printer.penup()

with open('50_states.csv') as file:
    data = pandas.read_csv(file)
    states_list = data.to_dict('records')
print(states_list)

score = 0
while score < 50:
    screen.update()
    state_dict = random.choice(states_list)
    print(state_dict)
    board.goto(state_dict['x'], state_dict['y'])
    board.write('???', False, align='center', font=('Arial', 16, 'normal'))
    guess = screen.textinput(title=f'{score}/50 States Correct', prompt='Guess the state\'s name?').title()
    if guess == state_dict['name']:
        score += 1
        states_list.remove(state_dict)
        printer.goto(state_dict['x'], state_dict['y'])
        printer.write(guess, False, align='center', font=('Arial', 16, 'normal'))
    elif guess == 'Exit':
        states_to_write = []
        for state in states_list:
            states_to_write.append(state['name'])
        new_data = pandas.DataFrame(states_to_write)
        new_data.to_csv('states_to_learn.csv', header=False, index=False)
        break
    board.clear()
    print(len(states_list))

screen.exitonclick()
