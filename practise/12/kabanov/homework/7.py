# s = '0' + '1'*28 + '2' * 34 + '3' * '45'
for one in range(1000):
	for two in range(1000):
		for three in range(1000):
			s = '0' + '1'*one + '2' * two + '3' * three

			while '01' in s or '02' in s or '03' in s:
				s = s.replace('01', '33120', 1)
				s = s.replace('02', '3120', 1)
				s = s.replace('03', '20', 1)

		if s.count("1") == 28 and s.count("2") == 34 and s.count("3") == 45:
			print(one)
# DOESN`T WORK