from turtle import *
r = 20

tracer(0)

lt(90)

for i in range(7):
	rt(90)
	fd(4*r)
	for j in range(2):
		lt(90)
		fd(4*r)

up()
for x in range(-20,20):
	for y in range(-20,20):
		goto(x*r,y*r)
		dot(3, "blue")

update()
done()