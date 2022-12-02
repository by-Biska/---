from itertools import product as pr
k=0
for x in pr('АГИЛМОРТ', repeat=4):
	s =''.join(x)
	k+=1
	if s[-2:] == 'ИМ':
		print(k,s)