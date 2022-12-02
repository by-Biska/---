from itertools import product
k = 0
for x in product('КРСЛ','КРЕСЛО','КРЕСЛО','ЕО'):
	k+=1
print(k)