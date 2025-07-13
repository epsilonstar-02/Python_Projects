from turtle import Turtle

class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.shape(None)
        self.penup()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.write(name)
