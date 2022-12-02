def div(x):
	d = set()
	for i in range(1,int(x**0.5)+1):
		if x % i == 0:
			d |= {i, x//i}
	return sorted(d)

for x in range(10002000,10200000+1):
	if len(div(x))>=350:
		print(x, sum(int(d) for d in str(x)))