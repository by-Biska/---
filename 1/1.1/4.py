from turtle import *

setworldcoordinates(-30, -30, 30, 30)

def move(dx, dy):
  goto(xcor() + dx, ycor() + dy)
  
n = 4
a= -3 -13
b = -5 + 8
  
move(10,30)

for i in range(n):
  move(a,b)
  move(13, -8)