# # 19
# def f(a,c,m):
# 	if a<=12: return a%2 == m%2
# 	if c==m: return 0
# 	h = [f(a-1,c+1,m)]
# 	if a%2==0: h+=[f(a//2,c+1,m)]
# 	return any(h) if (c+1)%2== m%2 else all(h)

# for a in range(1,1000):
# 	for m in range(1,5):
# 		if f(a,0,m):
# 			if m==2: print(a,m)
# 			break

# # 20
# def f(a,c,m):
# 	if a<=12: return a%2 == m%2
# 	if c==m: return 0
# 	h = [f(a-1,c+1,m)]
# 	if a%2==0: h+=[f(a//2,c+1,m)]
# 	return any(h) if (c+1)%2== m%2 else all(h)

# for a in range(1,1000):
# 	for m in range(1,5):
# 		if f(a,0,m):
# 			if m==3: print(a,m)
# 			break

# 21
def f(a,c,m):
	if a<=12: return a%2 == m%2
	if c==m: return 0
	h = [f(a-1,c+1,m)]
	if a%2==0: h+=[f(a//2,c+1,m)]
	return any(h) if (c+1)%2== m%2 else all(h)

for a in range(1,1000):
	for m in range(1,5):
		if f(a,0,m):
			if m==4: print(a,m)
			break