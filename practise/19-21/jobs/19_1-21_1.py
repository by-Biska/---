# # 19
# def f(a,b,x,c,m):
# 	if a+b>=x and c!=0: return c%2 == m%2
# 	if c == m: return 0

# 	h = [f(a+2,b,x,c+1,m),f(a,b+2,x,c+1,m),f(a*2,b,x,c+1,m),f(a,b*2,x,c+1,m)]
# 	return any(h) if (c+1)%2 == m%2 else all(h)

# for x in range(9,100):
# 	if f(4,9,x,0,2):
# 		print(x)
# 		break

# 20
def f(a,b,x,c,m):
	if a+b>=x and c!=0: return c%2 == m%2
	if c == m: return 0

	h = [f(a+2,b,x,c+1,m),f(a,b+2,x,c+1,m),f(a*2,b,x,c+1,m),f(a,b*2,x,c+1,m)]
	return any(h) if (c+1)%2 == m%2 else all(h)

for x in range(26,100):
	for m in range(1,5):
		if f(10,15,x,0,m):
			if m == 3:print(x,m)
			break

# # 21
# def f(a,b,x,c,m):
# 	if a+b>=x and c!=0: return c%2 == m%2
# 	if c == m: return 0

# 	h = [f(a+2,b,x,c+1,m),f(a,b+2,x,c+1,m),f(a*2,b,x,c+1,m),f(a,b*2,x,c+1,m)]
# 	return any(h) if (c+1)%2 == m%2 else all(h)

# for x in range(26,100):
# 	for m in range(1,5):
# 		if f(8,8,x,0,m):
# 			print(x,m)
# 			break