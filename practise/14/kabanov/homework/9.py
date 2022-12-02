x = 6*144**26 + 11*12**75 - 48
a = []
while x > 0:
	a.insert(0, x%12)
	x //= 12
print(a.count(11))