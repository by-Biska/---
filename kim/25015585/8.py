from itertools import product
k = 0
for x in product('01234567', repeat=5):
	s = ''.join(x)
	if s[0]!=0 and s.count('5')==1:
		if s[0] == '5' and int(s[1])%2!=0:
			k+=1
		if s[1] == '5' and int(s[0])%2!=0 and int(s[2])%2!=0:
			k+=1
		if s[2] == '5' and int(s[1])%2!=0 and int(s[3])%2!=0:
			k+=1
		if s[3] == '5' and int(s[2])%2!=0 and int(s[4])%2!=0:
			k+=1
		if s[4] == '5' and int(s[3])%2!=0:
			k+=1
print(k)