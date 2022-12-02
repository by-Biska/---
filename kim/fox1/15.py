def f(x,y):
	return ((x<=3) <= (x**2<=a)) and ((y**2<=a) <= (y<=3))

for a in range(1000):
	if all(f(x,y) == 1 for x in range(1000) for y in range(1000)):
		print(a)