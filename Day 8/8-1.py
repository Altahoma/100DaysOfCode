def greet():
    print('Welcome to day 8!')
    print('Today we\'ll learn more about function.')
    print('Good luck!')


greet()


def greet_with_name(name):
    print(f'Hello {name}')


greet_with_name('John')


def greet_with(name, location):
    print(f'How do you do {name}')
    print(f'What is it like in {location}?')


greet_with('John', 'London')
greet_with(location='London', name='John')
