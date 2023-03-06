from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.x_movement = 1
    self.y_movement = 1
    self.shape("circle")
    self.color("white")
    self.penup()

  def move(self):
    new_x = self.xcor() + (self.x_movement * 10)
    new_y = self.ycor() + (self.y_movement * 10)
    self.goto(new_x, new_y)

  def bounce_top_or_bottom(self):
    self.y_movement *= -1


  def bounce_left_or_right(self):
    self.x_movement *= -1