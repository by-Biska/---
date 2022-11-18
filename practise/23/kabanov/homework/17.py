def f(c, end):
    if c > end:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 2, end) + f(c + 4, end) + f(c + 5, end)

for i in range(32, 10000000):
	if f(31, i) == 1001:
		print(i)
		break
