for N in range(1000):
	b = bin(N)[2:]
	b = b[::-1]
	r = int(b,2)
	if r == 13:
		print(N)