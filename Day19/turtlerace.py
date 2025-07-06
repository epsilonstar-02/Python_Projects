from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race!")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-280, y=y_positions[i])
    turtles.append(t)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() > 270:
            race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="Result", prompt=f"You won! The {winning_color} turtle is the winner! Press Enter to exit.")
            else:
                screen.textinput(title="Result", prompt=f"You lost! The {winning_color} turtle is the winner! Press Enter to exit.")
            break

screen.bye()
