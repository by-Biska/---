x = 7**103 + 20*7**204-3*7**57 + 97

a  = []

while x>0:
	a.insert(0, x%7)
	x //= 7
print(a.count(6))