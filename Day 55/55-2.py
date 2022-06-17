def logging_decorator(func):
    def wrapper(*args):
        print(f'You called {func.__name__}{args}')
        print(f'It returned: {func(*args)}')
    return wrapper


@logging_decorator
def add_function(*args):
    return sum(args)


add_function(1, 2, 3)
