from turtle import Turtle

FONT = ('Arial', 42, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.current_score = 0
    
    self.speed("fastest")
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(0,230)
    self.pendown()
    self.write(self.current_score, move=False, align="center",font=('Arial', 42, 'normal'))
    
  def increment_score(self):
    self.current_score += 1
    self.clear()
    self.write(self.current_score, move=False, align="center",font=('Arial', 42, 'normal'))
