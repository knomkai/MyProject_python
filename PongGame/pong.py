from turtle import Turtle
from RGB import elegant_colors , vs
import random
class Pong(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)
        self.ds = 45
        self.red = vs[0]
        self.white = vs[1]

    def move_up(self):
        new_y = self.ycor() + self.ds
        if new_y<270:
            self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y = self.ycor() - self.ds
        if new_y>-260:
            self.goto(self.xcor(), new_y)
    def hit_r(self,ball,x):
        if 369 > ball.xcor() > 351 and self.ycor() + 50 > ball.ycor() > self.ycor() - 50:
            ball.hit_a_ball()
            ball.color(random.choice(elegant_colors))
            x.color(self.red)
            self.color(self.white)
    def hit_l(self,ball,x):
        if -369 < ball.xcor() < -351 and self.ycor() + 50 > ball.ycor() > self.ycor() - 50:
            ball.hit_a_ball()
            ball.color(random.choice(elegant_colors))
            x.color(self.red)
            self.color(self.white)