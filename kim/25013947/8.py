from itertools import product

k = 0

for x in product('012345678', repeat=5):
	s = ''.join(x)
	if s[0]!='0' and s[0] not in '1357' and s[4] not in '18' and s.count('3') <= 1:
		k+=1
print(k)
