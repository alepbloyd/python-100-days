from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Snax")

seg_1 = Turtle()
seg_2 = Turtle()
seg_3 = Turtle()

seg_list = [seg_1, seg_2, seg_3]

for segment in seg_list:
  segment.shape("square")
  segment.color("white")

seg_1.goto(0,0)
seg_2.goto(-20,0)
seg_3.goto(-40,0)

screen.exitonclick()