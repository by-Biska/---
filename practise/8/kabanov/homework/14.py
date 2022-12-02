from itertools import permutations as pr

k =0
for x in pr('ДЕЙКСТРА', r=6):
	s = ''.join(x)
	if s.count('Й') == 1 and 'ЙЕ' not in s and 'ЙА' not in s and s[-1]!='Й':
		k+=1
print(k)