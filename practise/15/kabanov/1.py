# 1
# for a in range(1,1000):
# 	flag = 1

# 	for x in range(1,100000):
# 		f = (a%9==0) and ((280%x==0) <= ((a%x!=0) <= (730%x!=0)))
# 		if f==0:
# 			flag = 0
# 			break
# 	if flag:
# 		print(a)

# # 2
# for a in range(1,100):
# 	for x in range(1,100000):
# 		f = ((x%34==0) and (x%51!=0)) <= ((x%a!=0) or (x%51==0))
# 		if f==0:
# 			break
# 	else:
# 		print(a)

# 3
def f(x):
	return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)

for a in range(1,10000):
	if all(f(x)==1 for x in range(1, 1000000)):
		print(a)