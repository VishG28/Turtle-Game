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
grid.goto(100,75)
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
grid.goto(125,100)
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
R1.goto(85,57)
R1.pendown()
R1.begin_fill()
R1.circle(2)
R1.end_fill()
R1.penup()
R1.goto(300,300)

R2.penup()
R2.color('red', 'red')
R2.width(1)
R2.goto(85,27)
R2.pendown()
R2.begin_fill()
R2.circle(2)
R2.end_fill()
R2.penup()
R2.goto(300,300)

R3.penup()
R3.color('red', 'red')
R3.width(1)
R3.goto(85,-3)
R3.pendown()
R3.begin_fill()
R3.circle(2)
R3.end_fill()
R3.penup()
R3.goto(300,300)

R4.penup()
R4.color('red', 'red')
R4.width(1)
R4.goto(85,-33)
R4.pendown()
R4.begin_fill()
R4.circle(2)
R4.end_fill()
R4.penup()
R4.goto(300,300)

R5.penup()
R5.color('red', 'red')
R5.width(1)
R5.goto(85,-63)
R5.pendown()
R5.begin_fill()
R5.circle(2)
R5.end_fill()
R5.penup()
R5.goto(300,300)

B1.penup()
B1.color('blue', 'blue')
B1.width(1)
B1.goto(-85,57)
B1.pendown()
B1.begin_fill()
B1.circle(2)
B1.end_fill()
B1.penup()
B1.goto(300,300)

B2.penup()
B2.color('blue', 'blue')
B2.width(1)
B2.goto(-85,27)
B2.pendown()
B2.begin_fill()
B2.circle(2)
B2.end_fill()
B2.penup()
B2.goto(300,300)

B3.penup()
B3.color('blue', 'blue')
B3.width(1)
B3.goto(-85,-3)
B3.pendown()
B3.begin_fill()
B3.circle(2)
B3.end_fill()
B3.penup()
B3.goto(300,300)

B4.penup()
B4.color('blue', 'blue')
B4.width(1)
B4.goto(-85,-33)
B4.pendown()
B4.begin_fill()
B4.circle(2)
B4.end_fill()
B4.penup()
B4.goto(300,300)

B5.penup()
B5.color('blue', 'blue')
B5.width(1)
B5.goto(-85,-63)
B5.pendown()
B5.begin_fill()
B5.circle(2)
B5.end_fill()
B5.penup()
B5.goto(300,300)


def dieroll():

  min_value = 1
  max_value = 6
  print(random.randint(min_value, max_value))

dieroll()

trtl.done()
