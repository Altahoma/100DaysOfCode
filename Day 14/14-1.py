from art import logo, vs
from game_data import data
from random import choice


print(logo)
b = choice(data)
score = 0
end_of_game = False
while not end_of_game:
    a = b
    b = choice(data)
    while a == b:
        b = choice(data)
    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
    print(vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
    guess = input('Who has more followers? Type "A" or "B": ').upper()
    if guess == 'A' and a['follower_count'] > b['follower_count']:
        score += 1
        print(f'You\'re right! current score: {score}')
    elif guess == 'B' and b['follower_count'] > a['follower_count']:
        score += 1
        print(f'You\'re right! current score: {score}')
    else:
        end_of_game = True
        print(f'Sorry, that\'s wrong. Final score: {score}')
        break
