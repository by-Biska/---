s = open('24-232.txt').readline()
s = s.split('0')
m = ''
for c in s:
	if sum(map(int, c))%5==0:
		m = max(m, c,key=len)
print(sum( int(d) for d in m))