def f(x): return (((x%6==0) <= (not(x%10==0))) or (x+a>121))

for a in range(1000):
	if all(f(x) for x in range(1,100000)):
		print(a)
		break