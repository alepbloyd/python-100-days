from turtle import Turtle

FONT = ('Arial', 40, 'normal')
MOVE = False
ALIGNMENT = "center"

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
    self.write(self.current_score, move=MOVE, align=ALIGNMENT,font=FONT)
    
  def increment_score(self):
    self.current_score += 1
    self.clear()
    self.write(self.current_score, move=MOVE, align=ALIGNMENT,font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)
