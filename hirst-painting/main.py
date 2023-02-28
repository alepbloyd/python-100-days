import colorgram
import random
import turtle as t

colors = colorgram.extract('dots.png', 20)

screen = t.Screen()
t.setworldcoordinates(-500,-500,500,500)
screen.bgcolor("black")


rgb_colors = []

for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r,g,b)
  rgb_colors.append(new_color)

tim = t.Turtle()
tim.color("pink")
t.colormode(255)
tim.speed("slow")
tim.hideturtle()
tim.penup()

start_x = -450
start_y = -450

tim.setx(start_x)
tim.sety(start_y)

# 10 by 10 grid
# size 20 dots
# spaced 50 apart
def random_color():
  return random.choice(rgb_colors)

def check_color(color_tuple):
  r, g, b = color_tuple
  color_min = 200
  if r > color_min or g > color_min or b > color_min:
    return False
  else:
    return True  

non_white_rgb = []

for color in rgb_colors:
  if check_color(color):
    non_white_rgb.append(color)

def draw_circle(radius):
  tim.circle(20)

def draw_dots(width,height):
  # tim.hideturtle()
  tim.pensize(20)
  start_count = height

  while start_count > 0:
    for w in range(0,width):
      tim.color(random_color())
      tim.pendown()
      tim.forward(0)
      tim.penup()
      tim.forward(100)
      tim.penup()
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(width*100)
    tim.left(180)
    start_count -= 1


print(non_white_rgb)

draw_dots(10,10)


screen.exitonclick()