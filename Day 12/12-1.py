from random import randint


def set_difficulty():
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def check_answer(answer, guess):
    if guess > answer:
        print('Too high.')
    elif guess < answer:
        print('Too low.')
    else:
        print(f'You got it! The answer was {answer}.')


def game():
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    answer = randint(1, 100)
    print('Psst', answer)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        check_answer(answer, guess)
        turns -= 1
        if turns == 0:
            print(f'You\'ve run out of guesses, you lose. The answer was {answer}.')
            return
        elif guess != answer:
            print('Guess again.')


game()
