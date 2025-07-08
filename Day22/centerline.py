from turtle import Turtle

def draw_center_line():
    line = Turtle()
    line.hideturtle()
    line.color("white")
    line.penup()
    line.goto(0, -300)
    line.setheading(90)
    line.pensize(5)
    for _ in range(30):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)
