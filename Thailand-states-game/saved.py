class Game_Data():

    def __init__(self,x):
        with open(x) as a:
            self.data = a.read()
