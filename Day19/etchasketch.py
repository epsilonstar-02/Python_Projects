import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=tim.clear, key="c")
screen.exitonclick()