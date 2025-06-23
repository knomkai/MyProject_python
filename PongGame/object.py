from turtle import Turtle
import random
from RGB import elegant_colors
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.wall_list = []
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(1, 1)
        self.x = 1.75
        self.y = 1.75

    def move(self):
        new_x = self.xcor()+self.x
        new_y = self.ycor()+self.y
        self.goto(new_x,new_y)

    def change_direction_y(self):
        self.y *= -1

    def hit_a_ball(self):
        self.x *= -1
    def wall_bounce(self,y):
        if self.ycor() > y or self.ycor() < -y:
            self.change_direction_y()
            self.color(random.choice(elegant_colors))
    def reset(self):
        self.home()