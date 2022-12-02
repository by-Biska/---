from itertools import permutations as pm

k = 0

for x in pm('ИГРОК'):
	s = ''.join(x)
	if s[0]!= 'К' and 'РОК' not in s:
		k+=1
print(k)