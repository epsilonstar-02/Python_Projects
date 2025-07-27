"""Of course. The exercise asks you to create a Python decorator function that can add HTML tags to the output of another function.

The specific challenge is to create three decorator functions:


make_bold
make_emphasis
make_underlined
These decorators should wrap the output of a function in <b>, <em>, and <u> tags respectively. You will then apply all three decorators to a single function to see their combined effect."""
import functools
from flask import Flask

app = Flask(__name__)

def make_bold(func):
    @functools.wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    @functools.wraps(func)
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/make_bold')
@make_bold
def bold_text():
    return "Hello World!"

@app.route('/make_emphasis')
@make_emphasis
def emphasis_text():
    return "Hello World!"

@app.route('/make_underlined')
@make_underlined
def underlined_text():
    return "Hello World!"

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()