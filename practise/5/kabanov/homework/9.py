ans = []
for N in range(1,1000):
	b = bin(N)[2:]
	b = '1' + b + '0' if N % 2 == 0 else '11' + b + '11'
	r = int(b,2)
	if r > 52:
		ans.append(r)
print(min(ans))