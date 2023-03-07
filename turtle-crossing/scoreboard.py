from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.goto(-250, 250)
    self.current_level = 0
    self.update_level()
    
  def update_level(self):
    self.clear()
    self.current_level += 1
    self.write(f"Level: {self.current_level}", align="left", font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align="center", font=FONT)