from functools import *

@lru_cache(None)
def f(n):
	if n<3: return n+1
	if n>=3 and n%2==0: return f(n-2) + n -2
	if n>=3 and n%2!=0: return f(n+2) + n + 2

k = 0
for n in range(0,10000):
	try:
		if f(n)>=100000:
			break
		if 10000<=f(n)<100000:
			k+=1
	except:
		pass

print(k)