a = [0]*300
a[10] = 1
for i in range(10,100):
	if a[i]>0:
		a[i+3] = 1
		a[i*3] = 1
# print(a)
print(sum([i%2==1 and a[i] > 0 for i in range(100)]))