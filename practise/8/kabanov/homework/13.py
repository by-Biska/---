from itertools import product
k = 0
for x in product('0123456789', repeat=3):
	s = ''.join(x)
	if s[0]!='0' and s[0]<=s[1] and s[1]<=s[2]:
		print(s)
		k+=1
print(k)