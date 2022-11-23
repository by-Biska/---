ans = []
for N in range(2,10000):
	c_odd = c_even = 0
	b = bin(N)[2:]
	for i in range(0,len(b),2):
		if b[i] == '0':
			c_odd += 1
	for i in range(1,len(b),2):
		if b[i] == '1':
			c_even += 1
	r = abs(c_even - c_odd)
	if r == 5:
		ans.append(N)
print(min(ans))