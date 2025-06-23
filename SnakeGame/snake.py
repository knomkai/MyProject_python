import turtle
move_distance = 20
start_position = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.pens = []
    def create_snake(self):
        for position in start_position:
            self.add_segment(position)
    def add_segment(self,position):
        pen = turtle.Turtle()
        pen.shape("square")
        pen.color('white')
        pen.penup()
        pen.goto(position)
        self.pens.append(pen)
    def extend(self):
        self.add_segment(self.pens[-1].position())
    def move(self):
        for i in range(len(self.pens) - 1, 0, -1):
            set_x = self.pens[i - 1].xcor()
            set_y = self.pens[i - 1].ycor()
            self.pens[i].goto(set_x, set_y)
        self.pens[0].forward(move_distance)

    def left_move(self):
        if self.pens[0].heading() != 0:
            self.pens[0].setheading(180)

    def right_move(self):
        if self.pens[0].heading() != 180:
            self.pens[0].setheading(0)

    def up_move(self):
        if self.pens[0].heading() != 270:
            self.pens[0].setheading(90)

    def down_move(self):
        if self.pens[0].heading() != 90:
            self.pens[0].setheading(270)

    def reset(self):
        for i in self.pens:
            i.goto(1000,1000)
        self.pens.clear()
        self.create_snake()

