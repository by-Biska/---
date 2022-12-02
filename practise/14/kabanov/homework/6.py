for x in range(1, 10000):
	b = bin(4**2015 +  2**x - 2**2015 + 15)[2:]
	if b.count("1") == 500: print(x)
