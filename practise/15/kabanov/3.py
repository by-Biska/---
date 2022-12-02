# 287
# def f(x,y): return (y+3*x<a) or (x>20) or (y>40)

# for a in range(1,200):
# 	if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
# 		print(a)

#363
k = 0
for x in range(100):
	for y in range(100):
		f = not(((x>6)and ((x+y)>=5)) or (y>=5))
		if f == 1:
			k+=1
print(k)