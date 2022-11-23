for N in range(1000):
	p = N
	string = ''
	while N > 0:
		string += str(N%3)
		N//=3
	string = string[::-1]
	string += str(p%3)
	r = int(string, 3)
	if r > 99:
		print(r)
		break