for x in range(21, 30):
	t = x
	a = []
	while x>0:
		a.insert(0, x%3)
		x //= 3
	if a[-2:] == [1,1]:
		print(t)