from fnmatch import fnmatch
k = 0
for s in open('24 (9).txt'):
	for i in range(len(s)-3):
		if fnmatch(s[i:i+4], 'K?GE'):
			k+=1
			break
print(k)