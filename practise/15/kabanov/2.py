# # 1
# def f(x): return (x&41==0)<=((x&119!=0)<=(x&a!=0))

# for a in range(1,100):
# 	if all(f(x) for x in range(1,10000)):
# 		print(a)


# 4
def f(x): 
	B = (x&17!=0) <= ((x&a!=0) <= (x&58!=0))
	D = (x&8==0) and (x&a!=0) and (x&58==0)
	return B <= D

for a in range(43,56):
	if all(f(x) == 0 for x in range(1,100000)):
		print(a)