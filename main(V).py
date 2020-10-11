import random
import turtle as trtl

grid = trtl.Turtle()
R1 = trtl.Turtle()
R2 = trtl.Turtle()
R3 = trtl.Turtle()
R4 = trtl.Turtle()
R5 = trtl.Turtle()
B1 = trtl.Turtle()
B2 = trtl.Turtle()
B3 = trtl.Turtle()
B4 = trtl.Turtle()
B5 = trtl.Turtle()

grid.penup()
grid.goto(50,50)
grid.setheading(-180)
grid.pendown()
x = 0
while (x<2):
  grid.forward(200)
  grid.left(90)
  grid.forward(150)
  grid.left(90)
  x += 1

grid.penup()
grid.goto(75,75)
grid.setheading(-180)
grid.pendown()
x = 0
while (x<2):
  grid.forward(250)
  grid.left(90)
  grid.forward(200)
  grid.left(90)
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
