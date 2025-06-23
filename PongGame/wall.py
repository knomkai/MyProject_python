from turtle import Turtle
class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(0, -300)
        self.left(90)

    def create_wall(self):
        for i in range(65):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)
