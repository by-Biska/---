def f(n):
	if n<=18: return n+3
	if n>18 and n%3==0: return (n//3) * f(n//3)+n - 12
	if n>18 and n%3!=0: return f(n-1) + n * n + 5

k=0
for n in range(1,1001):
	f_ans = [int(x) for x in str(f(n))]
	if all(x%2==0 for x in f_ans):
		k+=1
print(k)