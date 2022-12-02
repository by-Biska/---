from itertools import product

k = 0
for x in product('ЕЛМРУ', repeat=4):
	s = ''.join(x)
	k+=1
	# print(k, s)
	if s[0]== 'Л':
		print(k)
		break