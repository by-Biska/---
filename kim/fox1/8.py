from itertools import product
k =0
for x in product('АПКМР',repeat=4):
	s = ''.join(x)
	if s.count('А') == 1:
		k+=1
print(k)