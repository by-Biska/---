ans = []

for x in range(17):
	a = (17**4 + 4*17**3 + 9*17**2 + x*17 + 3) + (x*17**3 + 6*17**2 + 17 + 2) + (x*17**3 + 5*17**2 + 4*17 + x)

	if a%7==0:
		ans.append(x)
print(ans)