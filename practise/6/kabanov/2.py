from turtle import *
r = 5

tracer(0)

lt(90)

for i in range(10):
	for j in range(3):
		fd(10*r)
		rt(90)		
		fd(10*r)
		rt(270)
	rt(90)

up()
for x in range(-20,20):
	for y in range(-20,20):
		goto(x*r,y*r)
		dot(3, "blue")

update()
done()