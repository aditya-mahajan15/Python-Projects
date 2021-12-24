import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

# adding image as background to turtle screen
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="Enter a states name:").capitalize()
print(answer_state)

# reading csv file
data = pd.read_csv("50_states.csv")
# print(data)
states = data["state"].tolist()
for state in states:
    # print(state)
    if state == answer_state:
        print("Right")
    else:
        print("Wrong")
# print(states)


screen.exitonclick()