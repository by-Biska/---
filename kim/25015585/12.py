for n in range(1000):
	s = '>'+ 15*'1' + n*'2' + 16*'3'
	while ">1" in s or ">2" in s or ">3" in s:
		if ">1" in s:
			s=s.replace('>1','22>',1)
		if ">3" in s:
			s=s.replace('>3','13>',1)
		if ">2" in s:
			s=s.replace('>2','1000>3',1)
	if sum([int(d) for d in s[:-1]])%len(s)==0:
		print(n)
		break