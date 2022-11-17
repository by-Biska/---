s = open("24.txt").readline().strip()
d = {x: 0 for x in sorted(set(s))}

for i in range(len(s)-2):
	if s[i] == 'X' and s[i+2] == 'Z':
		d[s[i+1]] += 1

m = max(d.values())

print(m, max(d,key=d.get))