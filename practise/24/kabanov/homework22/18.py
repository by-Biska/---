from fnmatch import fnmatch

s = open('24 (15).txt').readline().strip()

d = {x: 0 for x in sorted(set(s))}

for i in range(len(s)-4):
	if fnmatch(s[i:i+5], 'CB?BC'):
		d[s[i+2]] +=1
print(d)