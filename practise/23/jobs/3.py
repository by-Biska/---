def f(curr,end):
	if curr > end or curr == 50: return 0
	if curr == end: return 1
	if curr < end: return f(curr+3,end)+f(curr*2+1,end)+f(curr-curr%3+3,end)
print(f(5,23)*f(23,89))