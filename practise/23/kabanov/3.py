def f(c,end):
	if c > end or c == 14: return 0
	if c == end: return 1
	if c<end: return f(c+1, end) + f(c+3,end)

print(f(2,9)*f(9,18))