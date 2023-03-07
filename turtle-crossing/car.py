from turtle import Turtle

class Car(Turtle):
    
    def __init__(self, color, start_y, move_increment):
      super().__init__()
      self.shape("square")
      self.color(color)
      self.penup()
      self.move_increment = move_increment
      self.shapesize(stretch_wid=1,stretch_len=2)
      self.goto(300,start_y)
      self.setheading(180)

    def move_left(self):
      self.forward(self.move_increment)