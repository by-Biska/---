from itertools import permutations as pr

k =0
for x in pr('ВАЙФУ',r=4):
	s = ''.join(x)
	if s[0]!='Й' and 'ВФ' not in s and 'ФВ' not in s:
		k+=1
print(k)