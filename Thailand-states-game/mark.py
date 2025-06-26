from turtle import Turtle

class State_Mark(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('red')
        self.shapesize(0.5)
        self.goto(x,y)

