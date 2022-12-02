def div(x):
	d = set()
	for i in range(1,int(x**0.5)+1):
		if x%i==0:
			d |= {i, x//i}
	return sorted(d)

for x in range(100500,100700):
	a=[]
	b=[]
	for i in div(x):
		if i%3==0:
			a.append(i)
		else:
			b.append(i)
		if len(a) > len(b)*2 :
			print(x,len(a)-]len(b))