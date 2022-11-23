k = []
for N in range(1,1000):
	b = bin(N)[2:]
	b_sum = str(sum([int(c) for c in b]) % 2)
	b = b + b_sum
	b_sum = str(sum([int(c) for c in b]) % 2)
	b = b + b_sum
	r = int(b,2)
	if r < 80:
		k.append(r)
print(k, len(k))