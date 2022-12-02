s = [int(d) for d in open('17.txt')]
ans = []

for i in range(len(s)-1):
	if s[i]%6==0 and s[i+1]%6==0:
		ans.append(s[i]+s[i+1])

print(len(ans), max(ans))