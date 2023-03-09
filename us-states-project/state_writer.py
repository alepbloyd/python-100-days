from turtle import Turtle
import pandas

FONT = ('Arial', 18, 'normal')
MOVE = False
ALIGNMENT = "center"

class StateWriter(Turtle):
  def __init__(self, state_name):
    super().__init__()
    self.speed("fastest")
    self.hideturtle()
    self.color("black")
    self.penup()
    self.csv_data = pandas.read_csv("50_states.csv")
    self.state_row = self.csv_data[self.csv_data.state == state_name]
    self.state_name = state_name
    self.x_cor = int(self.state_row.x)
    self.y_cor = int(self.state_row.y)
    self.goto(self.x_cor, self.y_cor)
    self.pendown()
    self.write_state()

  def write_state(self):
    self.write(self.state_name, move=MOVE, align=ALIGNMENT, font=FONT)