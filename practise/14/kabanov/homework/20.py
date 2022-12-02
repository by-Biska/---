ans = []
for x in range(100000):
	if x<5**4 and len(bin(x)[2:]) >= 5 and hex(x)[-1] == 'c':
		ans.append(x)

print(len(ans), ans)