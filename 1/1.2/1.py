from turtle import *

speed(100)
def go(length):
  if length < 4:
    fd(length)
  else:
    go(length / 3)
    lt(60)
    fd(length / 3)
    rt(120)
    go(length / 3)
    lt(60)
    go(length / 3)

penup()
bk(300)
pendown()
tracer(0)
for side in range (3):
  go(200)
  rt(120)
update()
done()
