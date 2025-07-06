import turtle
import random

# Damien Hirst dots painting with turtle
screen = turtle.Screen()
screen.colormode(255)

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Define a palette of colors (can be expanded)
color_list = [
    (239, 246, 241), (236, 239, 244), (245, 240, 235), (236, 245, 241),
    (240, 234, 238), (237, 245, 238), (244, 239, 236), (236, 239, 244),
    (230, 57, 70), (241, 196, 15), (46, 204, 113), (52, 152, 219),
    (155, 89, 182), (52, 73, 94), (22, 160, 133), (39, 174, 96),
    (142, 68, 173), (243, 156, 18), (211, 84, 0), (192, 57, 43)
]

# Set starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_dots = 100
dot_size = 20
gap = 50

for dot_count in range(1, num_dots + 1):
    tim.dot(dot_size, random.choice(color_list))
    tim.forward(gap)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(gap)
        tim.setheading(180)
        tim.forward(gap * 10)
        tim.setheading(0)

screen.exitonclick()
