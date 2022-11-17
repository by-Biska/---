from fnmatch import fnmatch
k = 0
for s in open("24 (3).txt"):
	for i in range(len(s)-3):
		if fnmatch(s[i:i+4], 'Z?RO'):
			k+=1
			break
print(k)