for x in range(1205):
	s = 125**200 - 5**x + 74
	a = []
	while s > 0:
		a.insert(0, s%5)
		s //= 5
	if a.count(4) == 100:
		print(x)