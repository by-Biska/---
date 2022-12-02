for x in range(1, 3000):
	b = bin(4**1014 - 2**x + 12)[2:]
	if b.count('0') == 2000: print(x)