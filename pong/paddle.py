from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
  def __init__(self, start_tuple):
    super().__init__()
    self.resizemode("user")
    self.speed("fastest")
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.penup()
    self.goto(start_tuple[0],start_tuple[1])

  def go_up(self):
    new_y = self.ycor() + MOVE_DISTANCE
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - MOVE_DISTANCE
    self.goto(self.xcor(), new_y) 