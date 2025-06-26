import turtle
import pandas
from mark import State_Mark
from saved import Game_Data

screen = turtle.Screen()
screen.title("Thailand Game")
image = "Thai map.gif" # load image
screen.addshape(image) # add new shape (background)
turtle.shape(image) # Background

data = pandas.read_csv("data.csv") # import data state to 'data' verible
data_dict = data.to_dict() # chang data type to 'dict'
state_data = {} # this list for {state_name :  x,y }
for i in range(len(data)):
    state_names = data_dict['จังหวัด'][i]
    x = data_dict['X'][i]
    y = data_dict['Y'][i]
    state_data[f'{state_names}'] = []
    state_data[f'{state_names}'].append(x)
    state_data[f'{state_names}'].append(y)


state = []
miss_state = []
while len(state)<77:

    answer_state = screen.textinput(title=f"Now {len(state)}/77 state correct",prompt="What's another state?")
    if answer_state == "Exit":
        for i in state_data:
            if i not in state:
                miss_state.append(i)
        print(miss_state)
        break

    if answer_state in state_data:

        if answer_state in state:
            print("You already answer that")
        else:
            state.append(answer_state)
            State_Mark(x=state_data[f'{answer_state}'][0],y=state_data[f'{answer_state}'][1])



