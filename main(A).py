import turtle as trtl
painter = trtl.Turtle()

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
    xinitial += 37.5
    painter.penup()
    painter.goto(xinitial, 150)
    painter.setheading(270)
    painter.pendown()
    painter.forward(300)
    x += 1

player1_turtles = []
player2_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
color1 = input("Player 1: Choose a color") 
color2 = input("Player 2: Choose a color") 

ystart1 = 100
for s in turtle_shapes:
    p1 = trtl.Turtle(shape = s)
    player1_turtles.append(p1)
    p1.penup()
    p1.fillcolor(color1)
    p1.goto(187.5, ystart1)
    p1.setheading(180)
    ystart1 -= 50

ystart2 = 100
for s in turtle_shapes:
    p2 = trtl.Turtle(shape = s)
    player2_turtles.append(p2)
    p2.penup()
    p2.fillcolor(color2)
    p2.goto(-187.5, ystart2)
    ystart2 -= 50

wn = trtl.Screen()
wn.mainloop()
