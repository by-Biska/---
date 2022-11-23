for N in range(1,1000):
	b = bin(2*N)[2:]
	b += str(b.count('1') % 2)
	b += str(b.count('1') % 2)
	r = int(b,2)
	if r>1017:
		print(N)
		break