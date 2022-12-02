from fnmatch import *

for x in range(27,10**9+1, 27):
	if fnmatch(str(x), '1234?67?8'):
		print(x, x//27)
