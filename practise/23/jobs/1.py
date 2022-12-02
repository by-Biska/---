d = set()

def f(curr, step):
	if step == 5:
		d.add(curr)
	else:
		f(curr+4,step+1)
		f(curr*2,step+1)
f(2,0)
print(len(d))