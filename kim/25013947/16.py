from functools import lru_cache

@lru_cache(None)
def f(n):
	if n == 1: return 1
	if n > 1: return n*f(n-1) - 1

for n in range(2, 1000):
	f(n)
print(f(1000)/f(997))