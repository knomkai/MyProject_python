from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point_1 = 0
        self.point_2 = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,230)
        self.write(arg=f'{self.point_1}    {self.point_2}', font=('Courier', 40, 'normal'), align='center')

    def count_point_r(self):
        self.point_1 += 1
        self.clear()
        self.write(arg=f'{self.point_1}    {self.point_2}', font=('Courier', 40, 'normal'), align='center')
    def count_point_l(self):
        self.point_2 += 1
        self.clear()
        self.write(arg=f'{self.point_1}    {self.point_2}', font=('Courier', 40, 'normal'), align='center')
    def end_game(self):
        if self.point_1 == 10:
            self.clear()
            self.write(arg=f'WIN    LOSE', font=('Courier', 40, 'normal'), align='center')
            return True
        elif self.point_2 == 10:
            self.clear()
            self.write(arg=f'LOSE    WIN', font=('Courier', 40, 'normal'), align='center')
            return True