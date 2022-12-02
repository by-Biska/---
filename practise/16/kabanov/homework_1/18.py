from functools import *

@lru_cache(None)
def f(n):
	s = n*n
	if n>1:
		s += (2*n+1) + f(n-2) + f(n//3)
	return s

print(f(100))