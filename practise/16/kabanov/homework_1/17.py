def f(n):
	if n < 1:
		return 1
	else: return 3 + f(n-1) + f(n-3)
print(f(40))