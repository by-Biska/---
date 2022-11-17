m = 'A'*1000
s1 = ''
for s in open('24 (4).txt'):
	if s.count('A') < m.count('A'):
		m = s.strip()
	s1 += s.strip()

d = {x: m.count(x) for x in sorted(set(m))}
# LETTER: V
d1 = {x: s1.count(x) for x in sorted(set(s1))}
print('V',  d1['V'])