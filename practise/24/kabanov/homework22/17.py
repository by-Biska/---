s = open("24 (14).txt").readline().strip()
k = 0

d = {x: 0 for x in sorted(set(s))}

for i in range(len(s)-2):
	if s[i] == s[i+2]:
		d[s[i+1]] +=1
print(max(d.values()))
print(d)