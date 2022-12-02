s = [int(x[:-1]) for x in open('17var01.txt')][:-1]
s.append(53093)
ans = []
for i in range(len(s)-2):
	if s[i]%10!=3 and s[i+1]%10!=3 and s[i+2]%10!=3 and s[i]**2+s[i]**2+s[i]**2 > max(s):
		ans.append(s[i]**2+s[i]**2+s[i]**2)
print(len(ans), min(ans))