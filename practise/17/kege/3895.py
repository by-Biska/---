ans = []
ans2 = []

s = [int(i) for i in open('17(1).txt')]
aver = sum(s)/len(s)
for i in range(len(s)-3):
	if s[i]*s[i+3]<s[i+1]*s['i+2]:
		ans.append(s[i+1]+s[i+2])
		if s[i+1]> aver or s[i+2]>aver:
			ans2.append(s[i+1]+s[i+2])
print(max(ans),len(ans2))