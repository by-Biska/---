from fnmatch import fnmatch
s = open('24 (2).txt').readline()

k = 0 

for i in range(len(s)-4):
	if fnmatch(s[i:i+5], 'B?X?A'):
		k+=1
print(k)