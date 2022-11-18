s = open('24var02.txt').readline()


min_s = 1000000000000000000000

for start in range(len(s)):
	s1 = s[start:]
	count =0
	count_A =0
	for i in s1:
		if i:
			count +=1
			if i == 'A':
				count_A += 1
				if count_A == 35:
					min_s = min(min_s,count)
					count =0
					count_A =0
