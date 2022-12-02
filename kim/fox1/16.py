from sys import *
setrecursionlimit(10000)

def f(n):
	if n == 1: return 4
	if n>1: return 2*n+f(n-1)
print(f(2010) - f(1028))