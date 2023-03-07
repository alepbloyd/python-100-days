from turtle import Turtle

FONT = ('Arial', 32, 'normal')
MOVE = False
ALIGNMENT = "center"

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.current_score = 0
    self.high_score = 0
    self.speed("fastest")
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(0,230)
    self.pendown()
    self.update_scoreboard()
    
  def increment_score(self):
    self.current_score += 1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=MOVE, align=ALIGNMENT,font=FONT)

  def reset(self):
    if self.current_score > self.high_score:
      self.high_score = self.current_score
    self.current_score = 0
    self.update_scoreboard()


  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)
