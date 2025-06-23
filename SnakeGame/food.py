from turtle import Turtle
import random
from RGB import bright_colors

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(bright_colors))
        self.speed('fastest')
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

    def refresh(self):
        self.color(random.choice(bright_colors))
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)



