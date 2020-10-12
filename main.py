import turtle as trtl
import random
painter = trtl.Turtle()

painter.speed(0)
painter.penup()
painter.goto(225,150)
painter.setheading(-180)
painter.pendown()
x = 0
while (x < 2):
  painter.forward(450)
  painter.left(90)
  painter.forward(300)
  painter.left(90)
  x += 1

''' painter.penup()
painter.goto(250,200)
painter.setheading(-180)
painter.pendown()
x = 0
while (x < 2):
  painter.forward(500)
  painter.left(90)
  painter.forward(400)
  painter.left(90)
  x += 1
'''

x = 0 
xinitial = -225
while (x < 11):
    xinitial += 37.501
    painter.penup()
    painter.goto(xinitial, 150)
    painter.setheading(270)
    painter.pendown()
    painter.forward(300)
    x += 1

painter.hideturtle()

p1score = 0
p2score = 0
player1_turtles = []
player2_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]


ystart1 = 100
for s in turtle_shapes:
    p1 = trtl.Turtle(shape = s)
    player1_turtles.append(p1)
    p1.penup()
    p1.speed(0)
    p1.fillcolor("red")
    p1.goto(187.5, ystart1)
    p1.setheading(180)
    ystart1 -= 50

ystart2 = 100
for s in turtle_shapes:
    p2 = trtl.Turtle(shape = s)
    player2_turtles.append(p2)
    p2.penup()
    p2.speed(0)
    p2.fillcolor('blue')
    p2.goto(-187.5, ystart2)
    ystart2 -= 50


def dieroll():

  min_value = 1
  max_value = 5
  global roll
  roll = random.randint(min_value, max_value)
  print ("You rolled a", roll)

def player1_move():
  turtle = int(input("Player 1, Choose a turtle to move"))
  distance = (37.501*roll)
  if (turtle == 1):
    turtle_y = 100
  elif (turtle == 2):
     turtle_y = 50
  elif (turtle == 3):
     turtle_y = 0
  elif (turtle == 4):
     turtle_y = -50
  elif (turtle == 5):
     turtle_y = -100
  for mt in player1_turtles:
    if (mt.ycor() == turtle_y):
     mt.forward(distance)

def player2_move():
  turtle = int(input("Player 2, Choose a turtle to move"))
  distance = (37.501*roll)
  if (turtle == 1):
    turtle_y = 100
  elif (turtle == 2):
     turtle_y = 50
  elif (turtle == 3):
     turtle_y = 0
  elif (turtle == 4):
     turtle_y = -50
  elif (turtle == 5):
     turtle_y = -100
  for mt in player2_turtles:
    if (mt.ycor() == turtle_y):
     mt.forward(distance)

def update_score():
  for t in player1_turtles:
    if (t.xcor() == 0):
      global p1score
      p1score += 1

  for t in player2_turtles:
    if (t.xcor() == 0):
      global p2score
      p2score += 1

while (p1score < 3 and p2score < 3):
  dieroll()
  player1_move()
  dieroll()
  player2_move()
  update_score()
  print("Player 1 score: ", p1score)
  print("Player 2 score: ", p2score)
  p1score = 0
  p2score = 0

trtl.done()
