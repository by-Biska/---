for N in range(1000):
	b = bin(N)[2:]
	b_sum = sum([int(c) for c in b])
	b += str((b_sum % 2))

	b_sum = sum([int(c) for c in b])
	b += str((b_sum % 2))
	if int(b,2) > 80:
		print