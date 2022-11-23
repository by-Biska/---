for N in range(1000):
	b = bin(N)[2:]
	b += b[-1]
	b += '0' if b.count('1') % 2 == 0 else '1'
	b += '0' if b.count('1') % 2 == 0 else '1'
	r = int(b,2)
	if r > 130:
		print(N)
		break