def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while not wall_on_right():
        turn_right()
        if front_is_clear():
            move()
    if front_is_clear():
        move()
    else:
        turn_left()
