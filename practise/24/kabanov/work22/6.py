s = open('24.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}

m = 0
c = ''
for x in d:
	if d[x]> m:
		m = d[x]
		c = x
print(c, m)