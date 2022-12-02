from itertools import product
k =0
for x in product('WXYZ','ABC','ABC','ABC','ABC','WXYZ'):
	k+=1
print(k)