from fnmatch import fnmatch
s = open('24-230.txt').readline()
s = s.split('KK')
m = 0
for c in s:
	if 'K' not in c and fnmatch(c, '43??78???34'):
		m = max(m, int(c))

k = 1
while m>0:
	if (m%10)%2!=0:
		k*=m%10
	m//=10
print(k)