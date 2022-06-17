from flask import Flask


def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper


def make_emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper


def make_underlined(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper


app = Flask(__name__)


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
