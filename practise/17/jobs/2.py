digits = [1]
x = n
while x > 0:
	digits += [x%2]
	x = x//10
digits += [1]