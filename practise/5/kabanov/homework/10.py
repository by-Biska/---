ans = []
for N in range(1,1000):
	b = bin(N)[2:]
	if sum([int(c) for c in b]) % 2 == 0:
		b = "10" + b[2:] + '0'
	else:
		b = "11" + b[2:] + '1'
	r = int(b,2)
	if r < 35:
		ans.append(N)
print(max(ans))