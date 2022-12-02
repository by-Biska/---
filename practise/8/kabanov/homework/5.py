from itertools import product
k =0
for x in product('САЛО', repeat=6):
	s = ''.join(x)
	if 0<s.count('О')<=3:
		print(s)
		k+=1
print(k)