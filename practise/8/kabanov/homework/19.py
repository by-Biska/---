from itertools import product

k=0
for x in product('АИМРЯ',repeat=4):
	s =''.join(x)
	k+=1
	if s == 'АРИЯ':
		print(k,s)