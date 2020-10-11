import random
import turtle as trtl

painter = trtl.Turtle()
R1 = trtl.Turtle()

painter.penup()
painter.goto(50,50)
painter.setheading(-180)
painter.pendown()
x = 0
while (x<2):
  painter.forward(200)
  painter.left(90)
  painter.forward(150)
  painter.left(90)
  x += 1

painter.penup()
painter.goto(75,75)
painter.setheading(-180)
painter.pendown()
x = 0
while (x<2):
  painter.forward(250)
  painter.left(90)
  painter.forward(200)
  painter.left(90)
  x += 1

R1.penup()
R1.color('red', 'red')
R1.width(1)
R1.goto(35,30)
R1.pendown()
R1.begin_fill()
R1.circle(2)
R1.end_fill()
R1.penup()
R1.goto(300,300)

def dieroll():

  min_value = 1
  max_value = 6
  print(random.randint(min_value, max_value))

dieroll()

trtl.done()
