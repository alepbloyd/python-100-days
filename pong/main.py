from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
  screen.update()
  ball.move()
  time.sleep(ball.ball_speed)

  if ball.ycor() > 295 or ball.ycor() < -295:
    ball.bounce_top_or_bottom()

  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_left_or_right()

  if ball.xcor() > 380:
    scoreboard.left_point()
    ball.reset_position()

  if ball.xcor() < -380:
    scoreboard.right_point()
    ball.reset_position()

screen.exitonclick()