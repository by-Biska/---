for N in range(2, 36):
	try:
		if int('132', N) + int('13', 8) == int('124', N+1):
			print(N)
	except:
		pass