x = 51 *7**12 - 7**3 - 22
a = []
while x > 0:
	a.insert(0, x%7)
	x //= 7

print(sum(a))