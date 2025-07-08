from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(["blue", "red", "green", "yellow", "purple", "orange"]))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        import random
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)