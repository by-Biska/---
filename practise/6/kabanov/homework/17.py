k = 0
for x in range(0, 100):
	for y in range(0, 100):
		if y < 90 and y < 3*x and y > x:
			k+=1
print(k)