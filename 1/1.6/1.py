from turtle import *
tracer(0)
setworldcoordinates(-6,-11, 6, 1)
for i in range(3):
  rt(60)
  fd(10)
  rt(60)
for x in range(-6, 6 + 1):
  for y in range(-11, 1+1):
    t = Turtle(shape="circle")
    t.penup()
    t.goto(x, y)
update()
done()