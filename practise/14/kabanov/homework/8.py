for x in range(1, 50000):
	s = 36**17 - 6**x + 71
	a = []
	while s > 0:
		a.insert(0, s%6)
		s //= 6

	if sum(a) == 61:
		print(x)
		break