def div(x):
	d = set()
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			d |= {i,x//i}
	return sorted(d)

k = 0

for x in range(1_200_001,1000000000000):
	d = div(x)
	if sum(d)!=0 and sum(d) < x/555:
		print(x, sum(d))
		k+=1
		if k==6:
			break