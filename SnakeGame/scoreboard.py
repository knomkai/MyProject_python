from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        self.point = 0
        with open('high_score.txt') as read:
            score = int(read.read())
        self.hight_score = score
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(arg=f'score: {self.point} /Hight score: {self.hight_score}' ,font=('Courier',20,'normal'),align='center')

    def get_points(self):
        self.point +=1
        self.clear()
        self.write(arg=f'score: {self.point} /Hight score: {self.hight_score}', font=('Courier',20,'normal'),align='center')

    def load_score(self):
        if self.point > self.hight_score:
            self.hight_score = self.point
            with open("high_score.txt",mode="w") as save:
                save.write(f"{self.hight_score}")
            with open('high_score.txt') as read:
                read_file = read.read()
                self.hight_score = int(read_file)
        self.point = 0
        self.clear()
        self.write(arg=f'score: {self.point} /Hight score: {self.hight_score}', font=('Courier', 20, 'normal'),align='center')





    # def game_over(self):
    #     self.reset()
    #     self.hideturtle()
    #     self.color('red')
    #     self.write(arg='GAME OVER',font=('Courier',40,'normal'),align='center')

    # def final_score(self):
    #     self.hideturtle()
    #     self.color('white')
    #     self.penup()
    #     self.goto(0,-200)
    #     self.write(arg=f'You score is :{self.point}', font=('Courier', 20, 'normal'), align='center')
