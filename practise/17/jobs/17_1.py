s = [int(i) for i in open('17-1.txt')]
k = 0
ans = []
ans2 = []
aver = sum(s)/len(s)
for i in range(len(s)-1):
	if abs(s[i])%10 + abs(s[i+1])%10 == 7:
		ans.append(s[i]+s[i+1])
		if s[i]<\aver and s[i+1]<\aver:
			ans2.append(s[i]+s[i+1])
print(len(ans), max(ans2)) 