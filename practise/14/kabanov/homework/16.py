for x in range(1,41):
	b = bin(x)
	if b[-4:] == '1011':
		print(x)
