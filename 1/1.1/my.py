from turtle import *
shape("turtle")
shapesize(3)
color("purple", "pink")

speed(10)

raysNumber = 8 #int(input())
edge_size = 100
for step in range(raysNumber):
  forward(edge_size)
  right(360 / raysNumber)
  for step in range(3):
    forward(edge_size)
    left(360 /3 )
print("I just finished")
  
# forward(300)
# left(120)
# forward(300)
# left(120)
# forward(300)
# left(120)
# forward(300)
# left(120)
# forward(300)
# left(120)
# forward(300)