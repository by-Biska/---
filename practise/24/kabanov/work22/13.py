m = 0
for s in open('24 (4).txt1'):
	if s.count('E')< 20:
		for x in set(s):
			a = s.find(x)
			b = s.rfind(x)
			m = max(m, b-a)
print(m)