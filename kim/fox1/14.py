for x in '0123456789abcdefg':
	a = int(f'1c3{x}6', 17) + int(f'1{x}2{x}', 17)
	if a%19 == 0:
		print(x, a//19)