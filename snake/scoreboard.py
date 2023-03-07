from turtle import Turtle

FONT = ('Arial', 32, 'normal')
MOVE = False
ALIGNMENT = "center"

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.current_score = 0
    with open("data.txt", mode="r") as file:
      self.high_score = int(file.read())
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
      with open("data.txt", mode="w") as file:
        file.write(str(self.current_score))
      with open("data.txt", mode="r") as file:
        self.high_score = int(file.read())
    self.current_score = 0
    self.update_scoreboard()


  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)
