from turtle import Turtle, Screen
timmy = Turtle(shape='turtle')
timmy.color('blue')
timmy.forward(100)
my_screen = Screen()
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Bulbasaur"])
table.add_column("Type",["Electric","Water","Grass"])
table.align = "l"
print(table)