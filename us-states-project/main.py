import turtle
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
  answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state name?")
  answer_state_titlized = answer_state.title()
  if answer_state_titlized == "Exit":
    missing_states = pandas.Series(state_list)
    missing_states.to_csv("missing_states.csv", index=False)
    break
  if answer_state_titlized in state_list:
    correct_guesses.append(answer_state_titlized)
    StateWriter(answer_state_titlized)
    state_list.remove(answer_state_titlized)