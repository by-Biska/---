x = 2*27**7 + 3**10 - 9
a = []
while x > 0:
	a.insert(0, x%3)
	x //= 3
print(a.count(0))