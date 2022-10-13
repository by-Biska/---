from turtle import *
import random
speed(1)
pensize(3)
pencolor("orange")
def triangle(length=30):
    fillcolor((random.random(),random.random(),random.random()))
    begin_fill()
    for i in range(3):
        forward(length)
        left(120)
    end_fill()

for i in range(5):
  triangle(50)
  fd(50)